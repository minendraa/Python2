num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

largest = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num1 and num2 > num3 else num3 if num3>num1 and num3>num2 else "equal" if num1==num2==num3 else "they are equal"
print(f"The largest number is: {largest}") 
