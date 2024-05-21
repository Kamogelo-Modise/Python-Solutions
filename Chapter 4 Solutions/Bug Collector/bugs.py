#This Program Calculates the Number of bugs Collected in 5 Days

#Maximum Days
MAX_DAY = 5

#Total Number of Bugs
total_bugs = 0

#Bugs Collected
for i in range(1, MAX_DAY + 1):
    num_bugs = int(input(f"Bugs Collected in day {i}: "))
    while num_bugs < 0:
        print("Invalid Input")
        num_bugs = int(input(f"Bugs Collected in day {i}: "))
    total_bugs += num_bugs

#Display Results
print(f"Total Bugs Collected is {total_bugs}")