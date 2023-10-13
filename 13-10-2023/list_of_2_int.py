i=-1
a=[]
b=[]
while(i == -1):
    z=int(input("enter number of list1:\n"))
    if z == 0:
        break
    else:
        a.append(z)
while i == -1:
    c=int(input("enter number of list2"))
    if c == 0:
         break
    else:
         b.append(c)
if len(a)==len(b):
    print("list are sanme length\n",len(a))
else:
    print("\nlist are not same length\n")
    
if sum(a)==sum(b):
    print("list have the same sum\n",sum(a))
else:
    print("\nnot same sum")
for n in a:
    for d in b:
        if n==d:
            print("\n",n,"is both list1 in position",a.index(n),"and list 2")
    
    
    
