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


# Graph audio
#create time axis, end time is number of samples / sample rate
time_axis = np.linspace(0, signal.size / sampling_rate, signal.size)

# Plot
print("times:", time_axis)
print("Signal:", signal)

plt.figure(figsize=(10, 6))
plt.plot(time_axis, signal, label='MP3 File')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('MP3 file voltage over time')
plt.grid(True)
plt.legend()
plt.show()
