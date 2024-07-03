#This Program Displays file content

#main function definition
def main():
    #Enter file name
    file_name = input("File Name: ")
    
    #open file for processing
    with open(file_name,"r") as file:
        #read line from the file
        line = file.readline().rstrip()
        #number of line(s)
        counter = 1
        
        #read the contents of the file
        while line != "" and counter <= 5:
            print(f"{line}")
            line = file.readline().rstrip()
            counter += 1
            
main()