import numpy as np
from numpy import pi
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

t = np.arange(0, 1650)*1e-7 # Time vector
print (t) # Print the time vector to verify its contents
message = np.cos(2*pi*10e3*t) # Message signal (10 kHz)
car = np.cos(2*pi*300e3*t) # Carrier signal (300 kHz)
bAM = 0.33 # Modulation index
vAM = (1 + bAM*message) * car # AM signal

plt.figure(figsize=(10, 12))
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title('Message Signal (10 kHz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, car)
plt.title('Carrier Signal (300 kHz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, vAM)    
plt.title('AM Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()

plt.show()