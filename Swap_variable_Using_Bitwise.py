#Python program to swap two 
# variables using bitwise operator

#using xor
a=5
b=4
a=a^b
b=a^b
a=a^b 
print(f"a is {a} b is {b}")