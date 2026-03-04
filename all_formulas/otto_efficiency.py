def otto_efficiency_from_r(r, gamma):
    return 1 - (1 / (r ** (gamma - 1)))

def otto_efficiency_from_work(W_net, Q_in):
    return W_net / Q_in
    