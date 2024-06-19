#This program uses functions to calulate repalcement cost

#Get Cost Function
def get_cost():
    c = float(input("Home or Building Cost:"))
    return c
#Replacement Cost
def replacement_cost(c):
    insured_amount = c * 0.80
    return insured_amount

#Main function Definition
def main():
    #Get Structure Cost
    amount = get_cost()
    
    #Replacement Cost
    insurance_cost = replacement_cost(amount)
    
    #Print Results
    print(f"Replacement Cost: ${insurance_cost}")
    
#main function call
main()