def getnum():
    i=int(input("enter the number: "))
    return i
i=getnum()
def primecheck(i):
    x=0
    for z in range(i,0,-1):
        if i%z==0:
            x+=1
    if x==2:
        print("prime")
    else:
        print("not prime")
primecheck(i)