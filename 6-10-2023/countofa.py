lst=["shafeen","ansar"]
count = 0
a = str(input("enter the letter to search: "))
for i in lst:
    for f in i:
        if (f == "a"):
            count= count+1
print("count of ",a," in ",lst," is ",count)
