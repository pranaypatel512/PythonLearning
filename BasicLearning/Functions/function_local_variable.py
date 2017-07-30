# https://python.swaroopch.com/functions.html

foo_variable = 45


def foo_fun(foo_variable):
    print('Value of fooVariable is', foo_variable)
    foo_variable = 23  # it will change only local scope variable value
    print('Change Local foo_variable to ', foo_variable)


foo_fun(foo_variable)
print('Function Called')
print('Value of fooVariable is', foo_variable)
