class vehicle():
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
value=vehicle(240,19)
print("max speed of the model:",value.max_speed)
print("milage of the model:",value.milage)