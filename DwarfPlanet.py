import math
from random import randint

from Planet import Planet


class DwarfPlanet(Planet):
    '''DwarfPlanet is derived from CelestialBody class.'''
    def __init__(self, planet_data):
        '''calls base class constructor, then assigns a bracketed, semi-random radius value.'''
        super().__init__(planet_data)
        self.p_radius = randint(0, 8675309)

    @property
    def radius(self):
        return self.p_radius

    def volume(self):
        r = self.radius
        return (4.0 / 3.0) * math.pi * r * r * r
