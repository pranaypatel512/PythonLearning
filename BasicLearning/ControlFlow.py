# https://python.swaroopch.com/control_flow.html
# If statements example
number = 33

guess = int(input('Enter an integer:'))

if guess == number:
    # New Block start here
    print("Congratulation, you are right!")
elif guess < number:
    print('No, it is little higher than that')
else:
    print('No it is little lower then that')

print('If Done')
