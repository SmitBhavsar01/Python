# find roots of quadratic equations
# if roots are real

import math

a=float(input("Enter Coefficient of a :"))
b=float(input("Enter Coefficient of b :"))
c=float(input("Enter Coefficient of c :"))

discriminanat = float((b**2) - (4*(a*c)))

if discriminanat >0:
    
    print("discriminanat is Greater Than Zero(0) So")
    root1= (-b + math.sqrt(discriminanat)) /(2*a)
    root2= (-b - math.sqrt(discriminanat)) /(2*a)
    print(f"The equation has two distinct real roots: {root1} and {root2}")
    
elif discriminanat == 0:
    
    print("discriminanat is Zero(0) so")
    root=(-b)/(2*a)
    print(f"The equation has one real root: {root}")

else:
    
    print("discriminanat is Less Than Zero(0)")
    print("Complex roots")