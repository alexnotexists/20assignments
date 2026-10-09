employees = {
    101: {"name": "Ram", "department": "IT", "salary": 30000},
    102: {"name": "Sita", "department": "HR", "salary": 35000},
    103: {"name": "Hari", "department": "Sales", "salary": 25000},
    104: {"name": "Gita", "department": "Finance", "salary": 40000},
    105: {"name": "Shyam", "department": "IT", "salary": 45000}
}

def findemployee(emp_id):
    if emp_id in employees:
        return employees[emp_id]
    else:
        raise ValueError("Employee ID not found!")

def yearlysalary(salary):
    return salary * 12

def increasesalary(salary, percentage):
    return salary + (salary * percentage / 100)

try:
    emp_id = int(input("Enter Employee ID: "))

    employee = findemployee(emp_id)

    old_salary = employee["salary"]
    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])
    print("Old Salary:", old_salary)

    percentage = float(input("Enter salary increase percentage: "))

    if percentage < 0:
        raise ValueError("Percentage cannot be negative!")

    new_salary = increasesalary(old_salary, percentage)
    employee["salary"] = new_salary

    print("New Salary:", new_salary)
    print("Yearly Salary:", yearlysalary(new_salary))

except ValueError as e:
    print(e)