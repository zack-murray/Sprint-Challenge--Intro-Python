# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle will be the base class, since flight/ground vehicles will inherit from them
class Vehicle:
    def __init__(self):
        pass

# Child class of vehicle, parent class of starship/airplane
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# Child class of vehicle, parent class of car/motorcycle
class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# Child class of flightvehicle
class Starship(FlightVehicle):
    def __init__(self):
        pass

# Child class of flightvehicle
class Airplane(FlightVehicle):
    def __init__(self):
        pass

# Child class of groundvehicle
class Car(GroundVehicle):
    def __init__(self):
        pass

# Child class of groundvehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        pass