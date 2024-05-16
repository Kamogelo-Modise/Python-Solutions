#This Program calculates the percentage of males and females in a Classroom

#Number of males and females
males = int(input("Number of Males: "))

females = int(input("Number of Females: "))

#Total Number of Males and Females
total = males + females

#Male and Females Percentages

male_percentage = (males / total) * 100

female_percentage = (females / total) * 100

#Display Results
print("Male Percentage: ", male_percentage)
print("Female Percentage: ", female_percentage)