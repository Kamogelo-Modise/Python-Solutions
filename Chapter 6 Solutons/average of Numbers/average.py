#this program calculates the average of numbers read fron a file

#main function definition
def main():
    
    #total sum
    total = 0
    
    #average 
    average = 0
    
    #number of total numbers
    count = 0
    
    #open file for processing
    with open("numbers.txt") as file:
        for line in file:
            #read number
            number = int(line.rstrip())
            #update total
            total += number
            #update number count
            count += 1
        
        #Calculate average
        average = total / count
        #display average 
        print(f"Average: {average: .2f}")
        
#main function definition
main()