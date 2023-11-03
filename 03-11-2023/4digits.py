lists = []
def squares(a,b):
    #traverse through all numbers
    for i in range(a,b+1):
        j=1
        while j*j <= i:
            if j*j == i:
                lists.append(str(i))
            j = j + 1
        i = i+1
    return lists
print("perferct square list\n",squares(1000,9999))

lus=[]
{"for i in lists:
    count = 0
    for j in i:
        if int(j) % 2 == 0:
            count = count+1
        else:
            break
    if count == 4:
        lus.append(int(i)) 
print("even list is\n",lus)
             
