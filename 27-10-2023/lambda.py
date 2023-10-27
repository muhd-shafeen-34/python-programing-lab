#lambda function to find the area of square rectangle & triangle

a = int(input("enter the side of the square \n"))
area = lambda b:b*b
print("area of square ",area(a))

a = int(input("enter the length of the rectangle \n"))
b = int(input("enter the breadth of the rectangle \n"))
area = lambda l,b:l*b
print("area of rectangle is ",area(a,b))

a = int(input("enter the length of the trisngle \n"))
b = int(input("enter the breadth of the triangle \n"))
area = lambda h,b:h*b
print("area of triangle is ",area(a,b))


