#This Program calculates the distance of a falling object using functions
#main function definition

#Max Time in Seconds and Gravitatonal Acceleration
MAX = 10
G = 9.8

#get_distance function definition
def get_distance(t):
    d = (1 / 2) * G * (t**2)
    return d

def main():
    
    print("Time (in secs)\tDistance (in m)")
    print("---------------------------------")
    #loop for time interals 
    for time in range(1, MAX + 1):
        #function call to get distance per 1 sec interval
        distance = get_distance(time)
        
        #Display Results
        print(f"{time}\t\t{distance:.2f}")
        
#main function call
main()