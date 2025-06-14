def get_numbers():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    return a,b
def calculate_sum(a,b):
    return a+b 
def print_sum(result):
    print(f"the sum is {result}.")

a,b = get_numbers()

result=calculate_sum(a,b)

print_sum(result)



