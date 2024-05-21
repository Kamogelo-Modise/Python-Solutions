#This Program Calulates the Average Rainfall

#Months
MONTHS = 12

#Get Number of Years
years = int(input("Years: "))

while years < 0:
    years = int(input("Invalid Value. Enter Years: "))

#Total rainfall
total_rainfall = 0.0

#Total months 
months = years * 12

for i in range(1, years + 1):
    for j in range(1, MONTHS + 1):
        rainfall = float(input(f"Rainfall for year {i} month {j}: "))
        while rainfall < 0:
            rainfall = float(input(f"Invalid Value.Enter Rainfall for year {i} month{j}:"))
        total_rainfall += rainfall
        
        
#Average Rainfall
average_rainfall = total_rainfall / months

#Display Results
print(f"Total Rainfall is {total_rainfall}")
print(f"Total Months: {months}")
print(f"Average Rainfall: {average_rainfall}")