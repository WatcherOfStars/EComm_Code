import numpy as np
from scipy.special import sinc

import matplotlib.pyplot as plt

# Parameters
freq = 10e9  # 10 GHz
c = 3e8  # Speed of light
wavelength = c / freq
k = 2 * np.pi / wavelength

# Aperture dimensions
aperture_width = 0.12  # 12 cm in meters
aperture_height = 0.06  # 6 cm in meters

# Observation plane
distance_to_screen = 0.20  # 20 cm in meters
observation_area = 2.0  # 2m x 2m area

# Create observation grid
x = np.linspace(-observation_area/2, observation_area/2, 256)
y = np.linspace(-observation_area/2, observation_area/2, 256)
X, Y = np.meshgrid(x, y)

# Distance from aperture center to observation points
R = np.sqrt(X**2 + Y**2 + distance_to_screen**2)

# Angles for far-field approximation
sin_theta_x = X / R
sin_theta_y = Y / R

# Rectangular aperture antenna pattern (sinc function)
# Field pattern for uniform aperture distribution
u = (k * aperture_width / 2) * sin_theta_x
v = (k * aperture_height / 2) * sin_theta_y

# Avoid division by zero
with np.errstate(divide='ignore', invalid='ignore'):
    E_field = np.sinc(u / np.pi) * np.sinc(v / np.pi)
    E_field = np.nan_to_num(E_field, nan=1.0)

# Normalize to maximum value
E_field = E_field / np.max(np.abs(E_field))

# Convert to dB
E_field_dB = 20 * np.log10(np.abs(E_field) + 1e-10)

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Linear scale
im1 = ax1.contourf(X, Y, np.abs(E_field), levels=20, cmap='viridis')
ax1.set_xlabel('X (m)')
ax1.set_ylabel('Y (m)')
ax1.set_title(f'Antenna Pattern - Linear Scale\n12cm x 6cm aperture at 10 GHz')
ax1.set_aspect('equal')
plt.colorbar(im1, ax=ax1, label='Normalized Amplitude')

# dB scale
im2 = ax2.contourf(X, Y, E_field_dB, levels=20, cmap='viridis', vmin=-40, vmax=0)
ax2.set_xlabel('X (m)')
ax2.set_ylabel('Y (m)')
ax2.set_title(f'Antenna Pattern - dB Scale\n20cm from aperture, 2m x 2m area')
ax2.set_aspect('equal')
plt.colorbar(im2, ax=ax2, label='Amplitude (dB)')

plt.tight_layout()
plt.savefig('projection_AP.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Wavelength: {wavelength*100:.2f} cm")
print(f"Aperture size: {aperture_width*100:.1f}cm x {aperture_height*100:.1f}cm")
print(f"Observation distance: {distance_to_screen*100:.1f}cm")