def getnum():
    num=int(input("enter the number: "))
    return num 
def factor(num):
    if num<0:
        print("error")
        return None
    else:
        factors=[]
        i=1
        while i<=num:
            if num%i==0:
                factors.append(i)
            i+=1
        return factors

num=getnum()
result=factor(num)
print(f"The factor of {num} is {result}")