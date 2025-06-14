import math
while True:
    def get_numbers():
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
    def squareroot(a):
        return math.sqrt(a)
    def calculation(a,b):
        print("What operation would you like to perform?")
        print("Enter \n 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division \n 5 for squareroot")
        choice=input("enter your choice: 1/2/3/4/5 \n: ")
        if choice=="1":
            return  addition(a,b)
        elif choice=="2":
            return  substraction(a,b)
        elif choice=="3":
            return  multiplication(a,b)
        elif choice=="4":
            return  division(a,b)
        elif choice=="5":
            return squareroot(a)
        else:
            return("invalid number given.")
    def printresult(result):
        print(f"result is {result}")
        
    a,b = get_numbers()
    result = calculation (a,b)
    printresult(result)