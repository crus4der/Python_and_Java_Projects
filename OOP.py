
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print("Exer 1")
print(modelX.max_speed, modelX.mileage)

print("\nExer 2")
class Vehicle2:
    pass

print("\nExer 3")
class Vehicle3:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle3):
        pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

print("\nExer 4")
class Vehicle4:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle4):
    pass

class Car(Vehicle4):
    pass

print("\nExer 5")
bus = Bus("SchoolVolvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print("Color: White,", "Vehicle name:", bus.name, "Speed:", bus.max_speed, "Mileage:", bus.mileage)
print("Color: White,", "Vehicle name:", car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

print("\nExer 6")
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print("\nExer 7")
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))

print("\nExer 8")
class Vehicle8:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle8))