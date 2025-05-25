"""This is a library of a basic calculator"""

import math

def add(*args):
    """Returns the sum of the parameters"""
    sum = 0
    for arg in args:
        sum += arg
    return sum

def substract(*args):
    """Returns the difference of the parameters in order"""
    diff = args[0]
    for arg in args[1:]:
        diff -= arg
    return diff

def multiply(*args):
    """Returns the product of the parameters"""
    product = 1
    for arg in args:
        product *= arg
    return product

def divide(a, b):
    """Returns the quotient when 1st num is divided by the 2nd num"""
    return a / b

def modulus(a, b):
    """Returns the remainder"""
    return a % b

def power(a,b):
    """Returns a^b"""
    return a ** b

def sqrt(x):
    """Returns square root of the num"""
    return math.sqrt(x)

def f_division(a, b):
    """Returns GIF of the quotient"""
    return math.floor(a / b)

def log(x, base):
    """Returns log of x with base in the order of parameters (x, base)"""
    return math.log(x, base)

def sine(x):
    """Returns sin(angle) where angle in parameter should be in degrees"""
    return math.sin(math.radians(x))

def cosine(x):
    """Returns cos(angle) where angle in parameter should be in degrees"""
    return math.cos(math.radians(x))

def tangent(x):
    """Returns tan(angle) where angle in parameter should be in degrees"""
    return math.tan(math.radians(x))

def fact(x):
    """Returns factorial of a num"""
    if x == 0:
        return 1
    return x * fact(x-1)

def absolute(x):
    return abs(x)

def inverse(x): 
    try:
        return 1 / x
    except ZeroDivisionError:
        return "UNDEFINED"
    
def percentage(part, whole):
    """Returns percent of part as a whole"""
    return (part / whole) * 100
