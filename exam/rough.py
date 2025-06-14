def getstring():
    i=input("enter: ")
    return i
def check(i):
    upper=0
    lower=0
    for char in i:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower=+1
    return lower,upper
i=getstring()
upper,lower=check(i)
print(f"There are {upper} upercase letters and {lower}lowercase letters.")