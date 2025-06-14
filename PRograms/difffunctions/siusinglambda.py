


def getinputs():
    p=float(input("enter the principle: "))
    t=float(input("enter the time: "))
    r=float(input("enter the rate: "))
    return p,t,r
p,t,r=getinputs()
si=lambda p,t,r:(p*t*r)/100 
result=si(p,t,r)
print(f{"the simple interest is {result}")