#This Program calulates Automobile Costs Using Function

#Monthly Cost Function Definition
def monthly_costs(loan, insurance, gas, oil, tire, maintenance):
    total = loan + insurance + gas + oil, + tire + maintenance
    return total

#Annual Costs
def annual_cost(monthly_cost):
    return monthly_cost * 12
    
#main function definition
def main():
    
    #Get loan payment, insurance, gas, oil, tires, and maintenance cost per monthly
    loan_payment = float(input("Loan Payment: "))
    
    insurance_costs = float(input("Insurance Cost: "))
    
    gas_costs = float(input("Gas Cost:"))
    
    oil_costs = float(input("Oil Costs: "))
    
    tire_cost = float(input("Tire Costs: "))
    
    maintenance_cost = float(input("Maintenance costs:"))
    
    #Get total monthly cost
    total_monthly_cost = monthly_costs(loan_payment, insurance_costs, gas_costs, oil_costs, tire_cost,maintenance_cost)
    
    #Get Annual Costs
    annual_costs = annual_cost(total_monthly_cost)
    
    #Display Results
    print("Monthly Costs: $" + str(total_monthly_cost))
    print("Annual Cost: $" + str(annual_costs))
    
#main function call
main()