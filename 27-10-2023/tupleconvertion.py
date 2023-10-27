#convert a tuple int oa list and add item

tup = (1,2,3,4)
print(tup)
lis = list(tup)
a = int(input("enter an item: "))
lis.append(a)
tup = tuple(lis)
print(tup)
    
