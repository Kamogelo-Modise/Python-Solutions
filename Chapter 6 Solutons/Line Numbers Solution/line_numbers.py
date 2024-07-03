#This program displays the contents of the file

#main function definition
def main():
    #get file name
    file_name = input("Enter File Name: ")
    
    #open file for processing
    with open(file_name, "r") as file:
        #read first line in file
        line = file.readline().rstrip()
        
        #line number
        counter = 1
        #read the remaining lines
        while line != "":
            #display line
            print(f"{counter}:{line}")
            #read next line
            line = file.readline().rstrip()
            #increment line number
            counter += 1
            
#call main function
main()