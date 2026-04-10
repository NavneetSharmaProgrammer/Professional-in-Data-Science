class Employee:
    company = "ASUS"  # Class variable

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Instance variable
        self.name = name     # Instance variable
        self.bond = bond     # Instance variable
        self.company = company  # Instance variable

    def get_salary(self):
        return self.salary
        
    def get_info(self):
        print(f"The salary of {self.name} is {self.salary} and the bond is {self.bond} years.")

e1 = Employee(50000, "Alice", 2, "TATA")  # Creating an instance of Employee
print(e1.company)
print(Employee.company)  # Accessing class variable through class name

# Object introspection
print(dir(e1))  # List all attributes and methods of the instance
