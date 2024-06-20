#This Program determines the greatest between 2 numbers using function
#get input
def get_num():
    n = int(input("Enter number: "))
    return n

#max function definition
def max(n, m):
    if n > m:
        return n
    elif n < m:
        return m
    else:
        return 0
    
#main function definition
def main():
    #get integer
    num1 = get_num()
    
    #get integer
    num2 = get_num()
    
    #maximun integer 
    max_num = max(num1, num2)
    
    #Display Results
    print(f"Maximum integer is {max_num}")
    
#main function calls
main()
    