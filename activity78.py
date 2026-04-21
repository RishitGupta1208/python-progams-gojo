class Vehicle:
    def __init__(self, fare_per_person):
        self.fare_per_person = fare_per_person
class Bus(Vehicle):
    def __init__(self, fare_per_person, passengers):
        super().__init__(fare_per_person)
        self.passengers = passengers

    def total_fare(self):
        total = self.fare_per_person * self.passengers
        return total
bus1 = Bus(50, 10)
print("Total Fare:", bus1.total_fare())