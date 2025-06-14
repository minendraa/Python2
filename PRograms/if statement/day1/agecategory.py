age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 2:
    print("infant")
elif age <= 10:
    print("child")
elif age <= 17:
    print("teen")
elif age <= 55:
    print("adult")
else:
    print("hajurbuwa")
