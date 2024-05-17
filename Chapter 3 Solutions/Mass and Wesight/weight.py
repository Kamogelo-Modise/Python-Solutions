#THis Program Calculates the weight of an object

#Get Object's mass
mass = float(input("Mass: "))

#Calculating Weight

weight = mass * 9.8

#Check if the object is heavy or light
if mass > 500:
    print("The Object is too heavy")
elif mass < 100:
    print("The Object is too light")