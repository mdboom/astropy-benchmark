import unittest

from astropy import coordinates
from astropy import units

class TestLatitude(unittest.TestCase):
    def test_latitude(self):
        coordinates.Latitude(3.2, units.degree)
