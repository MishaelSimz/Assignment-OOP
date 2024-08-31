# Task 1
class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name          # Private variable for employee's name
        self.__emp_id = emp_id      # Private variable for employee's ID
        self.__salary = salary      # Private variable for employee's salary

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for employee ID
    def get_emp_id(self):
        return self.__emp_id

    # Setter for employee ID
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary with validation to prevent negative values
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")

employee = Employee("Mishael Simfukwe", 100624, 50000)
print(employee.get_name())
print(employee.get_salary())

employee.set_salary(55000)
print(employee.get_salary())


# Task 2
# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start_engine(self):
        print("Starting engine...")

# Derived class for Car
class Car(Vehicle):
    def start_engine(self):
        print(f"The {self.make} {self.model} car engine roars to life!")

# Derived class for Truck
class Truck(Vehicle):
    def start_engine(self):
        print(f"The {self.make} {self.model} truck engine starts with a rumble!")

# Function demonstrating polymorphism
def start_vehicle_engine(vehicle):
    vehicle.start_engine()

my_car = Car("Lexus", "IS250")
my_truck = Truck("Chevrolet", "Silverado")

start_vehicle_engine(my_car) 
start_vehicle_engine(my_truck)
