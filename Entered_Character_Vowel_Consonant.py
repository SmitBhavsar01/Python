#check whether entered 
# character is vowel or consonant. 

a=input("Enter a Character : ")
if len(a) != 1 or not a.isalpha():
    print("Please enter a single alphabet character.")
else:
    vowel= ("a","e","i","o","u","A","E","I","O","U")

    if  a in vowel:
        print(f"{a} is Vowel")
    else:
        print(f"{a} is Consonant")