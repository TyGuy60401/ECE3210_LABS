import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def circuit_analysis():
    data = pd.read_csv("./scope_15_good.csv")
    data['computed_input'] = data['second'].apply(lambda t: np.sin(10e3 * np.pi * 2 * t))
    data['computed_output'] = data['second'].apply(lambda t: 0.072056 * np.sin(10e3 * np.pi * 2 * t + 1.4987))

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(data['second'], data['Volt'], 'o', markersize=1, label=r"$V_{in}$ recorded")
    ax.plot(data['second'], data['Volt.1'], 'yo', markersize=1, label=r"$V_{out}$ recorded")
    ax.plot(data['second'], data['computed_input'], 'b', linewidth=1, label=r"$V_{in}$: 2 V$_{pp}$ @ 10 kHz")
    ax.plot(data['second'], data['computed_output'], 'orange', linewidth=1, label=r"$V_{out}$: ~144 mV$_{pp}$ @ 10 kHz")
    
    ax.set_xlabel('Time [ms]')
    ax.set_ylabel('Voltage [V]')
    # ax.set_title("Phasor circuit analysis and measurement")

    ax.set_xticklabels([f"{x * 1000:.3f}" for x in ax.get_xticks().tolist()])

    ax.legend()
    ax.grid(True, which='both')
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
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)
    ax2.set_title(r"Phase [$\degree$]")
    ax2.semilogx(w, phase)
    ax2.grid(True, which='both')
    ax2.set_xlabel('Frequency [Hz]')

    plt.savefig('bode_plots.pdf')

def compare_analytical_cumtrapz_plot():
    data = pd.read_csv("./compare_analytical_cumtrapz.csv")

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(data['t_vals'], data['ct_y_vals'], label="py_cumtrapz Function")
    ax.plot(data['t_vals'], data['ana_y_vals'], label="Analytical Solution")
    ax.grid(True, which='both')

    ax.set_xlabel('t')

    ax.legend()
    plt.savefig('comparison.pdf')


def main():
    circuit_analysis()
    bode_plots()
    compare_analytical_cumtrapz_plot()

if __name__ == "__main__":
    main()
