#program to find factorial of a number using function

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter number to find fact: "))
print("the factorial of "+str(n)+" is ",factorial(n)) 
