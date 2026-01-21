import numpy as np
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

# Plot characteristic impedance of twin wire transmission line vs s/d. Wires enclosed in polyethylene .

# Consts
permeability_free_space = 4 * np.pi * 1e-7  # Free space permeability (H/m)
permittivity_free_space = 8.854e-12  # Free space permittivity (F/m)

# Params for dielectric
permeability_rel = 1.0  # Relative permeability for polyethylene (https://www.rolling-components.com/wp-content/uploads/2017/05/PE_E.pdf)
permittivity_rel = 2.3  # Relative permittivity for polyethylene (https://www.engineeringtoolbox.com/relative-permittivity-d_1660.html)

mu = permeability_rel * permeability_free_space
epsilon = permittivity_rel * permittivity_free_space

# Params for diameters: https://www.pasternack.com/images/ProductPDF/RG58C-U.pdf
inner_diameter = 0.91  # Inner diameter (mm) 
outer_diameter = 3.51  # Outer diameter (mm)

# Impeacdance calculation function
def characteristic_impedance(outer_dia, inner_dia):
    Zc = np.sqrt(mu/epsilon) * (1/(2*np.pi)) * np.log(outer_dia/inner_dia) #np.log is natural log
    return Zc

# print out
Zc = characteristic_impedance(outer_diameter, inner_diameter);
print("Characteristic Impedance Zc:", Zc)