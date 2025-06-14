name_list=[]
for i in range(1,3):
    name=input("enter your name: ")
    name_list.append(name)
def make_path(*names):
    result = ""
    for name in names:
        result += name + "/"
    return result  

name = make_path(*name_list)
print(name)
