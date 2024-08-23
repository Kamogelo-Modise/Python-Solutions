import random
#maximum lottery numbers
MAX_NUMS = 7

#generate lottery numbers function definition
def get_numbers():
    #list of lottery numbers
    lottery_numbers = [] * MAX_NUMS
    
    #counter
    counter = 0
    
    #generating lottery numbers list
    while counter < MAX_NUMS:
        lottery_numbers.append(random.randint(0, 9))
        counter += 1
        
    return lottery_numbers
def main():
    #list of numbers
    lottery_numbers = get_numbers()
    
    #Display lottery numbers
    for n in lottery_numbers:
       print(f"{n},",end="")
       
main() 
    