def areaofcuboid():
    l = int(input("enter the length for cube: "))
    b = int(input("enter the breadth for cube: "))
    h = int(input("enter the heigth for cube: "))
    area = 2*((l*b)+(b*h)+(l*h))
    print("area of cuboid: ",area)

def perimeterofcuboid():
    l = int(input("enter the length for cube: "))
    b = int(input("enter the breadth for cube: "))
    h = int(input("enter the heigth for cube: "))
    peri= 4*(l+b+h)
    print("perimeter of cuboid: ",peri)
    
    
