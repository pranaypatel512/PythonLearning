def total(var1=5, *numbers, **phone_book):
    print("a", var1)

    # iterate through all the items in tuple
    for one_item in numbers:
        print('one item', one_item)

    # iterate through all the items in Dictionary
    for part_one, part_two in phone_book.items():
        print(part_one, part_two)


print(total(22, 2, 3, 4, 5, Pranay=10, Ritesh=85, Nihal=98))
