# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

# Child class for Managers
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Call parent class's __init__
        self.team_size = team_size

    def display_info(self):
        return f"{super().display_info()}, Team Size: {self.team_size}"

# Child class for Developers
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        #calling display_info from the parent class
        return f"{super().display_info()}, Language: {self.programming_language}"


#Multi Level
#Grandparent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting."

#Parent class
class Car(Vehicle):
    def drive(self):
        return f"{self.brand} is driving."

#Child class
class ElectricCar(Car):
    def charge(self):
        return f"{self.brand} is charging."

