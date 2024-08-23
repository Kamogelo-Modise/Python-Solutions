
#number of months
MONTH_NUM = 12


#get total rainfall functon definition
def get_total(num_list):
    sum = 0
    for n in num_list:
       sum += n
    return sum

#get average rainfall function definition
def get_average(sum):
     return sum / MONTH_NUM
 
def main():
    
    #rainfall for 12 months list
    rainfall_list = [] * MONTH_NUM
    
    print("Rainfall for 12 months")
    
    for month in range(MONTH_NUM):
        #get rainfall for each month
        print(f"Enter rainfall for month {month + 1}: ", sep="", end="")
        rainfall = float(input())
        
        #add to the railfall list
        rainfall_list.append(rainfall)
     
    #total rainfall
    total = get_total(rainfall_list)
    
    #Average Rainfall
    average_rainfall = get_average(total)
    
    #highest and lowest rainfall
    highest_rainfall = max(rainfall_list)

    lowest_rainfall = min(rainfall_list)
    
    #Display Results
    print(f"Total Rainfall:{total}, Average Rainfall: {average_rainfall}")
    
main()