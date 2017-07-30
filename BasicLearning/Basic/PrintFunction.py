print('a', end='')
print('b')
# Output is:
# ab

# Or you can end with a space:
print('a', end=' ')
print('b', end=' ')
print('c')
# Output is:
# a b c


print("This is the first sentence. \
This is the second sentence.")

# Output is: single line output
# This is the first sentence. This is the second sentence.

# Raw Strings
print(R"Newlines are indicated by \n")  # OR print(r"Newlines are indicated by \n")

# format float
print('{0:.3f}'.format(1.0 / 3))

# Keyword based arguments
print('my name is {name}. I am {which_developer}'.format(name='pranay', which_developer='Android Developer'))
