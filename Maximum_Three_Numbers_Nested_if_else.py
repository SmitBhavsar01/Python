#maximum of three numbers(nested if-else)

x=int(input("Enter a Number x : "))
y=int(input("Enter a Number y : "))
z=int(input("Enter a Number z : "))

if x>y and x>z:
    print(f"{x} means x is the maximun number")
elif y>x and y>z:
    print(f"{y} means y is the maximun number")
else:
    print(f"{z} means z is the maximun number")


