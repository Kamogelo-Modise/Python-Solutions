#This program read numbers for a text file
 
#Main function definition
def main():
    
    with open("numbers.txt", "r") as file:
        #Read each number from the text file
        for line in file:
            #Display numbers from the file
            print(int(line.rstrip()))
            
#main function call
main()