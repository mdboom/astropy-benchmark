import unittest

from astropy import units as u


class TestUnit(unittest.TestCase):
    def test_unit_compose(self):
        u.Ry.compose()

    def test_unit_to(self):
        u.m.to(u.pc)
