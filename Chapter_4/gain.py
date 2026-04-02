import numpy as np
import matplotlib
import scipy.integrate

# define AP
def AP(theta):
    if(theta < 0 or theta > 2*np.pi):
        return 0
    else:
        return np.sin(5*np.pi*theta) / (np.pi*np.sin(theta))

# find max AP
max_AP = 0
for theta in np.linspace(0, 2*np.pi, 1000):
    max_AP = max(max_AP, np.abs(AP(theta)))
print("Maximum AP:", max_AP)

# solve for omega p
integrand = lambda th, phi: AP(th) / max_AP
omega_p = scipy.integrate.dblquad(integrand, 0, np.pi, 0, 2*np.pi)[0]

# find gain
efficiency = 0.95  # Example efficiency value
G = (4 * np.pi / omega_p) * efficiency
print("Gain:", G)