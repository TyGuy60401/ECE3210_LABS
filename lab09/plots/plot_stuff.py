import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import signal
from sympy import solve, Symbol, Eq, symbols

def plot_mag_phase(freq, mag, phase, file_name):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.semilogx(freq, mag)
    ax1.set_ylabel("Magnitude [dB]")
    ax1.grid(which="both")
    ax1.axvline(7500, linestyle='--')

    ax1.annotate("7500 Hz", (3200, -27))

    ax2.semilogx(freq, phase)
    ax2.set_ylabel("Phase [°]")
    ax2.grid(which="both")

    ax2.set_xlabel("Frequency [Hz]")

    plt.savefig(file_name)

def cheby1(fp, fs, r, Gs):
    wp = fp*(2*np.pi)
    ws = fs*(2*np.pi)
    N, wc = sp.signal.cheb1ord(wp, ws, r, Gs, analog=True)
    numerator, denominator = sp.signal.cheby1(N, r, wc, analog=True, output='ba')
    zeros, poles, krap = sp.signal.cheby1(N, r, wc, analog=True, output='zpk')
    w_ang, h = sp.signal.freqs(numerator, denominator)
    return w_ang, h, zeros, poles
    

def main():
    # Python calculation
    fp = 7500 #Hz
    fs = 10000 #Hz
    r = 1.5 #dB
    Gs = 24 #dB
    calc_freq, h, zeros, poles = cheby1(fp, fs, r, Gs)
    calc_freq = calc_freq / (2 * np.pi)
    calc_mag = 20 * np.log10(abs(h))
    calc_phase = np.degrees(np.unwrap(np.angle(h)))
    plot_mag_phase(calc_freq, calc_mag, calc_phase, 'calculation_results.pdf')
    # zeros and poles
    # fig, ax = plt.subplots()
    # coords = [(np.real(pole), np.imag(pole)) for pole in poles]
    # for coord in coords:
    #     ax.plot(coord[0], coord[1], 'x', color='blue')
    # ax.set_xbound(-325, 325)
    # ax.grid()
    # plt.show()

    # plt.figure()
    
    # plt.semilogx(calc_freq, 20 * np.log10(abs(h)))
    # plt.xlabel('Frequency')
    # plt.ylabel('Amplitude response [dB]')
    # plt.grid(True)
    # plt.show()



    # Measurement
    data_meas = pd.read_csv("../meas/scope_21.csv", encoding='latin1')
    data_meas = data_meas[data_meas[' Frequency (Hz)'] < 30e3]

    meas_freq = data_meas[' Frequency (Hz)']
    meas_mag = data_meas[' Gain (dB)']
    meas_phase = np.degrees(np.unwrap(np.radians(data_meas[' Phase'])))

    plot_mag_phase(meas_freq, meas_mag, meas_phase, './measurement_results.pdf')

    # Simulation
    data_sim_mag = pd.read_csv("../sim/mag.csv")
    data_sim_phase = pd.read_csv("../sim/phase.csv")

    sim_freq = data_sim_mag['X--Trace 1::[V(11) | V(PR1)]']
    sim_mag = 20 * np.log10(data_sim_mag['Y--Trace 2::[V(9) | V(PR2)]'])
    sim_phase = data_sim_phase['Y--Trace 2::[V(9) | V(PR2)]']

    plot_mag_phase(sim_freq, sim_mag, sim_phase, './simulation_results.pdf')


if __name__ == '__main__':
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#492365', '#a275b3', '#2dbbc4', '#91c74f', '#efad21', '#f16357', '#8a787c'])
    main()
