class Particle:
    def __init__(self, charge, mass):
        self.mass = mass
        self.charge = charge

    
class Neitron(Particle):
    def __init__(self):
        mass = 1.67492749804e-27
        charge = 0
        super().__init__(charge, mass)
    def compton(self):
        h = 6.62607015e-34
        c = 299792458 
        m = self.mass
        return h / (m * c)