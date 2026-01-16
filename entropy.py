import numpy as np

# Get user input for probabilities
p_input = input("Enter percents separated by spaces: ")
input_list = p_input.split() # Splits the string into a list of strings
p = np.array(input_list, dtype=float) #probability array

# Get user input for instances (numbers of occurrences)
r_input = input("Enter number of instances separated by spaces: ")
input_list = r_input.split() # Splits the string into a list of strings
r = np.array(input_list, dtype=float) #instance number array

# Calculate information content
I = np.log2(1/(p/100))

# Calculate entropy
H = np.sum(r * (p/100 * I))

# Display results
print ("Probabilities p:", p)
print("Information Content I:", I)
print("Entropy H:", H)