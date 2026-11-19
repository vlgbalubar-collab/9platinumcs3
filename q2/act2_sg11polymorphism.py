# Guide Questions

# 1. a. What is duck typing, as explained in the video?
#       Duck typing is based on the philosophy "If it walks like a duck and quacks like a duck, it's a duck." It means that if an object has the required method, Python can use it regardless of what class it comes from, making code more flexible without needing a strict inheritance structure.
#    b. b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class? 
#       It needed to have the required method that matched what the loop calls, allowing Python to interact with it successfully based on behavior rather than class type.

# 2.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car_obj = Car()
boat_obj = Boat()
drone_obj = Drone()

start_trip(car_obj)
start_trip(boat_obj)
start_trip(drone_obj)
