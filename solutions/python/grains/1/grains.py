def square(number):
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    squared = 2 ** (number - 1)
    return squared
def total():

    return (2**64)-1
