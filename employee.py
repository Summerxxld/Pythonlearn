class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def give_raise(self,amount):
        self.salary+=amount

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.employees=[]
    
    def add_employee(self,employee):
        self.employees.append(employee)

    def remove_employee(self,employee):
        self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
    

employee1=Employee(name="John",salary=50000)
employee2=Employee(name="Jane",salary=60000)    
manager=Manager(name="Alice",salary=100000)

manager.add_employee(employee1)
manager.print_employees()

manager.add_employee(employee2)
manager.print_employees()

print(f"Before:{employee1.salary}")
employee1.give_raise(10000)
print(f"After:{employee1.salary}")

manager.print_employees()
manager.remove_employee(employee1)
manager.print_employees()
