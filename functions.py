# functions are block of code that perform a certain task. A function should not do more than a single task
def greet(name):
    return "Hello" + " " + name


# name = input("Enter your name: ")

# greet_person = greet(name)

# print(greet_person)

def add(num1, num2):
    print("num1 =", num1)
    print("num2 =", num2)
    return num1 +  num2

num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

total = add(num_one, num_two)
print(total)

