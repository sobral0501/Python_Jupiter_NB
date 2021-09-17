""" A class that can be used to represent a car  """

class Car:
    
    def __init__(self, make, model, year):
        self.make          = make
        self.model         = model
        self.year          = year
        self.odometer_read = 0
        self.gas_tank      = 15
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_read} miles on it.")
        
### This Method was added later  ==> Modifying an Attribute's value through a Method     
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")
            
### Incrementing an Attribute's value through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_read += miles
        
    def fill_gas_tank(self):
        print(f'This car holds {self.gas_tank} gallons of gas.')
        
######################################################################
"""A set of classes used to represent gas and electric cars."""

class Battery:
    
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
        print(f'The battery size is :{self.battery_size}')
                
###########################################################################
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)   #===> initialize attributes of the parent class.
        self.battery = Battery()
       
    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank.")