#This program reads words frkom a file 

#main function definition
def main():
    #list of words
    words = []
    
    #count number of words
    count = 0
    
    #open file to read words
    with open("words.txt", "r") as file:
        for line in file:
            words.append(line.rstrip())
            count += 1
            
    #longest word
    long_word = words[0]
    
    for word in words:
        if len(word) > len(long_word):
            long_word = word

    #print longest word
    print(f"Longest word: {long_word}")
    
    #number of words
    print(f"{count} words")

#main function call    
main()
            