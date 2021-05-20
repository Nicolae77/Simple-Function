def add(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 + n2


def divide(n1, n2):
    return n1 + n2


def calculator(n1, n2, func):
    return func(n1, n2)


add_result = calculator(2, 3, add)
subtraction_result = calculator(5, 3, add)
multiply_result = calculator(4, 3, add)
divide_result = calculator(6, 3, add)
print(add_result)
print(subtraction_result)
print(multiply_result)
print(divide_result)
