#This Program Calculates the Area and The Circumference of a Circle

#Get the radius
radius = float(input("Radius: "))

#Pi Constant
pi = 0.14159

#Area of a Circle
area = radius * pi**2

#Circumference of a Circle
circumference = 2 * pi * radius

#Display Results
print("Area: ", area)
print("Circumference: ", circumference)