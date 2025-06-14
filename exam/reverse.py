def getstring():
    i=input("Enter the string.")
    return i
i=getstring()
def obfuscation(i):
    z=i.replace('  ','')
    r=z[::-1]
    return r
result=obfuscation(i)
print(result)
