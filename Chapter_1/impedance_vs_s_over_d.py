import numpy as np
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

# Plot characteristic impedance of twin wire transmission line vs s/d. Wires enclosed in polyethylene .

# Consts
permeability_free_space = 4 * np.pi * 1e-7  # Free space permeability (H/m)
permittivity_free_space = 8.854e-12  # Free space permittivity (F/m)

# Params for polyethylene
permeability_rel = 1.0  # Relative permeability for polyethylene (https://www.rolling-components.com/wp-content/uploads/2017/05/PE_E.pdf)
permittivity_rel = 2.3  # Relative permittivity for polyethylene (https://www.engineeringtoolbox.com/relative-permittivity-d_1660.html)

# Impeacdance calculation function
def characteristic_impedance(s_over_d):
    mu = permeability_rel * permeability_free_space
    epsilon = permittivity_rel * permittivity_free_space
    Zc = np.sqrt(mu/epsilon) * (1/np.pi) * np.arccosh(s_over_d) #think i got this right
    return Zc

# s/d range
s_over_d = np.linspace(1, 10, 500)
Zc = characteristic_impedance(s_over_d);

# Plot
print("s/d range:", s_over_d)
print("Characteristic Impedance Zc:", Zc)

plt.figure(figsize=(10, 6))
plt.plot(s_over_d, Zc, label='Characteristic Impedance')
plt.xlabel('s/d')
plt.ylabel('Characteristic Impedance [Ohms]')
plt.title('Characteristic Impedance vs s/d for Twin Wire Transmission Line in Polyethylene')
plt.grid(True)
plt.legend()
plt.show()