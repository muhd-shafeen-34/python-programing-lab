#Display pyramid with number accepted from user

j = int(input("enter the number: "))

def pyramid(j):
    for i in range(1,j+1):
        for n in range(1,i+1):
            print(n*i,end=" ")
        print("\n")
pyramid(j)



    
