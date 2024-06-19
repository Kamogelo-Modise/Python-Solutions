#This Program uses functions to convert
#Kilometer to Miles

#Get distance function
def get_distance():
    d = float(input("Enter Distance in Kilometers: "))
    return d

#Convert Kilometers to Miles Function
def kilometers_to_miles(d):
    m = d * 0.6214
    return m

#main function Definition
def main():
    
    #Get Distance Input
    distance = get_distance()
    
    #Get Miles
    miles = kilometers_to_miles(distance)
    
    #Display Results
    print(f"{distance} km is {miles} miles")

main()
  
