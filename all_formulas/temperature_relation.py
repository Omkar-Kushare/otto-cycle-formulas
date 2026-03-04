def temperature_ratio_T2_T1(r, gamma):
    return r ** (gamma - 1)


def temperature_ratio_T3_T4(r, gamma):
    return r ** (gamma - 1)


def T2_from_T1(T1, r, gamma):
    return T1 * (r ** (gamma - 1))


def T4_from_T3(T3, r, gamma):
    return T3 / (r ** (gamma - 1))


