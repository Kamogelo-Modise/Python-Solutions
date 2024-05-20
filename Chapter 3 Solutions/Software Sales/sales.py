#This Program calculates Discount For a Software Company

#Packages Purchases
packages_purchased = int(input("Enter Number of Packages Purchased: "))

#Retail Price
retail_price = 99.00

#Claculating Discount and Displaying Results

if packages_purchased >= 0 and packages_purchased < 10:
    print("No Discount")
elif 10 <= packages_purchased < 20:
    discount = (retail_price * 0.10) * packages_purchased
    total_amount = retail_price * packages_purchased - discount
    print("Discount: $" + discount)
    print("Total Amount: $" + total_amount)
elif 20 <= packages_purchased < 50:
    discount = (retail_price * 0.20) * packages_purchased
    total_amount = retail_price * packages_purchased - discount
    print("Discount: $" + discount)
    print("Total Amount: $" + total_amount)
elif 50 <= packages_purchased < 100:
    discount = (retail_price * 0.30) * packages_purchased
    total_amount = retail_price * packages_purchased - discount
    print("Discount: $" + discount)
    print("Total Amount: $" + total_amount)
elif packages_purchased >= 100:
    discount = (retail_price * 0.40) * packages_purchased
    total_amount = retail_price * packages_purchased - discount
    print("Discount: $" + discount)
    print("Total Amount: $" + total_amount)