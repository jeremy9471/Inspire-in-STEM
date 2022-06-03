# create a vehicle class without variables and methods
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
Toyota = Vehicle(str(578),str(46))
print("The Toyta mileage is "+ Toyota.mileage + " kilometres and its maximum speed is "+ Toyota.max_speed + " kilometres per hour")

