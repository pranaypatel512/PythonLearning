# https://python.swaroopch.com/modules.html
import os
import sys

print('The Command Line Argument here:')
for i in sys.argv:
    print(i)


print('\n\n The PythonPath is', sys.path, '\n')

# It will print current file directory path
print(os.getcwd())


from math import sqrt
print("Square root of 8 is", sqrt(16))

# WARNING: In general, avoid using the from..import statement,
# use the import statement instead.
# This is because your program will avoid name clashes and will be more readable.
