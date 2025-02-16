# A class is a blueprint for creating objects, and an object is an instance of a class.
class Person:
    
    # constructor method  
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old..")


      

# #creating an object       
p1 = Person(name="Mario", age=26)
# print(p1.name)
# print(p1.age)
p1.greet()
# # print("--------------------------------------")
# p2 = Person("Franka", 25)
# print(p2.name)
# print(p2.age)
# p2.greet()

class Car:
    wheels = 4 # all cars have 4 wheel 
    
    def __init__(self, brand):
        self.brand = brand
        
car1 = Car("Toyota")

print(car1.brand)


car2 = Car("Honda")
car2.wheels = 6
