#abstract class that cannot be instantiated, but other classes inherit from it
#use it to make blueprint classes

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @abstractmethod
    def show_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary


    def show_salary(self):
        return f"Salary is: {self.salary}"

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, pay_rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.pay_rate = pay_rate



    def show_salary(self):
        return f"Salary is: {self.worked_hours * self.pay_rate}"

class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for emp in self.employee_list:
            print(f"{emp.first_name} {emp.last_name}\t ${emp.show_salary()}")


