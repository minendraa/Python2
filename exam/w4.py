def getstring():
    str=(input("enter word: "))
    return str
i=getstring()
def check(i):
    upper=0
    lower=0
    for char in i:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    return upper,lower
upper,lower=check(i)
print(f"the num of upper is {upper} and lower is {lower}")