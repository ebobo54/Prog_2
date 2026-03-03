# Получение всех проектов
def get_all_projects():
    return session.query(проекты).all()

# Получение всех сотрудников
def get_all_employees():
    return session.query(сотрудники).all()

# Получение всех задач
def get_all_tasks():
    return session.query(задачи).all()

# Получение задач по проекту
def get_tasks_by_project(project_id):
    return session.query(задачи).filter(задачи.ProjectID == project_id).all()

# Получение задач по сотруднику
def get_tasks_by_employee(employee_id):
    return session.query(задачи).filter(задачи.EmployeeID == employee_id).all()

# Пример использования запросов
projects = get_all_projects()
for project in projects:
    print(f"Project: {project.Name}, Start: {project.StartDate}, End: {project.EndDate}")

employees = get_all_employees()
for employee in employees:
    print(f"Employee: {employee.Name}, Position: {employee.Position}")

tasks = get_all_tasks()
for task in tasks:
    print(f"Task: {task.Description}, Status: {task.Status}, ProjectID: {task.ProjectID}, EmployeeID: {task.EmployeeID}")

tasks_by_project = get_tasks_by_project(1)
for task in tasks_by_project:
    print(f"Task for Project 1: {task.Description}, Status: {task.Status}")

tasks_by_employee = get_tasks_by_employee(1)
for task in tasks_by_employee:
    print(f"Task for Employee 1: {task.Description}, Status: {task.Status}")
