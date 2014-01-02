from astropy import units as u


class TimeUnit:
    def time_unit_compose(self):
        u.Ry.compose()

    def time_unit_to(self):
        u.m.to(u.pc)


def time_unit_parse():
    u.Unit('1e-07 kg m2 / s2')


def mem_unit():
    return u.erg
