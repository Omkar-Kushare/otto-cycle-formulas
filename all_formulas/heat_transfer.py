def heat_added(m, Cv, T2, T3):
    return m * Cv * (T3 - T2)


def heat_rejected(m, Cv, T1, T4):
    return m * Cv * (T4 - T1)