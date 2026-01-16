import numpy as np
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

# --- 1. Signal Parameters ---
Fs = 1000  # Sampling frequency (samples per second)
T = 1.0    # Total time duration (seconds)
N = int(Fs * T) # Number of samples
t = np.linspace(0.0, T, N, endpoint=False) # Time vector

# --- 2. Create a Signal ---
# A signal composed of two sine waves at 50 Hz and 120 Hz
freq1 = 50.0
freq2 = 120.0
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t) #

# --- 3. Compute the FFT ---
# np.fft.fft computes the 1D DFT
yf = np.fft.fft(signal)

# Normalize the result by the number of samples
yf = yf / N

# --- 4. Get the Frequency Axis ---
# np.fft.fftfreq returns the frequency bins corresponding to the output of fft()
xf = np.fft.fftfreq(N, 1/Fs)

# --- 5. Plotting ---

# We only plot the positive frequencies for a real-valued signal, as the spectrum is symmetric
# We use slicing to get the first half of the frequency and amplitude data
xf_pos = xf[:N//2]
yf_pos = np.abs(yf[:N//2]) # np.abs gives the magnitude (amplitude)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(xf_pos, yf_pos, markerfmt=" ", basefmt="-b")
plt.title('Frequency Domain (DFT/FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(f)| (Amplitude)')
plt.xlim(0, Fs/2) # Limit to Nyquist frequency
plt.grid()

plt.tight_layout()
plt.show()