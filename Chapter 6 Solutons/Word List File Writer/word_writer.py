#This program writes a list of words to a file

#get_num_words definition
def get_num_words():
    n = int(input("enter Number of Words: "))
    return n

#main function definition
def main():
    #get the number of words
    num_words = get_num_words()
    
    #open file for writing words
    with open("words.txt", "w") as file:
        for i in range(num_words):
            word = input(f"Word {i + 1}:")
            file.write(word + "\n")
            
#main function call
main() 