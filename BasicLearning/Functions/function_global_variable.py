# https://python.swaroopch.com/functions.html

foo_variable = 45


def foo_fun():
    global foo_variable
    print('Value of foo_variable is', foo_variable)
    foo_variable = 23  # Now it will change global scope variable value
    print('Changed global foo_variable to ', foo_variable)


foo_fun()
print('Function Called')
print('Now Value of foo_variable is', foo_variable)
