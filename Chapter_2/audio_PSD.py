from audio2numpy import open_audio
import os
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt
import numpy as np

# Needed mono function
def stereo_to_mono_numpy(stereo_array):
    if stereo_array.ndim != 2 or stereo_array.shape[1] != 2:
        raise ValueError("Input array must be 2D with shape (num_samples, 2)")

    # Average the channels
    mono_array = np.mean(stereo_array, axis=1)
    
    return mono_array


# Get audio signal and sample rate
file_path = "Chapter_2/mass_audio.mp3"
if os.path.exists(file_path):
    signal, sampling_rate = open_audio(file_path)
    signal = stereo_to_mono_numpy(signal) #convert to mono for easier graphing
    print(f"Sampling rate: {sampling_rate} Hz")
    #print(f"Signal: {signal}")
    print(f"Signal shape: {signal.shape}")
    print(f"Signal dtype: {signal.dtype}")
else:
    print(f"Error: File not found at {file_path}")

#get number of samples
N = signal.size

# FFT of audio
sig_fft = np.fft.fft(signal)

# get single-sided psd
# psd = np.abs(sig_fft)**2 / (sampling_rate*N)
psd = (1/N) * np.abs(sig_fft)**2

# convert to dB/Hz
psd = 10 * np.log10(psd)

# get frequency axis
f_axis = np.fft.fftfreq(N, 1/sampling_rate)

#shift
f_axis = np.fft.fftshift(f_axis)
psd = np.fft.fftshift(psd + 30) #+30 for dBm

# Plot
plt.figure(figsize=(8, 5))
plt.plot(f_axis, psd)
plt.title('PSD')
plt.xlabel('Frequency (Hz)')
plt.ylabel('dBm / Hz')
plt.grid(True)
plt.show()
