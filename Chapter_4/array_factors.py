import numpy as np
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

spacings = np.array([0.5, 1.0, 2.0]) # Element spacing in wavelengths
N = 8 # num elements

theta = np.linspace(-90, 90, 1000) # Angle range in degrees
theta_rad = np.radians(theta)

plt.figure(figsize=(12, 6))

for spacing in spacings:
    # Calculate psi phase shift
    # phi = k * d * sin(theta)
    k = 1 # constant???
    phase = k * spacing * np.sin(theta_rad)

    # Caulculate non-normalized array factor
    array_factor = (np.abs(np.sin(N * phase / 2) / np.sin(phase / 2))) * np.exp(1j * ((N-1)/2) * phase)

    # Normalize
    array_factor = array_factor / np.max(array_factor)

    plt.plot(theta, 20 * np.log10(array_factor + 1e-10), label=f'Spacing = {spacing}λ')

plt.xlabel('Angle (degrees)')
plt.ylabel('Magnitude (dB)')
plt.title('Array Factor - 8 Element Uniform Antenna Array')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-90, 90)
plt.show()