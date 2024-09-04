import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def circuit_analysis():
    data = pd.read_csv("./scope_15_good.csv")
    data['computed_input'] = data['second'].apply(lambda t: np.sin(10e3 * np.pi * 2 * t))
    data['computed_output'] = data['second'].apply(lambda t: 0.072056 * np.sin(10e3 * np.pi * 2 * t + 1.4987))
    print(data)

    plt.plot(data['second'], data['Volt'], 'o', label=r"$V_{in}$: 2 V$_{pp}$ @ 10 kHz", markersize=1)
    plt.plot(data['second'], data['Volt.1'], 'o', markersize=1, label=r"$V_{out}$: ~140 mV @ 10 kHz")
    plt.plot(data['second'], data['computed_input'], 'r', label=r"Input computed")
    plt.plot(data['second'], data['computed_output'], 'b', label=r"Output computed")
    
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.title("Phasor circuit measurement")
    plt.legend()
    plt.grid(True, which='both')
    plt.savefig('circuit_analysis.pdf')

def bode_plots():
    bode_data = pd.read_csv('./scope_19.csv')
    w = bode_data['Frequency (Hz)']
    mag = bode_data['Gain']
    phase = bode_data['Phase']

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title("Magnitude [dB]")
    ax1.semilogx(w, mag)
    ax1.grid(True, which='both')

    ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)
    ax2.set_title(r"Phase [$\degree$]")
    ax2.semilogx(w, phase)
    ax2.grid(True, which='both')

    plt.savefig('bode_plots.pdf')


def main():
    circuit_analysis()
    bode_plots()

if __name__ == "__main__":
    main()
