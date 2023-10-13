n = input("enter a string which has repeated letters")
n.upper()
print("orginal string is: ",n)
k='$'
res= n[0]+n[1:].replace(n[0],k)
print(res)
