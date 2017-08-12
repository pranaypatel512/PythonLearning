def print_max(x,y):
    """ Prints maximum of two numbers.

    Two values must be integers."""
    # Convert to int if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")


# call function
print_max(45, 54)
print(print_max.__doc__)
