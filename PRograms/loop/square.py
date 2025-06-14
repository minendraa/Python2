num=int(input("enter the number: "))
a=1
b=0
while a<=num:
    c=a**2
    print(f"{c}")
    b+=c
    a+=1
print(f"the sum is {b}")