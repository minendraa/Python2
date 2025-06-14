def gettemp():
    temperature=[]
    while True:
        temp=(input("enter the temperatures: "))
        if temp=='':
            break
        temperature.append(float(temp))

    maximum=max(temperature)
    minimum=min(temperature)
    avg=sum(temperature)/len(temperature)
    print(f"maximum={maximum}\nminimum={minimum}\naverage={avg}")

gettemp()


       
    
   