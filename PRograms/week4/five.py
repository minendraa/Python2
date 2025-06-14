"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""
def gettemp():
    c=int(input("enter the temprature in celsius: "))
    f=int(input("enter the temprature in fahrenheit: "))
    return c,f
def celsiustofahrenheit(c):
    f=(c * 9/5) + 32
    return f

def fahrenheittocelsius(f):
    c=(f - 32) * 5/9
    return c

c,f=gettemp()
result=celsiustofahrenheit(c)
result2=fahrenheittocelsius(f)
print(f"Temp in {c} degree C is equivalent to {result} degree F")
print(f"Temp in {f} degree F is equivalent to {result2} degree C")

