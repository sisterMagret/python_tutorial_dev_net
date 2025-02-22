
"""
1. Introduction to Object Oriented Programming (OOP)
---------------------------------------------------
Basic Terminology
---------------------------------------------------
- class: is a blue print for creating objects
- objects: An instance of a class
- attribute: a variable that holds data inside an object
- method: is a function defined inside a class that operates on objects

2. Create class and Objects
- A class is define using the `class` keyword in python
- Objects are created from class

3. Instance VS Class Attributes
- instance attributes: are define within __init__ method (constructor method) 
  and is unique to each object.
- class attribute: shared across all instances

4. Principles of OOP:
    a. Encapsulation: restricts direct access to object attributes, 
       ensuring data security.
       example: private and protected attributes
       
    b. Inheritance: allows a child class to inherit methods 
       and attributes from a parent class
       
    c. Polymorphism: allows methods to be used interchangeably across different classes
    
    d. Abstraction: hides complex details and expose only necessary features.
    
5. Duck Typing: python allows dynamic method call based on object type

6. Advanced OOP concepts:
    - property decorator

"""

#class definition
class Car:
    wheels = 4 # class attribute
    # method definition (__init__(self) is called the constructor method)
    def __init__(self, brand, model, year):
        """
        __init__: is the constructor method that initializes attribute.
        self: represents the instance of the class and allows access to attributes and methods.
        """
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        """
        display_info: is a method that returns a formatted string
        """
        return f"{self.year}-{self.brand}-{self.model}"
    

# trying to show encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number # public
        self._balance = balance # protected
        self.__pin = "1234" # private
        
    def deposit(self, amount):
        self._balance +=  amount
        
    def get_balance(self):
        return self._balance
    

# parent class
class Animal:
    def __init__(self, name):
        self.name =  name
        
    def make_sound(self):
        return "Some sound"
    
class Mammal:
    def has_hair(self):
        return True
    
# child class
class Dog(Animal):
    def make_sound(self):
        return "Bark!"
    
class Bird:
    def can_fly(self):
        return True

# multiple inheritance   
class Bat(Mammal, Bird):
    pass


class Cat(Animal):
    def __init__(self, color, name):
        self.color = color
        super().__init__(name)
    def make_sound(self):
        return "Meow!"



class Sparrow:
    def fly(self):
        return "Sparrow is flying"
    
class Airplane:
    def fly(self):
        return "Airplane is flying"
    
    
sparrow = Sparrow()
plane = Airplane()

# duck typing
def lift_off(entity):
    print(entity.fly())
    
# lift_off(sparrow)
# lift_off(plane)


#-----------------------------------------------
#Abstraction
#-----------------------------------------------
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# dog = Dog()
# print(dog.make_sound())

#------------------------------------
# advanced topics
#------------------------------------

# method decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius can not be negative")
        self._radius = value
        
# circle = Circle(5)

# print(circle.radius)
# circle.radius = 12
# print(circle.radius)

# magic methods
#__str__, __repr__

class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Person: {self.name}"
    
    def __repr__(self):
        return "Person('mario')"
        
        
p = Person("Mario")

print(p.__repr__())