#This Program Calculates the grade of a student
#And Determines if they passed or not

#Get marks for test1, test2 and exam
test1 = int(input("Test 1: "))

test2 = int(input("Test 2: "))

exam = int(input("Exam: "))

#Totals
tests_total = test1 + test2

total = exam + tests_total

#Checking input Validation
if (test1 < 0 and test1 > 25) or (test2 < 0 and test2 > 25) or (exam < 0 and exam > 50):
    print("Invalid Score(s) tests should be 0-25 and exam 0-50")
elif total >= 50 and exam >= 25:
    if total >= 80:
        print("Distinction")
    elif total < 80 and total >= 60:
        print("Credit")
    elif total >= 50 and total <= 59:
        print("Pass")
else:
    print("Fail")