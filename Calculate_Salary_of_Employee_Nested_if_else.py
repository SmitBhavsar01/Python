#calculate the salary of an employee based 
# on following conditions (nested if-else): 
# 1. If degree=B.E.and experience<5years,salary=30000 
# 2.If degree=B.E.and experience>=5years,salary=40000 
# 3.If degree=M.E.and experience<5years,salary=50000 
# 4.If degree=M.E.and experience>=5years,salary=60000 

degree=str(input("Enter the Degree of Employee (B.E OR M.E): "))
experience=float(input("Enter the experience of employee in years : "))

if degree=="B.E" and experience<5:
    print("Salary : 30000")
elif degree=="B.E" and experience>=5:
    print("Salary : 40000")
elif degree=="M.E" and experience<5:
    print("Salary : 50000")
elif degree=="M.E" and experience>=5:
    print("Salary : 60000")
else:
    print("Please Enter Valid Info")