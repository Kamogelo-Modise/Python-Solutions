#This program calculates the total cost of tickects in a Stadium
#Get Tickects Function Definitions
def get_classA_tics():
    tics = int(input("Number of Class A tickets:"))
    return tics

def get_classB_tics():
    tics = int(input("Number of Class B tickets:"))
    return tics
def get_classC_tics():
    tics = int(input("Number of Class C tickets:"))
    return tics
#Total Amount Function Definition
def total_amount(a, b, c):
    total = (a * 20) + (b * 15) + (c * 10)
    return total

#main function definition
def main():
    #Get tickects for Class A
    classA_tickets = get_classA_tics()
    
    #Get tickects for Class B
    classB_tickets = get_classB_tics()
    
    #Get tickects for Class C
    classC_tickets = get_classC_tics()
    
    #Get total amount of the tickets
    total_ticket_amount = total_amount(classA_tickets, classB_tickets, classC_tickets)
    
    #Print Results
    print("Total Amount of the Tickets is $" + str(total_ticket_amount))
    
#main function call
main()