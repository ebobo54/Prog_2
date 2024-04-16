import math

class Particle:
    def __init__(self, charge, mass):
        self.mass = mass
        self.charge = charge

    def specific_charge(self):
        if self.mass == 0:
            return None
        return self.charge / self.mass
class Electron(Particle):
    def __init__(self):
        mass = 9.10938356e-31
        charge = -1.602176634e-19
        super().__init__(charge, mass)
    def compton(self):
        h = 6.62607015e-34  
        c = 299792458  
        m_n = self.mass
        return h / (m_n * c)