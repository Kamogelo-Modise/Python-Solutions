#This Program calculates sales tax using functions
#main function definition

#Define get_total_sales function
def get_total_sales():
    sales = float(input("Total Sales: "))
    return sales
    
#Define county_sales_tax function
def county_sales_tax(sales):
    county_tax = sales * 0.025
    return county_tax

#Define state_sales_tax function
def state_sales_tax(sales):
    state_tax = sales * 0.05
    return state_tax

#Define Total sales tax
def total_sales_tax(county_tax, state_tax):
    total_tax = county_tax + state_tax
    return total_tax

def main():
    #Get total Sales For the month
    total_month_sales = get_total_sales()
    
    #Get county sales tax
    county_tax = county_sales_tax(total_month_sales)
    
    #Get state sales tax
    state_tax = state_sales_tax(total_month_sales)
    
    #Get total sales tax
    total_tax = total_sales_tax(county_tax, state_tax)
    
    #Display Results
    print(f"County Sales tax: {county_tax}")
    print(f"State Sales Tax: {state_tax}")
    print(f"Total Sales Tax: {total_tax}")
    
#main function call
main()