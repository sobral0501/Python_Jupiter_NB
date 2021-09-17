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