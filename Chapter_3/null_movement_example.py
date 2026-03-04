import numpy as np
from numpy import pi
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# Parameters
spacing = 0.5 # d=lambda/2
angle = np.arange(-90, 90.1, 0.1) # Angle range in degrees (include +90 like MATLAB)
root_radius = 1.0 # Use 1.0 for exact nulls in angle-domain AF (1.2 pushes roots off unit circle)

# Determine positions where you want nulls to be
nulls_psi = np.deg2rad(np.array([60, -60, 90, -120, 180])) # Convert null angles to radians
nulls_z = root_radius*np.exp(1j*nulls_psi) # Convert null angles to complex numbers
print("Nulls in z-domain:", nulls_z)

# Functions
def weight_conv(varargin):
    # convolves binomials together, input in form ([1 0], [4 5], ...)
    weights = 1
    print("length of varargin:", len(varargin))
    for ii in range(0, len(varargin)):
        weights = np.convolve(weights, varargin[ii])
    return weights

def z_term(spacing, angle):
    # calculates z for a given distance (in wavelengths) and angle (in degrees)
    return np.exp(1j * 2 * pi * spacing * np.sin(np.deg2rad(angle)))

# Calculations
# for plotting and conversion ease
nulls_theta = np.degrees(np.arcsin(nulls_psi/pi)) # Convert null angles to degrees for plotting

# Make binomial coefficients and multiply
terms = np.empty((nulls_psi.size, 2), dtype=complex) # Create empty array to hold complex binomial terms
for ii in range(0, nulls_psi.size):
    terms[ii] = [1, -nulls_z[ii]] # Binomial term for each null, in form [1, -z_null] which corresponds to (1 - z_null*z^-1)

print("Binomial terms:", terms)

weights = weight_conv(terms) # Normalize the weights

# Add each polynomial term to make full Array Factor
# this is only based on wegihts and phases

AF = 0
N_weights = weights.size
for ii in range(0, N_weights):
    AF = AF + weights[ii]*z_term(spacing, angle)**(N_weights-ii-1)

# Print results
print("Null positions (psi):", nulls_psi)
print("Null positions (theta):", nulls_theta)
print("Weight magnitudes:", np.abs(weights))
print("Weight phases (degrees):", np.angle(weights, deg=True)) #rad2deg(atan2(imag(weights),real(weights))))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(angle, (abs(AF)), label='Array Factor')
plt.plot(nulls_theta, np.zeros_like(nulls_theta), 'rx', label='Nulls')
plt.xlabel('Angle (degrees)')
plt.ylabel('Array Factor Magnitude')
plt.title('Array Factor with Nulls')
plt.legend()
plt.grid(True)
plt.show()
