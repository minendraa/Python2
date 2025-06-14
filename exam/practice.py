print("set password")
while True:
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

    pass1=input("enter password:")

    if pass1 in BAD_PASSWORDS:
        print("error common password")
    else: 
        if(8<=len(pass1)<=12):
            pass2=input("enter password:")
            if pass1!=pass2:
                print("error")
            else:
                print("password set")
                break
        else:
            print("error password must be between 8 to 12 chars")
