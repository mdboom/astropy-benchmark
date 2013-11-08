import unittest

from astropy import coordinates


class TestLatitude(unittest.TestCase):
    def test_latitude(self):
        coordinates.Latitude(3.2)
