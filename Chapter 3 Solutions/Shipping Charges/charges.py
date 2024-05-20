#This Program Calculates Shipping Charges

#Get Weight
weight = float(input("Enter Weight: "))

if weight >= 0 and weight <= 2:
    charges = weight * 1.25
    print("Charges: $" + str(charges))
elif weight > 2 and weight <= 6:
    charges = weight * 3.00
    print("Charges: $" + str(charges))
elif weight > 6 and weight <= 10:
    charges = weight * 4.00
    print("Charges: $" + str(charges))
elif weight > 10:
    charges = weight * 4.75
    print("Charges: $" + str(charges))
else:
    print("Invalid Weight")
