x=[]
n=int(input("enter the size: "))
for i in range(0,n):
      ele = int(input("enter integers "))
      if ele > 100:
          x.append("over limit")
      else:
          x.append(ele)
print(x)
        
