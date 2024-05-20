#This Program calculates the number of points a person gets for reading a book

#Get Number of Books Purchased
num_books = int(input("Enter Number of Books Purchased This month: "))

#Checks Points OFr the Months
if num_books >= 0 and num_books <= 1:
    print("No Points")
elif num_books >= 2 and num_books < 4:
    print("5 Points")
elif num_books >= 4 and num_books < 6:
    print("15 Points")
elif num_books >= 6 and num_books < 8:
    print("30 Points")
elif num_books >= 8:
    print("60 Points")
else:
    print("Invalid Number of Books")