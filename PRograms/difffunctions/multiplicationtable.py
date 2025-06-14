def getnumber():
    a=int(input("enter the number: "))
    return a
a=getnumber()
multiply=lambda a,i:a*i[(a, i, multiply(a, i)) for i in range(1, 11)]
for a, i, result in table:
    print(f"{a} x {i} = {result}")


