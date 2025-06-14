import math
def get_nums():
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    return a,b 
def addition(a,b):
    return a+b 
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def sqareroot(a):
    return math.sqrt(a)
def calculations(a,b):
    print("enter the operation you would like to perform.")
    print("enter \n1 for add \n 2 for subs \n 3 for multiply \n 4 for division\n 5 for square root ")
    choice=input("1/2/3/4/5: ")
    if choice=="1":
        return addition(a,b)
    elif choice=="2":
        return substraction(a,b)
    elif choice=="3":
        return multiplication(a,b)
    elif choice=="4":
        return division(a,b)
    elif choice=="1":
        return sqareroot(a)
    else: 
        "Inavlid number provided.."
def printresult(result):
    print(f"result = {result}")

a,b=get_nums()
result=calculations(a,b)
printresult(result)

