import numbers


def return_value():
    return 100

print(return_value())

"""
def return_value1():
    print("This is a function")

print(return_value1())

"""

def return_integer() -> int:
    print("This is a function")

print(return_integer())


def cube(num) -> int:
    return num * num * num

print(cube(10))


def addition(num1: numbers, num2: numbers, num3: numbers = 0, num4: numbers = 0) -> numbers:
    return num1 + num2 + num3

print(addition(1, 2.5))
print(addition(1, 2.5, 300))
print(addition(1, 2.5, 300, 400))






