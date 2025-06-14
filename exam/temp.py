def take():
    i=int(input("enter num: "))
    return i
def check(i):
    factors=[]
    for x in range(1,i+1):
        if i%x==0:
            factors.append(x)
        else:
            continue
    print(factors)
i=take()
check(i)
 