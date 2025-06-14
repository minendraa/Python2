r = float(input("Enter the rate: "))
p = float(input("Enter the principle: "))
t = float(input("Enter the time in months: "))
y = float(input("Enter the time in years: "))

s = (p*y+t/12*r)/100
print(f"The Simple interest calculated is {s}")