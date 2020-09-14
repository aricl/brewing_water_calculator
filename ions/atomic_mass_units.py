from mendeleev import element


def hydrogen():
    return element('H').atomic_weight


def carbon():
    return element('C').atomic_weight


def oxygen():
    return element('O').atomic_weight


def sodium():
    return element('Na').atomic_weight


def magnesium():
    return element('Mg').atomic_weight


def sulphur():
    return element('S').atomic_weight


def chlorine():
    return element('Cl').atomic_weight


def calcium():
    return element('Ca').atomic_weight


def sulphate():
    return sulphur() + (4 * oxygen())


def carbonate():
    return carbon() + (3 * oxygen())


def water():
    return 2 * hydrogen() + oxygen()
