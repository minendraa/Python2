BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
print("set password")
p1=(input("enter password between 8 to 12 chars: "))
while True:
    if p1 in BAD_PASSWORDS:
        print ("bad password")
    else:
        p2=(input("enter password again: "))
        if (8<len(p1)<=12):
            if p1==p2:
                print("password set")
            else:
                print("error")
        else:
            print("error")