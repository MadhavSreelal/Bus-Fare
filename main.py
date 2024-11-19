class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
        
    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
        
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        final_fare = total_fare + maintenance_charge
        return final_fare

bus = Bus(50)
print("Total fare for bus ride: INR", bus.fare())
