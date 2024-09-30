# functions.py

def greet(name):
    return f"Hello, {name}!"

def calculate_area(length, width):
    return length * width

def is_even(number):
    return number % 2 == 0

def get_initials(full_name):
    parts = full_name.split()
    initials = ''.join([part[0].upper() for part in parts])
    return initials
