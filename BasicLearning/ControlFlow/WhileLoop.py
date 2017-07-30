# https://python.swaroopch.com/control_flow.html
# While loop Example
number = 35
running = True
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulation, You guess right number')
        running = False
    elif guess < number:
        print('No, it is little higher than that')
    else:
        print('No it is little lower then that')

else:
    print('The while loop is over.')

print('While Loop done')
