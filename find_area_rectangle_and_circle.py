#Python program to find area of a 
#rectangle and circle. 

import math 
l=int(input("Enter the length of rectangle :"))

w=int(input("Enter the width of rectangle :"))

r=int(input("Enter the radius of circle :"))

print("Area of rectangle :",l*w)
print("Area of circle :",math.pi*(r*r))