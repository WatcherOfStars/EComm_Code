import numpy as np
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

# define equation
def AP(theta):
    return np.sinc(10*np.sin(theta))

# Create theta range
theta = np.linspace(-np.pi/2, np.pi/2, 1000)
# Calculate AP values
AP_values = abs(AP(theta))

#calculate for dB
AP_dB = 20 * np.log10(np.abs(AP_values))

#convert theta and phi to rectangular coordinates
x = AP_values * np.cos(theta)
y = AP_values * np.sin(theta)

# Plot
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(theta, AP_values, 'b-', linewidth=2)
plt.grid(True)
plt.xlabel('Theta (radians)')
plt.ylabel('AP(Theta)')
plt.title('Antenna Pattern')

plt.subplot(3, 1, 2)
plt.plot(theta, AP_dB, 'r-', linewidth=2)
plt.grid(True)
plt.xlabel('Theta (radians)')
plt.ylabel('AP(Theta) dB')
plt.title('Antenna Pattern in dB')

plt.subplot(3, 1, 3)
plt.plot(x, y, 'g-', linewidth=2)
plt.grid(True)
plt.xlabel('X (rectangular)')
plt.ylabel('Y (rectangular)')
plt.title('Antenna Pattern in Rectangular Coordinates')

plt.tight_layout()
plt.show()