import pandas as pd
import matplotlib.pyplot as plt

def circuit_analysis():
    input = pd.read_csv("./scope_15_good.csv")
    # input['second'] = input['second'].apply(lambda x: 1000 * x)
    # plt.figure()
    plt.plot(input['second'], input['Volt'], label=r"$V_{in}$: 2 V$_{pp}$ @ 10 kHz")
    plt.plot(input['second'], input['Volt.1'], label=r"$V_{out}$: ~140 mV @ 10 kHz")
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.title("Phaser circuit measurement")
    plt.legend()
    plt.grid(True, which='both')

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





def main():
    circuit_analysis()
    bode_plots()
    plt.show()

if __name__ == "__main__":
    main()
