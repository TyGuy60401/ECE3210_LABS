import matplotlib.pyplot as plt
import pandas as pd
from ece3210_lab05 import *

def fourier_analytical():
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    t_array = np.linspace(-0.00005, 0.00005, 100000, dtype='complex128')
    omega_0 = 40000 * np.pi

    d_n = np.array([compute_dn(n) for n in range(35)])
    result = fourier_series(t_array, d_n, omega_0)
    ax.plot(t_array, result)

    response = system_response(t_array, d_n, omega_0)
    ax.plot(t_array, response)


    data = pd.read_csv('./data/scope_20.csv', header=1)
    data['second'] = data['second'].apply(lambda x: x + 0.1e-3 - 0.0125e-3 if x < -0.0375e-3 else x - 0.0125e-3)
    data = data.sort_values('second')
    ax.plot(data['second'], data['Volt'])
    ax.plot(data['second'], data['Volt.1'])

    ax.set_xlabel('Time [ms]')
    ax.set_xticklabels([f"{x * 1000:.2f}" for x in ax.get_xticks().tolist()])
    ax.set_ylabel('Voltage [V]')
    ax.legend()
    ax.grid()
    plt.savefig('./doc/plots/fourier_analysis.pdf')


def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#cbc3dc', '#492365', '#a275b3', '#2dbbc4', '#91c74f', '#efad21', '#f16357', '#8a787c'])
    fourier_analytical()


if __name__ == "__main__":
    main()
