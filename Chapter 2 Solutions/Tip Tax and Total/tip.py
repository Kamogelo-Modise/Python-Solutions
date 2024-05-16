#This Program Calculates the Tip Tax and Total for a given Meal

#Get meal Price
meal_price = float(input("Meal Price: "))

#calculate Tip
tip = meal_price * 0.18

#Calculate Meal tax
tax = meal_price * 0.07

#Meal Total Price
total_price = meal_price + tip + tax

#Display Results
print("Total Meal Price is ", total_price)