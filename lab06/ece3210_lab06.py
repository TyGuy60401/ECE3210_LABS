import sounddevice as sd
import numpy as np
import time
import matplotlib.pyplot as plt

def sin(k_array, freq_hz, sample_rate):
    waveform = np.sin(2 * np.pi * k_array * freq_hz / sample_rate)
    return waveform

def plot1():
    duration = 10e-3
    sample_rate = 8e3
    k_array = np.arange(duration * sample_rate)

    fig = plt.figure()

    freqs = [300, 500, 700, 900]
    for i, freq in enumerate(freqs):
        waveform = sin(k_array, freq, sample_rate)
        ax = fig.add_subplot(2, 2, i + 1)
        ax.stem(k_array / sample_rate, waveform, markerfmt='.')
        ax.set_title(f"{freq} Hz")

        if i < 2:
            ax.set_xticklabels([])
        else:
            ax.set_xticklabels([f"{float(x * 1e3):.1f}".rstrip('0').rstrip('.') for x in ax.get_xticks().tolist()])
            ax.set_xlabel("Time [ms]")

        if i % 2 == 1:
            ax.set_yticklabels([])
        else:
            ax.set_ylabel("Amplitude")
    plt.show()


def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#aa989c', '#492365'])
    sample_rate = 8000
    freq_hz = 700.
    duration_s = 3.

    atten = 0.3
    plot1()

    # k = np.arange(duration_s * sample_rate)
    # waveform = sin(k, freq_hz, sample_rate)
    # waveform_quiet = waveform * atten
    #
    # sd.play(waveform_quiet, sample_rate)
    # time.sleep(duration_s)
    # sd.stop()

if __name__ == "__main__":
    main()
