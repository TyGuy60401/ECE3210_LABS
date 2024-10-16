import sounddevice as sd
import numpy as np
import time
import matplotlib.pyplot as plt

def sin(k_array, freq_hz, sample_rate):
    return np.sin(2 * np.pi * k_array * freq_hz / sample_rate)

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
    plt.savefig('./doc/figures/stem.pdf')

def play_sounds():
    sample_rate = 8000
    freq_hz = 700.
    duration_s = 3.

    atten = 0.3
    frequencies = [7700, 7500, 7300, 900]

    k = np.arange(duration_s * sample_rate)
    waveforms = [sin(k, freq, sample_rate) * atten for freq in frequencies]
    # waveform = sin(k, freq_hz, sample_rate)
    # waveform_quiet = waveform * atten

    for i, waveform in enumerate(waveforms):
        print(f"Playing: {frequencies[i]}")
        sd.play(waveform, sample_rate)
        time.sleep(duration_s)
        sd.stop()

def chirp(A, mu, freq, phi, t_array):
    return A * np.cos(np.pi * mu * t_array * t_array + 2 * np.pi * freq + phi)

def show_and_hear_chirp():
    fig = plt.figure()

    fs_s = [32000, 16000, 8000]
    data_list = [
        { 'frequency': fs_s[0] },
        { 'frequency': fs_s[1] },
        { 'frequency': fs_s[2] }
    ]
    duration = 8
    for i, fs_data in enumerate(zip(fs_s, data_list)):
        print(i)
        ax = plt.subplot2grid((2, 2), (i // 2, i % 2), colspan=2 if i == 2 else 1)
        t_array = np.linspace(0, duration, fs_data[0] * duration)
        chirp_signal = chirp(0.3, 2000, 100, 0, t_array)
        # sd.play(chirp_signal, fs_data[0])
        # time.sleep(duration)
        # sd.stop()

        first_2000 = chirp_signal[:2000]

        ax.plot(t_array[:2000], first_2000)
        ax.set_title(f"{fs_data[1]['frequency']} Hz")
    plt.tight_layout()
    plt.savefig("./doc/figures/chirp.pdf")


def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#aa989c', '#492365'])
    plot1()
    # play_sounds()
    show_and_hear_chirp()


if __name__ == "__main__":
    main()
