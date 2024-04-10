import math

class Particle:
    def __init__(self, mass):
        self.mass = mass

    def specific_charge(self):
        return self.charge / self.mass

class Electron(Particle):
    def __init__(self):
        super().__init__(9.10938356e-31) 
        self.charge = -1.602176634e-19

def calculate_compton_wavelength(particle):
    h = 6.62607015e-34
    c = 299792458 
    return h / (particle.mass * c)

