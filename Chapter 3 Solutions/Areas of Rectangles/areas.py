#This Program calculates the areas of two rectangles and compares them

#Get length and width fo the first rectangle
length_rect1 = float(input("Rectangle 1 Length: "))

width_rect1 = float(input("Rectangle 1 Width: "))

#Calculating the Area of Rectangle 1
rect1_area = length_rect1 * width_rect1

#Get length and width of rectangle 2
length_rect2 = float(input("Rectangle 2 Length: "))

width_rect2 = float(input("Rectangle 2 Width: "))

#Area of Rectangle 2
rect2_area = length_rect2 * width_rect2

#Comparing Areas

if rect1_area > rect2_area:
    print("Rectangle 1 Area is greater than Ractangle 2 Area")
elif rect2_area > rect1_area:
    print("Rectangle 2 Area is greater than Rectangle 2 Area")
else:
    print("The two rectangles have the equal areas")