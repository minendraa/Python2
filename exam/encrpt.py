def getstr():
    i=input("enter string: ")
    return i
i=getstr()
def addspace(i):
    z='  '.join(i)
    return z
z=addspace(i)
def replace(z):
    v=z.replace('  ','xy')
    return v
print(i)
print(z)
result=replace(z)
print(result)


