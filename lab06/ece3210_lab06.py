import sounddevice as sd
import numpy as np
import time
import matplotlib.pyplot as plt

def sin(k_array, freq_hz, sample_rate):
    return np.sin(2 * np.pi * k_array * freq_hz / sample_rate)

def aliasing_example():
    f_s = 8000

    f_1 = 1600
    f_2 = f_s - f_1


    duration = 1/f_1
    t_array = np.linspace(0, duration, 1000)
    sin_2 = np.sin(2*np.pi*f_2 * t_array)
    sin_1 = np.sin(2*np.pi*f_1 * t_array)

    k_array = np.arange(0, duration * f_s)

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.plot(t_array, -sin_2, label=f'{f_2} Hz Signal')
    ax.plot(t_array, sin_1, label=f'{f_1} Hz Signal')
    ax.vlines(k_array/f_s, ymin=-1, ymax=1, linestyles='dashed', linewidth=1, colors='#333')

    custom_legend = plt.Line2D([0], [0], color='#333', linestyle='dashed', linewidth=1, label='8000 Hz Sampling')
    handles, labels = plt.gca().get_legend_handles_labels()
    handles.append(custom_legend)
    labels.append('8000 Hz Sample Rate')
    ax.legend(loc='upper right', handles=handles, labels=labels)

    ax.set_xticklabels([f"{round(x * 1e6):.1f}".rstrip('0').rstrip('.') for x in ax.get_xticks().tolist()])
    ax.set_xlabel(r"Time [μs]")
    ax.set_ylabel(f"Amplitude")
    
    plt.savefig('./doc/figures/aliasing.pdf')

def stem_plots(frequencies):
    duration = 10e-3
    sample_rate = 8e3
    k_array = np.arange(duration * sample_rate)

    fig = plt.figure()

    for i, freq in enumerate(frequencies):
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
    plt.savefig(f'./doc/figures/stem_{"-".join([str(freq) for freq in frequencies])}.pdf')

def play_sounds(frequencies):
    sample_rate = 8000
    duration_s = 3.

    atten = 0.3

    k = np.arange(duration_s * sample_rate)
    waveforms = [sin(k, freq, sample_rate) * atten for freq in frequencies]
    sound = np.hstack(waveforms)
    print(f"Playing: {frequencies}")
    sd.play(sound, sample_rate)
    time.sleep(duration_s * len(waveforms))
    sd.stop()

def chirp(A, mu, freq, phi, t_array):
    return A * np.cos(np.pi * mu * t_array * t_array + 2 * np.pi * freq + phi)

def show_and_hear_chirp():

    fs_s = [32000, 16000, 8000]
    data_list = [
        { 'frequency': fs_s[0] },
        { 'frequency': fs_s[1] },
        { 'frequency': fs_s[2] },
    ]
    duration = 8
    for i, fs_data in enumerate(zip(fs_s, data_list)):
        fig = plt.figure()
        # ax = fig.add_subplot(3, 1, i+1)
        ax = plt.axes()
        fig.add_axes(ax)
        t_array = np.linspace(0, duration, fs_data[0] * duration)
        chirp_signal_0 = chirp(0.3, 2000, 100, 0, t_array)
        chirp_signal_1 = chirp(0.3, 1000, 100, 0, t_array)
        print(f"Playing chirp {fs_data[0]} u = 2000")
        sd.play(chirp_signal_0, fs_data[0])
        time.sleep(duration)
        sd.stop()
        print(f"Playing chirp {fs_data[0]} u = 1000")
        sd.play(chirp_signal_1, fs_data[0])
        time.sleep(duration)
        sd.stop()

        first_2000 = chirp_signal_0[:2000]

        ax.plot(t_array[:2000], first_2000)

        ax.set_xticklabels([f"{round(x * 1e3):.1f}".rstrip('0').rstrip('.') for x in ax.get_xticks().tolist()])
        ax.set_title(f"{fs_data[1]['frequency']} Hz")
        ax.set_xlabel(f"Time [ms]")
        ax.set_ylabel(f"Amplitude")
        # plt.tight_layout()
        plt.savefig(f"./doc/figures/chirp_{fs_data[1]['frequency']}.pdf")

def chirp_samples():
    t_array = np.linspace(0, 8, 1000)
    line_1 = t_array * 1
    line_2 = np.hstack([[t * 1 for t in t_array[:len(t_array) // 2]], [t * -1 + 8 for t in t_array[len(t_array) // 2:]]])
    quarter_len = len(t_array) // 4
    line_3_part1 = [t for t in t_array[:quarter_len]]
    line_3_part2 = [t * -1 + 4 for t in t_array[quarter_len:quarter_len * 2]]
    line_3_part3 = [t - 4 for t in t_array[quarter_len * 2:quarter_len * 3]]
    line_3_part4 = [t * -1 + 8 for t in t_array[quarter_len * 3:]]
    line_3 = np.hstack([line_3_part1, line_3_part2, line_3_part3, line_3_part4])
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(t_array, line_1 + 0.08, label="Chirp @ 32 kHz")
    ax.plot(t_array, line_2, label="Chirp @ 16 kHz")
    ax.plot(t_array, line_3 - 0.08, label="Chirp @ 8 kHz")
    ax.get_yaxis().set_ticks([])
    ax.get_xaxis().set_ticks([])
    ax.set_ylabel("Perceived Frequency")
    ax.set_xlabel("Input Frequency")
    ax.legend()

    plt.savefig("./doc/figures/chirp_samples.pdf")


def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#aa989c', '#492365', '#f16357', '#8a787c', '#2dbbc4'])
    stem_plots([300, 500, 700, 900])
    stem_plots([7700, 7500, 7300, 7100])
    play_sounds([300, 500, 700, 900])
    play_sounds([7700, 7500, 7300, 7100])
    aliasing_example()
    show_and_hear_chirp()
    chirp_samples()


if __name__ == "__main__":
    main()
