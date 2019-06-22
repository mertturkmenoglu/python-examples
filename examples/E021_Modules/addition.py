def add(*numbers):
    """Add all numbers and return the sum"""
    result = 0
    for number in numbers:
        result += number
    return result