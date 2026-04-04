class vehicle:
    def __init__(self,maximum_speed,milage,name):
        self.maximum_speed=maximum_speed
        self.milage=milage
        self.name=name
class bus(vehicle):
    pass
school_bus=bus(182,18,"school volvo")
print("vehicle name: ",school_bus.name,"speed: ",school_bus.maximum_speed,"milage: ",school_bus.milage)