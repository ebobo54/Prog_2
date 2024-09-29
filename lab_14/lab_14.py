from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    ProjectID = Column(Integer, primary_key=True)
    Name = Column(String)
    StartDate = Column(Date)
    EndDate = Column(Date)
    tasks = relationship("Task", back_populates="project")

class Employee(Base):
    __tablename__ = 'employees'
    EmployeeID = Column(Integer, primary_key=True)
    Name = Column(String)
    Position = Column(String)
    tasks = relationship("Task", back_populates="employee")

class Task(Base):
    __tablename__ = 'tasks'
    TaskID = Column(Integer, primary_key=True)
    Description = Column(String)
    Status = Column(String)
    ProjectID = Column(Integer, ForeignKey('projects.ProjectID'))
    EmployeeID = Column(Integer, ForeignKey('employees.EmployeeID'))
    project = relationship("Project", back_populates="tasks")
    employee = relationship("Employee", back_populates="tasks")

# Создание базы данных
engine = create_engine('sqlite:///company_projects.db')
Base.metadata.create_all(engine)

# Заполнение базы данных
Session = sessionmaker(bind=engine)
session = Session()

# Пример данных
projects = [
    Project(Name="Project Alpha", StartDate="2023-01-01", EndDate="2023-06-30"),
    Project(Name="Project Beta", StartDate="2023-02-15", EndDate="2023-07-15")
]

employees = [
    Employee(Name="John Doe", Position="Developer"),
    Employee(Name="Jane Smith", Position="Project Manager")
]

tasks = [
    Task(Description="Task 1 for Alpha", Status="Completed", ProjectID=1, EmployeeID=1),
    Task(Description="Task 2 for Alpha", Status="In Progress", ProjectID=1, EmployeeID=2),
    Task(Description="Task 1 for Beta", Status="Not Started", ProjectID=2, EmployeeID=1)
]

session.add_all(projects)
session.add_all(employees)
session.add_all(tasks)
session.commit()
