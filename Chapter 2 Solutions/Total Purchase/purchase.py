#This Program Takes the Price of 5 Items
#And Calculates the subtotal, sales tax and total

#Get Item Prices
item1 = float(input("Item 1 Price: "))

item2 = float(input("Item 2 Price: "))

item3 = float(input("Item 3 Price: "))

item4 = float(input("Item 4 price: "))

item5 = float(input("Item 5 Price: "))

#Subtotal

subtotal = item1 + item2 + item3 + item4 + item5

#Sales Tax

sales_tax = subtotal * 0.07

#Total
total = subtotal - sales_tax

#Dispaly Results
print("Subtotal: ", subtotal)
print("Sales Tax: ", sales_tax)
print("Total: ", total)
