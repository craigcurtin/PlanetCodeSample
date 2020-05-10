from unittest import TestCase

from CelestialBody import CelestialBody

#sample solar elements
starTokens = '0.0,0.0,0.0,0.0,0.0,0.0,1602075314.00000000,central-star,0'.split(',')
planetTokens = '3345048107.00000000,1618127707.00000000,4001288224.00000000,1444061399.00000000,2700534436.00000000,1938647176.00000000,1459718602.00000000,alpha,1'.split(',')
dwarfTokens = '352248782.00000000,3700326028.00000000,965464548.00000000,3236553557.00000000,1342363444.00000000,1740229486.00000000,4006226087.00000000,iota,2'.split(',')

class TestCelestialBody(TestCase):
    def setUp(self) -> None:
        self.cb = CelestialBody(starTokens)

class TestPositions(TestCelestialBody):
    #positive pos testing
    def test_pos_star_NE(self):
        actual = self.cb.pos()
        expected = [ 0.0, 0.0, 0.0 ]
        self.assertEqual(actual, expected, 'positive pos testing, fail')

    #negative pos testing
    def test_pos_star_EQ(self):
        actual = self.cb.pos()
        expected = [ 1.0, 0.0, 0.0 ]
        self.assertNotEqual(actual, expected, 'negative pos testing, fail')


    # TODO, lots more testing needed