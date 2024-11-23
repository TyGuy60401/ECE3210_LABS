import numpy as np
import matplotlib.pyplot as plt


w = np.linspace(-2*np.pi, 2*np.pi, 10000)
x = np.ones(9)
X = np.sin(4.5 * w) / np.sin(0.5 * w) * np.exp(-1j * 4 * w)

X_fft_9 = np.fft.fft(x)
w_fft_9 = np.arange(len(X_fft_9)) * 2 * np.pi / len(X_fft_9)

X_fft_16 = np.fft.fft(x, n=16)
w_fft_16 = np.arange(len(X_fft_16)) * 2 * np.pi / len(X_fft_16)

X_fft_128 = np.fft.fft(x, n=128)
w_fft_128 = np.arange(len(X_fft_128)) * 2 * np.pi / len(X_fft_128)

plt.figure()
plt.plot(w, X.real)
plt.stem(w_fft_9, X_fft_9.real, linefmt="g", markerfmt="go", label="9-pt")
plt.stem(w_fft_16, X_fft_16.real, linefmt="r", markerfmt="ro", label="16-pt")
# plt.stem(w_fft_128, X_fft_128.real, linefmt="r", markerfmt="r.", label="128-pt")
plt.show()

plt.figure()
plt.plot(w, X.imag)
plt.stem(w_fft_9, X_fft_9.imag, linefmt="g", markerfmt="go", label="9-pt")
plt.stem(w_fft_16, X_fft_16.imag, linefmt="r", markerfmt="ro", label="16-pt")
plt.show()
