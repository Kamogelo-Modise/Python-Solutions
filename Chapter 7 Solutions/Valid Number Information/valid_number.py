#This Program calculates the total and average of the list of numbers
#demonstrating list operations

#minimum valid number
MIN = 0

#maximum valid number
MAX = 100

#Generate valid numbers function definition
def get_valid_numbers(num_list):
    valid_numbers = []
    for n in num_list:
        if n >= MIN and n <= MAX:
            valid_numbers.append(n)
            
    return valid_numbers

#Get total of valid numbers function definition
def get_total(num_list):
    sum = 0
    for n in num_list:
        sum += n
    return sum

#Get average to the valid number function definition
def get_average(total, num_list):
    return total / len(num_list)

def main():
    
    #List of numbers
    numbers = [47, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    
    #Get valid numbers
    valid_numbers = get_valid_numbers(numbers)

    #get total of the valid numbers
    total = get_total(valid_numbers)

    #get average of the valid numbers
    average = get_average(total, valid_numbers)
    
    #Display the results
    print(f"Total: {total} and Average: {average:.2f}")
    
main()