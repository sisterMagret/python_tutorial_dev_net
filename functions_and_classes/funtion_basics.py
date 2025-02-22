
#print, eval, range

# function definition
def greet():
    print("Hello welcome to python")

# function call    
# greet()

# function definition with parameters/arguments and a return value
def add(a, b):
    return a + b

# total = add(4,5)

#positional arguments
def subtract(a, b):
    result = a - b
    return result  

diff = subtract(5,10)

# print(diff)

# default args
def greet(name="Mario"):
    print(f"Hello {name}")

# greet(name="Franka")


# def keyword args
def get_full_name(first_name, last_name):
    print(f"{first_name} {last_name}")
    
# get_full_name(last_name="Mario", first_name="Bowser")

def sum_all(*args):
    result = sum(args)
    return result

# total = sum_all(2,3,4,455,2,)
# print(total)

def person_info(*args, **kwarg):
    for key, value in kwarg.items():
        print(f"{key}: {value}")
    print(args[0])
    
# person_info(26,name="Mario", age=27, gender="male")   

# lambda functions or anonymous functions
square = lambda x: x**2

# print(square(7))

add = lambda x, y, i: x + y + i
# print(add(3,5, 1))

# higher order functions:  functions that can take other functions as arg or return a function
def apply_function(func, value):
    return func(value)

# print(apply_function(square, 2))
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)

# print(double(5))

#closures 
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

closure_func = outer_func("Hello word form closure")
# closure_func()


# decorator functions: they allow you to modify the behavior of functions
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


@decorator
def say_hello():
    print("Hello world!")