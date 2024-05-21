#This Program Calculates the Distance Traveled by a Vehicle

#Get Speed and time traveled

speed = float(input("Speed: "))

#input validation
while speed < 0:
    speed = float(input("Invalid value.Enter Speed: "))
    
time_traveled = int(input("Time in (hours):"))
#input validation
while time_traveled < 0:
    time_traveled = int(input("Invalid Value.Enter Time: "))

#Total Distance
total_distance = 0.0

#Displaying Results
print("Hours\t\tDistance Traveled")
print("------------------------")

for i in range(1, time_traveled + 1):
    distance = (speed * i)
    total_distance += distance
    print(f"{i}\t\t{distance}")