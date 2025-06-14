def taking():
    a=input("enter the word: ")
    return a 
def check(a):
    if len(a)>1:
        return a[:-1]
    else:
        return a
a=taking()
result=check(a)
print(result)
