class BMW:
    def fuel_type(self):
        return "Petrol / Diesel"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"


# Polymorphism in action
for car in (BMW(), Ferrari()):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("------")