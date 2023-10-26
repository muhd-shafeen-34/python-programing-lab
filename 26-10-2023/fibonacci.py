#generate fibonacci of n terms

n = int(input("enter the N term"))
n1,n2 = 0,1
count = 0
if n<=0:
    print("enter a positive integer")
elif n==1:
    print("fibonacci series ", n2)
else:
    print("fibinacci sequesnce: ")
    while count<n:
        print(n1)
        n3=n1+n2
        n1 = n2
        n2 = n3
        count = count+1
