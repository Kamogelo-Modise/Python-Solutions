#This program reads numbers form a file then adds them up

#main function definition
def main():
    #total
    total = 0
    
    #opening a file then processing from it
    with open("numbers.txt", "r") as file:
        #read number from the file
        for line in file:
            #accumulating the numbers
            total += int(line)
        #display the sum
        print(f"Total: {total}") 
#main function call
main()