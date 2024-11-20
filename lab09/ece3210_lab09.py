import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp


def cheby1(fp, fs, r, Gs):
    wp = fp/(2*np.pi)
    ws = fs/(2*np.pi)
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
    # ymin, ymax = ax.get_ybound()
    # ax.vlines([0], colors=['#000000'], ymin=ymin, ymax=ymax)
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

def main():
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

if __name__ == "__main__":
    main()