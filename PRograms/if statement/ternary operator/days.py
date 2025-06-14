day=int(input("Enter the day: "))
number=print("sunday") if day==1 else print("Monday") if day==2 else print("tuesday") if day==3 else print("wednesday") if day==4 else print("thursday") if day==5 else print("friday") if day==6 else print("saturday") if day==7 else print("no data for given number.")


num=int(input("enter the number: "))
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print(days[num-1]) if 0<num<8 else print("invalid")