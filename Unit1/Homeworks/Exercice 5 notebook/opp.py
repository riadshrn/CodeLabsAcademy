class Rectangle:
    #Python class named Rectangle constructed by a length and width 
    #and a method which will compute the area of a rectangle.
    def __init__(dim,length,width): 
        dim.length = length
        dim.width = width
    def AreOfTheRectangle(dim):
        return dim.lenght*dim.width


RectangleA = Rectangle(10,2)
print("The area of the rectangle is",Rectangle.AreOfTheRectangle(RectangleA))


class Vehicle:
    #Vehicle class with max_speed and mileage instance attributes
    def __init__(car,max_speed,mileage): 
        car.max_speed = max_speed
        car.mileage = mileage

class _Vehicle:
    #_Vehicle class without any variables and methods.
    pass

class Bus(Vehicle):
    #child class Bus that will inherit all of the variables and methods 
    #of the Vehicle class
    pass