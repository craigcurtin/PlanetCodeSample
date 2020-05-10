import math

# constant value for G, used below
G = 6.67408e-11


class CelestialBody(object):
    '''CelestialBody is base class all elements in Solar System.'''
    def __init__(self, planet_data):
        '''input is a token list, ordinality is important.'''
        self.p_pos = [float(planet_data[0]),
                      float(planet_data[1]),
                      float(planet_data[2])]
        self.p_vel = [float(planet_data[3]),
                      float(planet_data[4]),
                      float(planet_data[5])]
        self.p_mass = float(planet_data[6])
        self.p_label = planet_data[7]
        self.p_type = planet_data[8]

    def pos(self):
        return self.p_pos

    @property
    def mass(self):
        return self.p_mass

    @property
    def vel(self):
        return self.p_vel

    @property
    def name(self):
        return self.p_label

    def volume(self):
        '''Expect derived classes to set this, if called on Star '''
        if not hasattr(self, 'p_vol'):
            rv = 0
        else:
            rv = self.p_vol
        return rv

    def get_type(self):
        return self.p_type

    def getGravitationalPotential(self):
        '''Kind of random calculation to provide uniqueness in the Gravity Potential'''
        if self.get_type() != '0':
            dx, dy, dz = self.pos()
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            # C++ code took average ... just a random number here ...
            pot = self.mass / dist
            pot *= -G * self.mass
        else:
            pot: float = float(0)
        return pot
