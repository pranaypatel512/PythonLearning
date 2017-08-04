def print_values(val1, val2=4, val3=10):
    print("Val 1 is", val1, "\nVal 2 is", val2, "\nVal 3 is", val3)


print_values(10, 11, 54)
print("------------")
print_values(10, val3=24)
print("------------")
print_values(val2=24, val1=11)
