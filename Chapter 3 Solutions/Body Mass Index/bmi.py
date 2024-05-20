#This Program Calculates the Body Mass Index of an Individual

#Get Weight and Height
weight = float(input("Enter Weight: "))
height = float(input("Enter Height: "))

#Claculate Body Mass Index

bmi = (weight * 703) /(height ** 2)

if bmi >= 18.5 and bmi <= 25:
    print("Optimal Weight")
elif bmi < 18.5:
    print("Underweight")
elif bmi > 25:
    print("Overweight")