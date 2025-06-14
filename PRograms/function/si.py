def get_numbers():
    p=float(input("enter principle: "))
    t=float(input("enter time: "))
    r=float(input("enter rate: "))
    return p,t,r
def calculate_si(p,t,r):
    return (p*t*r)/100
def print_si(result):
    print(f"the simple interest is {result}.")

p,t,r = get_numbers()

result=calculate_si(p,t,r)

print_si(result)



