from graphics import circle,rectangle
from graphics.Graphics_D import cuboid as cub
from graphics.Graphics_D import sphere as sp

circle.areaofcircle(int(input("enter the radius for circle to find area: ")))
circle.perimeterofcircle(int(input("enter the radius for circle to find perimeter: ")))

rectangle.areaofrectangle(int(input("enter the length for rectangle: ")),int(input("enter the breadth for rectangle: ")))
rectangle.perimeterofrectangle(int(input("enter the length for rectangle: ")),int(input("enter the breadth for rectangle: ")))

cub.areaofcuboid()
cub.perimeterofcuboid()

sp.areaofsphere(int(input("enter the radius for sphere: ")))
sp.perimeterofsphere(int(input("enter the radius for sphere: ")))

