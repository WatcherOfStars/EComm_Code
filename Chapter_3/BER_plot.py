import numpy as np
from numpy import pi
from scipy.special import erfc
import matplotlib
matplotlib.use('QtAgg') 
import matplotlib.pyplot as plt

# BER for QPSK = Q(sqrt(2*Eb/N0))
# BER for 4-QAM = 2*Q(sqrt(2*Eb/N0))

# Define Q-function
def Q(z):
    return 0.5 * erfc(z / np.sqrt(2))

EbN0_dB = np.arange(0, 21, 1) # Eb/N0 range in dB

EbN0 = 10**(EbN0_dB/10) # Convert Eb/N0 from dB to linear scale

# Calculate BER for QPSK and 4-QAM
BER_QPSK = Q(np.sqrt(2*EbN0))
BER_4QAM = 2*Q(np.sqrt(2*EbN0))

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogy(EbN0_dB, BER_QPSK, 'o-', label='QPSK')
plt.semilogy(EbN0_dB, BER_4QAM, 's-', label='4-QAM')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BER vs Eb/N0 for QPSK and 4-QAM')
plt.legend()
plt.show()
