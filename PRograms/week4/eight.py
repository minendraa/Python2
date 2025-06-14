"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""
def check():
    temperatures=[]
    while True:
        temp=(input("enter the temperatures: "))
        if temp =='':
            break
        temperatures.append(float(temp))

    max_temp=max(temperatures)
    min_temp=min(temperatures)
    mean_temp=sum(temperatures)/len(temperatures)
    print(f"maximum temperature is {max_temp}C")
    print(f"minimum temperature is {min_temp}C")
    print(f"mean of all temperatures is {mean_temp}C")
check()
