# 2400 MHz, brick wall 267 mm, signal travels 20m in building

import numpy as np

#params
L_0 = 40.2 # loss at reference distance (dB)
d_0 = 1 # reference distance (m)
d = 20 # distance (m)
L_wall = 5 # loss of wall (dB)
L_floor = 14 # loss of floor (dB)
gamma = 2 # i think this is right

#calculate path loss using motley-keenan model
L = L_0 + 10 * gamma * np.log10(d/d_0) + L_wall + L_floor
print(f"Path loss: {L:.2f} dB")