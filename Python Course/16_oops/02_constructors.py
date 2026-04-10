class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Instance variable
        self.name = name     # Instance variable
        self.bond = bond     # Instance variable

    def get_salary(self):
        return self.salary
        
    def get_info(self):
        print(f"The salary of {self.name} is {self.salary} and the bond is {self.bond} years.")

e1 = Employee(50000, "Alice", 2)  # Creating an instance of Employee
# print(e1.get_salary())  # Calling the instance method
e1.get_info()  # Calling the instance method to get info