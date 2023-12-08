#create a class car with attributes color price and kilo meter and compare the price of two cars and add the total kilo meters of 2 cars
#operator overloading
class Car:
    def __init__(self,color,price,km):
            self.color = color
            self.price = price
            self.km = km
    def __gt__(self,others):
        if(self.price>others.price):
            return True
        else:
            return False
    def __add__(self,others):
        return self.km+others.km
c1 = Car("black",1200,2000)
c2 = Car("red",2110,4000)
if (c1>c2):
    print("car 1 price is high")
else:
    print("car 2 price is high")
print(c1+ c2)

            
