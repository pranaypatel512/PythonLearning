def maximum(var1, var2):
    if var1 > var2:
        return var1
    elif var1 == var2:
        return "Both numbers are equal"
    else:
        return var2

print(maximum(23, 23))
print(maximum(22, 23))

# TIP: There is a built-in function called max that already implements the
# 'find maximum' functionality, so use this built-in function whenever possible.
print(max(22, 34))
