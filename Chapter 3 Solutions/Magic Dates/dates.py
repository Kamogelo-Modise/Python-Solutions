#This Program Checks for Special Dates

#Get Month, Day and Year
month = int(input("Month: "))

day = int(input("Day: "))

year = int(input("Year: "))

#Checks if it's Magic Date
if (month * day) == year:
    print("It's a Magic Date")
else:
    print("It's not a Magic Date")