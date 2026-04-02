import numpy as np
import matplotlib
import scipy.integrate

# define AP
def AP(theta):
    return np.sin(theta)

# solve for max directivity
integrand = lambda th, phi: np.abs(AP(th))**2 * np.sin(th)

D_max =(4 * np.pi) / scipy.integrate.dblquad(integrand, 0, np.pi, 0, 2*np.pi)[0]


print("Maximum Directivity:", D_max)