s=int(input("Students? "))
g=int(input("groups? "))

total=s//g
l=s%g
if l==1:
    print(f"groups={total}left over={l}")
else:
    print(f"groups={total}left over={l}")


