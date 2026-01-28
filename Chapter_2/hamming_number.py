import numpy as np

# Create two arrays as specified
string_a = np.append(np.arange(1, 8), [0, 2])
string_b = np.arange(1, 10)

print("String A:", string_a)
print("String B:", string_b)

# Compute Hamming distances
hamming_distance = np.sum(string_a != string_b)
print("Hamming Distance:", hamming_distance)

