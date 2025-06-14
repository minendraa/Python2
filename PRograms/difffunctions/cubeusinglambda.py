def getnumber():
    a=int(input("enter the number: "))
    return a 
a=getnumber()
cube=lambda a:a*a*a
result=cube(a)
print(f"{result}")