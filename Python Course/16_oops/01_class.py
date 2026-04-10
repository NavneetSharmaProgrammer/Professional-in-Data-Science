class Employee:
    company = "HP"  # Class variable

    def get_salary(self): # Instance method
        return 65000

e1 = Employee()  # Creating an instance of Employee
print(e1.get_salary())  # Calling the instance method
print(e1.company)  # Accessing class variable from instance

e2 = Employee()  # Creating another instance of Employee
print(e2.get_salary())  # Calling the instance method
print(e1.company)  # Accessing class variable from instance