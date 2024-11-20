import numpy as np
import matplotlib.pyplot as plt


def ex1():
    k = np.arange(0, 100000)
    f = np.cos(k * np.pi / 100)
    ten_vals = np.arange(1000)
    f_1 = f[:1000]
    f_2 = f[-2000:-1000]
    # print("First 10 samples of f:", f_1)
    # print("Last 10 samples of f:", f_2)
    plt.plot(ten_vals, f_1, 'blue', linewidth=2)
    plt.plot(ten_vals, f_2, 'red', linewidth=1)
    plt.show()
    # Omega = 1.7 * np.pi

def ex2():
    k = np.arange(0, 6, 1)
    t = np.linspace(0, 5, 1000)
    Omega = 1.7*np.pi
    Omega_normalized = Omega - 2*np.pi
    y_t = np.cos(Omega*t)

    y_norm = np.cos(Omega_normalized * t)
    y_k = np.cos(Omega * k)
    y_k_norm = np.cos(Omega_normalized * k)

    plt.figure()
    plt.plot(t, y_t)
    plt.show()

    plt.figure()
    plt.plot(t, y_t)
    plt.stem(k, y_k)
    plt.show()

    plt.figure()
    plt.plot(t, y_t, label="y(t)")
    plt.stem(k, y_k, label="y[k]")
    plt.plot(t, y_norm, label="y(t) normalized")
    plt.stem(k, y_k_norm, label="y[k] noramlized")
    plt.legend()
    plt.show()

def main():
    # ex1()
    ex2()


if __name__ == "__main__":
    main()
