# Assignment-5, Cognitive Computing UCS420
# NumPy Introduction-1
# Nilabh Kishore Gupta

import numpy as np

# Q1. create a 1D array with 5 elements, a) add 2 b) multiply 3 c) divide by 2
arr1 = np.array([10, 20, 30, 40, 50])
print("array:", arr1)
print("add 2:", arr1 + 2)
print("multiply 3:", arr1 * 3)
print("divide 2:", arr1 / 2)

# Q2a. reverse the array
arr = np.array([1, 2, 3, 6, 4, 5])
print("\nreversed:", arr[::-1])

# Q2b. most frequent value and its indices, for x and y
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

counts_x = np.bincount(x)
mode_x = np.argmax(counts_x)
print("\nx mode:", mode_x, "at indices", np.where(x == mode_x)[0])

counts_y = np.bincount(y)
mode_y = np.argmax(counts_y)
print("y mode:", mode_y, "at indices", np.where(y == mode_y)[0])

# Q3. 2-D array, access row/col
arr2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\n1st row 2nd col:", arr2d[0, 1])
print("3rd row 1st col:", arr2d[2, 0])

# Q4. 1D array named after me, 25 evenly spaced numbers from 10 to 100
nilabh = np.linspace(10, 100, 25)
print("\narray:", nilabh)
print("ndim:", nilabh.ndim)
print("shape:", nilabh.shape)
print("size:", nilabh.size)
print("dtype:", nilabh.dtype)
print("nbytes:", nilabh.nbytes)

transposed = nilabh.reshape(25, 1)
print("transpose using reshape:\n", transposed)
# a 1-D array has only one axis, so .T just gives back the same array, no real transpose happens
print("using .T (no change for 1D array):", nilabh.T.shape)

# Q5. 2-D array 3x4 named ucs420_nilabh
ucs420_nilabh = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print("\nmean:", np.mean(ucs420_nilabh))
print("median:", np.median(ucs420_nilabh))
print("max:", np.max(ucs420_nilabh))
print("min:", np.min(ucs420_nilabh))
print("unique:", np.unique(ucs420_nilabh))

reshaped_ucs420_nilabh = ucs420_nilabh.reshape(4, 3)
print("\nreshaped to 4x3:\n", reshaped_ucs420_nilabh)

resized_ucs420_nilabh = np.resize(ucs420_nilabh, (2, 3))
print("\nresized to 2x3:\n", resized_ucs420_nilabh)
