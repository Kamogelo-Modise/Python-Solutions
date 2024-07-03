#This Program Displays file content

#main function definition
def main():
    #Enter file name
    file_name = input("File Name: ")
    
    #open file for processing
    with open(file_name,"r") as file:
        line = file.readline().rstrip()
        counter = 1
        
        while line != "" and counter <= 5:
            print(f"{line}")
            line = file.readline().rstrip()
            counter += 1
            
main()