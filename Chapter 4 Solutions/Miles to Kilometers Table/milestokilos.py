#This Program Coverts Miles to Kilometers

#MIN and MAX Miles
MIN_MILES = 10
MAX_MILES = 80
INCREMENT = 10

#Ratio
MILES_TO_KILOMETER_RATIO = 1.60934

print("Miles\t\tKilometers")
print("----------------------------")

for i in range(0, MAX_MILES + 1, INCREMENT):
    kilometer = MILES_TO_KILOMETER_RATIO * i
    if i > 0:
        print(f"{i}\t\t{kilometer:.2f}")