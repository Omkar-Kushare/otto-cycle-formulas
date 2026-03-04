def net_work_from_heat(Q_in, Q_out):
    return Q_in - Q_out


def net_work_from_efficiency(eta, Q_in):
    return eta * Q_in



def net_work_from_r_Qin(r, gamma, Q_in):
    return (1 - (1 / (r ** (gamma - 1)))) * Q_in


def net_work_from_mCvTemps(m, Cv, T1, T2, T3, T4):
    return m * Cv * ((T3 - T2) - (T4 - T1))