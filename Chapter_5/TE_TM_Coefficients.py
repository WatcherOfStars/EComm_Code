import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QtAgg') 

# vars
n_i = 1.5 # initial refractive index
n_t = 1.0 # target refractive index
theta_i = np.arange(0, 90, 1) # angles of incidence in degrees

# calculate thetas
theta_i_rad = np.radians(theta_i)
theta_t_rad = np.arcsin((n_i / n_t) * np.sin(theta_i_rad)) # snell's law
print("Theta_i (radians):", theta_i_rad)
print("Theta_t (radians):", theta_t_rad)

# calculate TE and TM coefficients
# fresnel reflection
fresnel_TM = (n_t * np.cos(theta_i_rad) - n_i * np.cos(theta_t_rad)) / (n_t * np.cos(theta_i_rad) + n_i * np.cos(theta_t_rad))
fresnel_TE = (n_i * np.cos(theta_i_rad) - n_t * np.cos(theta_t_rad)) / (n_i * np.cos(theta_i_rad) + n_t * np.cos(theta_t_rad))

# fresnel transmission
T_fresnel_TM = 1 - fresnel_TM
T_fresnel_TE = 1 - fresnel_TE

# display results as table
print(f"{'Angle (degrees)':<20} {'Fresnel TM':<20} {'Fresnel TE':<20} {'Transmission TM':<20} {'Transmission TE':<20}")
for i in range(len(theta_i)):
    print(f"{theta_i[i]:<20} {fresnel_TM[i]:<20f} {fresnel_TE[i]:<20f} {T_fresnel_TM[i]:<20f} {T_fresnel_TE[i]:<20f}")

# plot results
plt.figure(figsize=(12, 6))
plt.plot(theta_i, fresnel_TM, label='Fresnel TM Reflection Coefficient')
plt.plot(theta_i, fresnel_TE, label='Fresnel TE Reflection Coefficient')
plt.plot(theta_i, T_fresnel_TM, label='Fresnel TM Transmission Coefficient')
plt.plot(theta_i, T_fresnel_TE, label='Fresnel TE Transmission Coefficient')
plt.xlabel('Angle of Incidence (degrees)')
plt.ylabel('Coefficient Value')
plt.title('Fresnel Coefficients vs Angle of Incidence')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(0, 90)
plt.show()