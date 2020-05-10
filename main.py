from collections import defaultdict
from random import seed

#seed the rand() generator, used for Radius() and Volume() calculations
#for testing, a constant seed is good for repeatable.
#In production, seeding with number of seconds (or other 'unique' value is good)
seed(42)

# these are referenced from incoming .csv files, used by ClassFactory() to instantiate
Star = '0'
Planetary = '1'
DwarfPlanetary = '2'

#derrived classes in Solar System
#PlanetFactory() uses the below explicit imports because it creates the instance
#dynamically and therefore explicit imports are required.
from CelestialBody import CelestialBody
from Planet import Planet
from DwarfPlanet import DwarfPlanet

# PlanetFactory() instantiates the specific class
targetClass = ['CelestialBody', 'Planet', 'DwarfPlanet']

class PlanetFactory(object):
    '''Each input record describes an item in the Solar System.'''
    def __init__(self, planets_data):
        '''PlanetFactory(), each row provides descriptive data to create a Planet.'''
        self.body = defaultdict(list)

        for planet_data in planets_data:
            planet_tokens = planet_data[:-1].split(',')
            planet_type = int(planet_tokens[8])
            tc = targetClass[planet_type]
            #here is the dynamic invocation of target class
            p = (globals()[tc])(planet_tokens)
            self.body[p.get_type()].append(p)

    def getPlanetsOfType(self, T):
        '''return list of Planets that are of Type T.'''
        return self.body[T]

if __name__ == '__main__':
    #read input file for planetary configuration at startup
    planet_data = open('Data/planetary-system.csv').readlines()
    pf = PlanetFactory(planet_data)

    for pt in [Star, Planetary, DwarfPlanetary] :
        for planet in pf.getPlanetsOfType(pt):
            print('Name: {}\tType: {}\tVolume: {}\tGravity: {}'.format(planet.name,
                                                                       planet.get_type(),
                                                                       planet.volume(),
                                                                       planet.getGravitationalPotential()))
