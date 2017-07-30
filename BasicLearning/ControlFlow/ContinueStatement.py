# https://python.swaroopch.com/control_flow.html#
while True:
    string = input('Enter something:')
    if string == 'quit':
        break
    if len(string) < 3:
        print('Input is too small')
        continue
    print('Input is of sufficient length')
