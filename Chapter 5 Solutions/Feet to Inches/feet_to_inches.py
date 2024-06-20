#This program converts feet to inches using functions

#get feet function definition
def get_feet():
    feet = int(input("Number of Feet:"))
    return feet

#feet_to_inches function definition
def feet_to_inches(n):
    inches = n * 12
    return inches

#main function definition
def main():
    #get number of feet
    feet = get_feet()
    
    #covert feet to inches
    inches = feet_to_inches(feet)
    
    #Display Results
    print(f"{feet} feet is {inches} inches")
    
#main function call
main()