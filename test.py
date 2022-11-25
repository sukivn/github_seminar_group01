def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def calc(a, b, op):
    return op(a, b)

add(2, 3)
multiply(3, 5)
calc(6, 8, multiply)