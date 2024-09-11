import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def h(t: np.ndarray):
    result = np.zeros_like(t)
    t_gt0 = t[t >= 0]
    result[t >= 0] = -2647.5 * np.exp(-15151 * t_gt0) * np.sin(173417 * t_gt0) + 30303 * np.exp(-15151 * t_gt0) * np.cos(173417 * t_gt0)
    return result

def plot_impulse_response():
    csv_data = pd.read_csv('./scope_20.csv', header=1)
    t_vals = np.array(csv_data['second'].to_list())
    h_vals = h(t_vals) / 100000
    
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(t_vals, h_vals)
    ax.plot(t_vals, csv_data['Volt'])

    ax.set_xticklabels([f"{int(x * 1e6)}" for x in ax.get_xticks().tolist()])
    ax.grid(True, which='both')

    ax.set_xlabel(r"Time [$\mathregular{\mu}$s]")
    plt.savefig('plot.pdf')


def main():
    plot_impulse_response()





if __name__ == "__main__":
    main()
