names=["ram","anish","krish","hari"]
name=input("enter name: ")
for n in names:
    if n == name:
        print("found",name)
        break  
else:
    print("did not find",name)