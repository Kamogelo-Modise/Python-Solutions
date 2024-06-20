#This Program calculates the amount of a calories consumed a day
#Grams Input Function Definition
def get_grams():
    grams = float(input("Enter grams: "))
    return grams

#Fat Calories Function Definition
def get_fat_calories(n):
    carlories = 9 * n
    return carlories

#Carbohydrates Function Definition
def get_carbo_calories(n):
    calories = n * 4
    return calories

#main function definition
def main():
    #Get fat and carbohydartes grams
    fat_grams = get_grams()
    
    carbo_grams = get_grams()
    
    #Get fat and carbohydrates calories
    fat_calories = get_fat_calories(fat_grams)
    
    carbo_calories = get_carbo_calories(carbo_grams)
    
#main function call
main()