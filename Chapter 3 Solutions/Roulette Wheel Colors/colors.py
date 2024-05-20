#This Program Determines the color of a number on a roulette wheel

pocket_number = int(input("Enter Pocket Number: "))

if pocket_number < 0 or pocket_number > 36:
    print("Invalid Pocket Number")
elif pocket_number == 0:
    print("Green")
elif pocket_number >= 1 and pocket_number <= 10:
    if pocket_number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif pocket_number >= 11 and pocket_number <= 18:
    if pocket_number % 2 == 0:
        print("Red")
    else:
        print("Black")
elif pocket_number >= 19 and pocket_number <= 28:
    if pocket_number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number % 2 == 0:
        print("Red")
    else:
        print("Black")