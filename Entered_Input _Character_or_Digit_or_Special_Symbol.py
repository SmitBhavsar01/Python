#entered input is character,digit or 
#special symbol Using ladder if-else.

a=input("enter any thing: ")

if a.isalpha():
    print(f"{a} is Character")
elif a.isdigit():
    print(f"{a} is Digit")
else:
    print(f"{a} is Special Symbol")