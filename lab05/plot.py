import matplotlib.pyplot as plt
import pandas as pd
from ece3210_lab05 import *

def fourier_analytical():
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    t_array = np.linspace(-0.00005, 0.00005, 100000, dtype='complex128')
    omega_0 = 40000 * np.pi

    n_vals = range(-35, 35)
    d_n = np.array([compute_dn(n) for n in n_vals])
    result = fourier_series(t_array, d_n, omega_0, n_vals)
    ax.plot(t_array, result, label="Computed Fourier Analysis")

    response = system_response(t_array, d_n, omega_0, n_vals)
    ax.plot(t_array, response, label="Computed System Response")


    data = pd.read_csv('./data/scope_20.csv', header=1)
    data['second'] = data['second'].apply(lambda x: x + 0.1e-3 - 0.0125e-3 if x < -0.0375e-3 else x - 0.0125e-3)
    data = data.sort_values('second')
    ax.plot(data['second'], data['Volt'], label="Measured Input $f(t)$")
    ax.plot(data['second'], data['Volt.1'], label="Measured Output $y(t)$")


    ax.set_xlabel(r'Time [$\mathrm{\mu}$s]')
    ax.set_xticklabels([f"{round(x * 1000000)}" for x in ax.get_xticks().tolist()])
    ax.set_ylabel('Voltage [V]')
    ax.legend()
    ax.grid()
    plt.savefig('./doc/plots/fourier_analysis.pdf')


def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#cbc3dc', '#492365', '#a275b3', '#2dbbc4', '#91c74f', '#efad21', '#f16357', '#8a787c'])
    fourier_analytical()


if __name__ == "__main__":
    main()
