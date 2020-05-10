from random import randint

from CelestialBody import CelestialBody


class Planet(CelestialBody):
    '''Planet is derived from CelestialBody class.'''
    def __init__(self, planet_data):
        '''calls base class constructor, then assigns a bracketed, semi-random radius value.'''
        super().__init__(planet_data)
        # Planet radius with a restricted lower/upper boundary
        self.p_radius = randint(10000, 11000)

    @property
    def radius(self):
        return self.radius
