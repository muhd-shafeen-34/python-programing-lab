a = int(input("enter a number"))
i = 1
if a>0:
    for n in range(1,a+1):
        i = n*i
    print(i)
else:
    print("wrong input")
