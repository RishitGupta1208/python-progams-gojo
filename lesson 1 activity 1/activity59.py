class dog:
    species='animal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
beagle=dog('beagle',20)
pitbull=dog('pitbull',15)
print("blu is a {}".format(beagle.species))
print("woo is a {}".format(pitbull.species))
print("{} is {} years old".format(beagle.name,beagle.age))
print("{} is {} years old".format(pitbull.name,pitbull.age))