#This Program calculates the total number of instalments

#Get Purchase Price 
purchase_amount = float(input("Purchase Amount: "))

#Get Desired Number of instalments
num_of_instalments = int(input("Number of Instalments: "))

#Calculate Total Purchase
total_purchase = purchase_amount + purchase_amount * 0.05

#Instalment Cost
instalment_cost = total_purchase / num_of_instalments

#Display Results
print("Total Amount of Purchase: ", total_purchase)
print("Instalment Cost: ", instalment_cost)