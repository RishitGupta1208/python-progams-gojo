class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        ef=3.14*self.radius**2
        print(ef)
    def perimeter(self):
        er=6.28*self.radius
call=circle(9)
call.area()
call.perimeter()