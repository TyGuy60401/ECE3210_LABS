import numpy as np


def compute_dn(n):
    """Calculate the d_n coefficient for a square wave with magnitude 4 and frequency 20000 Hz

    Parameters
    ----------
    n : int
        Harmonic number

    Returns
    -------
    float
        b_n coefficient of the n-th harmonic
    """
    omega_0 = 40000 * np.pi
    T_0 = 1 / 20000
    return 0 if n == 0 else 160000 / (n * omega_0) * (4 * np.sin(n * omega_0 * T_0 / 4))


def fourier_series(t_array, d_n, omega_0):
    """Reconstructs a signal from its Fourier series.

    Parameters
    ----------
    t_array : ndarray
        time array
    b_n : ndarray
        b_n coefficients
    omega_0 : float
        fundamental frequency of the signal

    Returns
    -------
    ndarray
        reconstructed signal
    """
    sum_array = np.zeros_like(t_array)
    for dn in d_n:
        n = np.where(d_n == dn)[0][0]
        sum_array += dn * np.exp(1j * n * omega_0 * t_array)
    return sum_array

def H(s):
    R = 1000
    C = 0.033e-6
    L = 1e-3
    top = s / (R * C)
    bot = s*s + s / (R * C) + 1 / (L * C)
    return top / bot

def system_response(t_array, d_n, omega_0):
    sum_array = np.zeros_like(t_array)
    for dn in d_n:
        n = np.where(d_n == dn)[0][0]
        sum_array += H(1j * n * omega_0) * dn * np.exp(1j * n * omega_0 * t_array)
    return sum_array
