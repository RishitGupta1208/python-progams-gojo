class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        ef=3.14*self.radius**2
        print(ef)
call=circle(9)
call.area()