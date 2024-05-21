#This Program Calculates the amount of Calories
#Burnt in 30 minutes

#Calories Burnt Per Minute
CALORIES_PER_MIN = 4.2

#Max Duration
MAX_DURATION = 30

#Total calories burnt
total_calories = 0

#Calculating Calories Burned
for i in range(1, MAX_DURATION + 1):
    if i >= 10 and i % 5 == 0:
        total_calories += i * CALORIES_PER_MIN
        print(f"Calories Burned in {i} minutes is {total_calories} joules.")