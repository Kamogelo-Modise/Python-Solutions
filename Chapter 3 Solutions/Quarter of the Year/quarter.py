#This Program tells which quarter does a month belong

#Get Month
month = int("Month: ")

#Checks Quarter
if month >= 1 and month <= 3:
    print("First Quarter")
elif month > 3 and month < 6:
    print("Second Quarter")
elif month >= 7 and month <= 9:
    print("Third Quarter")
elif month >= 10 and month <= 12:
    print("Forth Quarter")
else:
    print("Invalid Month")