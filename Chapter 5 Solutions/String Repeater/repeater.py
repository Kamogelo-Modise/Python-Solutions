#This Program repeats strings by multiplying them with
#an integer using functions

#Repeat function
def repeat(s, n):
    repeated_str = s * n
    return repeated_str

#main Funtions Definition
def main():
    #String and Integer Inputs
    string = input("String: ")
    
    number = int(input("Integer: "))
    
    #Returned String assigned to variable
    repeated_string = repeat(string, number)
    
    #Print Results
    print(f"Reepated String: {repeated_string}")
    
#main function call
main()