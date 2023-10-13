#to generate & print a dictionary that contain a element b/w 1 and n (x , x*x)

n= int(input("enter a number: "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
