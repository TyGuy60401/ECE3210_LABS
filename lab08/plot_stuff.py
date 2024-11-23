import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import TransferFunction, bode

def hand_calc():
    R1 = 220
    R2 = 220
    C1 = 144.7e-9
    C2 = 36.17e-9
    omega_c = 1 / np.sqrt(R1 * R2 * C1 * C2)
    zeta = 1 / (R1 * C1) + 1 / (R2 * C1)
    numerator = [omega_c ** 2]
    denominator = [1, (R1 + R2)/(R1*R2*C1), omega_c ** 2]
    # denominator = [1, 2 * zeta, omega_c ** 2]
    system = TransferFunction(numerator, denominator)

    frequencies = np.logspace(1, 6, 500)
    w, mag, phase = bode(system, w=frequencies)

    fig, ax1 = plt.subplots()
    ax1.semilogx()  # Use semilogx for logarithmic frequency axis
    ax1.plot(w / (2 * np.pi), mag, label='Gain', color='#492365')
    ax1.grid()
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Gain [dB]")
    # plt.legend()

    ax2 = ax1.twinx()
    ax2.plot(w / (2 * np.pi), phase, label="Phase", color='#aa989c')
    ax2.set_ylabel("Phase [°]")
    plt.legend()
    plt.tight_layout()

    plt.savefig("./pdf/calculation.pdf")
    # plt.grid(which='both', linestyle='--', linewidth=0.5)

def plot(freq, gain, phase, filename):
    fig, ax1 = plt.subplots()
    ax1.plot(freq, gain, label='Gain', color='#492365')
    ax1.semilogx()
    ax1.grid()
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Gain [dB]")
    # plt.legend()

    ax2 = ax1.twinx()
    ax2.plot(freq, phase, label='Phase', color='#aa989c')
    ax2.set_ylabel("Phase [°]")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'./pdf/{filename}.pdf')

def main():
    data = pd.read_csv("./scope_0_new.csv", encoding='latin1')
    freq = data[' Frequency (Hz)']
    gain = data[' Gain (dB)']
    phase = np.array(data[' Phase (°)'])
    phase = np.degrees(np.unwrap(np.radians(phase)))
    
    plot(freq, gain, phase, 'measurements')

    data_sim = pd.read_csv("./lab8_sim.csv")
    freq = data_sim['X--Trace 1::[V(1) | V(V_out)]']
    gain = data_sim['Y--Trace 1::[V(1) | V(V_out)]']
    gain = 20*np.log10(gain)
    data_sim_phase = pd.read_csv("./lab8_sim_phase.csv")
    phase = data_sim_phase['Y--Trace 1::[V(1) | V(V_out)]']
    plot(freq, gain, phase, 'simulation')

    hand_calc()


if __name__ == "__main__":
    main()
