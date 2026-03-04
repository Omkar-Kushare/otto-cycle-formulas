import math

def compression_ratio(Vs, Vc):
    return (Vs + Vc) / Vc

def otto_efficiency(r, gamma):
    return 1 - (1 / (r ** (gamma - 1)))

def temperature_T2(T1, r, gamma):
    return T1 * (r ** (gamma - 1))

def temperature_T4(T3, r, gamma):
    return T3 / (r ** (gamma - 1))

def heat_added(m, Cv, T2, T3):
    return m * Cv * (T3 - T2)

def heat_rejected(m, Cv, T1, T4):
    return m * Cv * (T4 - T1)

def net_work(Q_in, Q_out):
    return Q_in - Q_out

def mean_effective_pressure(W_net, Vs):
    return W_net / Vs

def main():
    print("----- OTTO CYCLE CALCULATOR -----")

    # User Inputs
    Vs = float(input("Enter Swept Volume (Vs): "))
    Vc = float(input("Enter Clearance Volume (Vc): "))
    gamma = float(input("Enter Specific Heat Ratio (gamma): "))
    m = float(input("Enter Mass (m): "))
    Cv = float(input("Enter Specific Heat at Constant Volume (Cv): "))
    T1 = float(input("Enter Temperature T1: "))
    T3 = float(input("Enter Temperature T3: "))

    # Calculations
    r = compression_ratio(Vs, Vc)
    eta = otto_efficiency(r, gamma)

    T2 = temperature_T2(T1, r, gamma)
    T4 = temperature_T4(T3, r, gamma)

    Q_in = heat_added(m, Cv, T2, T3)
    Q_out = heat_rejected(m, Cv, T1, T4)

    W_net = net_work(Q_in, Q_out)
    MEP = mean_effective_pressure(W_net, Vs)

    # Output Results
    print("\n----- RESULTS -----")
    print(f"Compression Ratio (r): {r}")
    print(f"Otto Efficiency (η): {eta}")
    print(f"Temperature T2: {T2}")
    print(f"Temperature T4: {T4}")
    print(f"Heat Added (Q_in): {Q_in}")
    print(f"Heat Rejected (Q_out): {Q_out}")
    print(f"Net Work (W_net): {W_net}")
    print(f"Mean Effective Pressure (MEP): {MEP}")

if __name__ == "__main__":
    main()