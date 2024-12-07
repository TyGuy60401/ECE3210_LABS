import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from sympy import solve, Symbol, Eq, symbols


def cheby1(fp, fs, r, Gs):
    wp = fp*(2*np.pi)
    ws = fs*(2*np.pi)
    N, wc = sp.signal.cheb1ord(wp, ws, r, Gs, analog=True)
    numerator, denominator = sp.signal.cheby1(N, r, wc, analog=True, output='ba')
    zeros, poles, krap = sp.signal.cheby1(N, r, wc, analog=True, output='zpk')
    print("Zeros")
    print(zeros)
    print("Poles")
    fig, ax = plt.subplots()
    coords = [(np.real(pole), np.imag(pole)) for pole in poles]
    for coord in coords:
        ax.plot(coord[0], coord[1], 'x', color='blue')
    ax.set_xbound(-325, 325)
    ax.grid()
    plt.show()
    print(poles)
    print("Numerator")
    print(numerator)
    print("Denominator")
    print(denominator)
    w_ang, h = sp.signal.freqs(numerator, denominator)
    return w_ang, h, zeros, poles


def second_order_filter(omega_c_2, omega_c_zeta, R):
    C1 = Symbol('C1')
    C2 = Symbol('C2')
    eq1 = Eq(1/(R*R*C1*C2), omega_c_2)
    eq2 = Eq((2*R)/(R*R*C1), omega_c_zeta)
    solution = solve((eq1, eq2), (C1, C2))
    return solution

def chebyshev_components():
    ...

def part1():
    fp = 7500 #Hz
    fs = 10000 #Hz
    r = 1.5 #dB
    Gs = 24 #dB
    w_ang, h, zeros, poles = cheby1(fp, fs, r, Gs)
    import matplotlib.pyplot as plt
    plt.semilogx(w_ang, 20 * np.log10(abs(h)))
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response [dB]')
    plt.grid(True)
    plt.show()

def part2():
    res = pd.read_csv("./resistors.txt")
    print("First filter")
    for r in list(res['# Use # to denote comments']):
        r = int(r)
        w_c_2 = 2.149e9
        w_c_z = 7212
        print(r, second_order_filter(w_c_2, w_c_z, r))

    print("Second filter")
    for r in list(res['# Use # to denote comments']):
        r = int(r)
        w_c_2 = 9.034e8
        w_c_z = 18882
        print(r, second_order_filter(w_c_2, w_c_z, r))

    print("Final first order")
    for r in list(res['# Use # to denote comments']):
        r = float(r)
        print(r, 1 / (1.167e4 * r))



def main():
    # fp = 7500 #Hz
    # fs = 10000 #Hz
    # r = 1.5 #dB
    # Gs = 24 #dB
    # w_ang, h, zeros, poles = cheby1(fp, fs, r, Gs)
    # import matplotlib.pyplot as plt
    # plt.semilogx(w_ang, 20 * np.log10(abs(h)))
    # plt.xlabel('Frequency')
    # plt.ylabel('Amplitude response [dB]')
    # plt.grid(True)
    # plt.show()
    part1()
    part2()



if __name__ == "__main__":
    main()
