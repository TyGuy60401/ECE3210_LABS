import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot(freq, gain, phase, filename):
    fig, ax1 = plt.subplots()
    ax1.plot(freq, gain, label='Gain', color='#492365')
    ax1.semilogx()
    ax1.grid()
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Gain [dB]")

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


if __name__ == "__main__":
    main()
