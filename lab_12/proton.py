import math

class Particle:
    def __init__(self, mass):
        self.mass = mass

    def specific_charge(self):
        return self.charge / self.mass

class Proton(Particle):
    def __init__(self):
        super().__init__(1.67262192369e-27)  
        self.charge = 1.602176634e-19  