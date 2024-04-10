import math

class Particle:
    def __init__(self, mass):
        self.mass = mass

    def specific_charge(self):
        return self.charge / self.mass
    
class Neitron(Particle):
    def __init__(self):
        super().__init__(1.674927471e-27) 
        self.charge = 0  