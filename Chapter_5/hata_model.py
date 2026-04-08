import numpy as np


def hata_model(ht, hr, d, f, setting):
	"""
	Hata model path loss (dB).

	Parameters
	- ht: transmitter height in meters
	- hr: receiver height in meters
	- d: distance in meters
	- f: frequency in Hz
	- setting: environment string (e.g. 'M','C','S','R' or 'Metro','City','Suburban','Rural')

	Returns
	- path loss in dB (float or numpy array matching input shapes)
	"""
	f = np.asarray(f) / 1e6  # MHz
	d = np.asarray(d) / 1e3  # km

	s = str(setting).strip().lower()
	if s in ("m", "huge", "metro", "metropolitan"):
		# Metropolitan case: different a depending on frequency ranges
		if np.all(f <= 200):
			a = 8.29 * (np.log10(1.54 * hr)) ** 2 - 1.1
		elif np.all(f >= 400):
			a = 3.2 * (np.log10(11.75 * hr)) ** 2 - 4.97
		else:
			raise ValueError(
				"Metropolitan environments in this frequency range require more complexity in the Hata Model"
			)
		C = 0.0

	elif s in ("c", "city", "medium city"):
		a = (1.1 * np.log10(f) - 0.7) * hr - 1.56 * np.log10(f) + 0.8
		C = 0.0

	elif s in ("s", "sub", "suburb", "suburban"):
		a = (1.1 * np.log10(f) - 0.7) * hr - 1.56 * np.log10(f) + 0.8
		C = -2 * (np.log10(f / 28.0)) ** 2 - 5.4

	elif s in ("r", "rur", "rural"):
		a = (1.1 * np.log10(f) - 0.7) * hr - 1.56 * np.log10(f) + 0.8
		C = -4.78 * (np.log10(f)) ** 2 + 18.33 * np.log10(f) - 40.94

	else:
		raise ValueError(f"Unknown setting '{setting}'")

	A = 69.55 + 26.16 * np.log10(f) - 13.82 * np.log10(ht) - a
	B = 44.9 - 6.55 * np.log10(ht)

	loss = A + B * np.log10(d) + C

	# return a plain Python float for scalar inputs
	if loss.shape == ():
		return float(loss)
	return loss


# get vars from user input
ht = float(input("Enter transmitter height (m): "))     # transmitter height (m)
hr = float(input("Enter receiver height (m): "))       # receiver height (m)
d = float(input("Enter distance (m): "))   # distance (m)
f = float(input("Enter frequency (Hz): "))      # frequency (Hz)

# get hata loss in each setting
for setting in ["metro", "city", "suburban", "rural"]:
    print(f"Setting: {setting}")
    print("Loss (dB):", hata_model(ht, hr, d, f, setting))