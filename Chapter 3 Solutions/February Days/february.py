#This Program Determines if a year is a leap year or not

#Get Year 
year = int(input("Enter Year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
         print("Not a Leap Year")
if year % 100 != 0:
    if year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
