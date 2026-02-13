import numpy as np
from scipy.special import jn

beta_fm = input("Enter the frequency modulation index (β_fm): ") # get modulation index
beta_fm = float(beta_fm)

A_bessel = jn(np.arange(1, 30), beta_fm) # bessel function for 1 to 30
n_significant = np.sum(A_bessel > 0.01) # count significant amplitudes
n_bands = n_significant*2 - 1 # calculate number of bands
print(f"{n_bands} significant sidebands with modulation index {beta_fm:.2f}")

rel_bandwidth = n_bands # bandwidth relative to the message frequency
print(f"Bandwidth = {rel_bandwidth} * f_m")

rel_carson_bandwidth = 2 * (beta_fm + 1) # carson's rule
print(f"Carson's Bandwidth = {rel_carson_bandwidth:.2f} * f_m")