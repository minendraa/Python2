def numbers():
    a=int(input("enter the number: "))
    b=int(input("enter the number: "))
    return a,b
a,b=numbers()

subtract = lambda a,b:a-b
result=subtract(a,b)
print(f"{result}")


