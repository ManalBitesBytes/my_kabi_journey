#Encapsulation

print("Encapsulation:")
from encapsulatoin import Body_Measures
# we can access height & weight because of property decorator
MyBody = Body_Measures(150 , 47)
print(MyBody.height)
print(MyBody.weight)

#we can set height to new value because of setter
MyBody.height = 155
print(MyBody.height)

#we can't change the value of weight since I have no setter
#MyBody.weight = 45


#inheritance:
print(".............................................")
print("Inheritance:")

from inheritance import *
print("#1")
manager = Manager("Jana", 80000, 5)
developer = Developer("Sara", 70000, "Python")
print(manager.display_info())   # Output: Name: Alice, Salary: $80000, Team Size: 5
print(developer.display_info()) # Output: Name: Bob, Salary: $70000, Language: Python

print("#2")
electric_car = ElectricCar("Tesla")
print(electric_car.start())
print(electric_car.drive())
print(electric_car.charge())

#abstraction
print(".............................................")
print("Abstraction:")
from abstraction import *

payroll = Payroll()

payroll.add(FullTimeEmployee('Manal', 'Qatab', 12000))
payroll.add(FullTimeEmployee('Lara', 'Ahmed', 11500))
payroll.add(HourlyEmployee('Sara', 'Khalid', 200, 50))
payroll.add(HourlyEmployee('Jood', 'Waleed', 150, 110))


payroll.print()

print(".............................................")
print("Polymorphism:")
# Polymorphism in action
from polymorphism import *
file_readers = [TextFileReader(), CSVFileReader(), JSONFileReader()]

for reader in file_readers:
    print(reader.read())