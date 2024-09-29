from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    address = Column(String)
    orders = relationship("Order", back_populates="customer")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(Date)
    details = relationship("OrderDetail", back_populates="order")
    customer = relationship("Customer", back_populates="orders")

class OrderDetail(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    order = relationship("Order", back_populates="details")
    product = relationship("Product")

# Создание базы данных
engine = create_engine('sqlite:///shop.db')
Base.metadata.create_all(engine)

# Заполнение базы данных
Session = sessionmaker(bind=engine)
session = Session()

# Добавление данных
customer = Customer(name="Иван Иванов", email="ivan@example.com", address="Москва, Россия")
customer2 = Customer(name="Мария Петрова", email="maria@example.com", address="Санкт-Петербург, Россия")
customer3 = Customer(name="Алексей Смирнов", email="alexey@example.com", address="Новосибирск, Россия")

product = Product(name="Чайник", price=1500.50, quantity=10)
product2 = Product(name="Микроволновка", price=5000.00, quantity=15)
product3 = Product(name="Холодильник", price=20000.00, quantity=5)

order = Order(customer=customer, order_date=date.today())
detail = OrderDetail(order=order, product=product, quantity=1, price=1500.50)

# Получение заказов клиента:
def get_customer_orders(customer_name):
    return session.query(Order).join(Customer).filter(Customer.name == customer_name).all()

# Подсчет общей стоимости заказа:
def order_total(order_id):
    order_details = session.query(OrderDetail).filter(OrderDetail.order_id == order_id).all()
    return sum(detail.price * detail.quantity for detail in order_details)

# Получение товаров с низким количеством на складе:
def low_stock_products(threshold=5):
    return session.query(Product).filter(Product.quantity <= threshold).all()

# Получение клиентов из определенного города:
def customers_from_city(city_name):
    return session.query(Customer).filter(Customer.address.contains(city_name)).all()

# Получение деталей заказа с информацией о товаре:
def order_details_with_product_info(order_id):
    return session.query(OrderDetail, Product).join(Product).filter(OrderDetail.order_id == order_id).all()


session.add(customer)
session.add(product)
session.add(customer2)
session.add(customer3)
session.add(product2) 
session.add(product3)
session.add(order)
session.add(detail)
session.commit()