import numpy as np
from numpy import pi
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

t = np.arange(0, 1000)*1e-7 # Time vector
#print (t) # Print the time vector to verify its contents
message = np.cos(2*pi*10e3*t) # Message signal (10 kHz)
bFM = np.array([0.67,5,10]) # Modulation indecies to test
vFM = np.cos(2*pi*300e3*t + bFM[:,None]*message) # FM signal

plt.figure(figsize=(10, 12))
plt.subplot(4, 1, 1)
plt.plot(t, message)
plt.title('Message Signal (10 kHz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, vFM[0])    
plt.title('FM Modulated Signal (bFM = 0.67)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, vFM[1])    
plt.title('FM Modulated Signal (bFM = 5)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, vFM[2])    
plt.title('FM Modulated Signal (bFM = 10)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.tight_layout()

plt.show()