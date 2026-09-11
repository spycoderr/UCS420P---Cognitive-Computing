# Assignment-6, Cognitive Computing UCS420
# NumPy-II
# Nilabh Kishore Gupta

import numpy as np

# Q1. sensor readings, sensor has +2C error, do without using for loop
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

corrected = temperature + 2
print("corrected temp:", corrected)

fahrenheit = (9 / 5) * temperature + 32
print("in fahrenheit:", fahrenheit)

above_32 = temperature[temperature > 32]
print("readings above 32:", above_32)

print("count above 32:", above_32.size)

# vectorization runs the operation on the whole array at once (numpy uses c loops internally)
# instead of a python level for loop, so it is much faster for large arrays.
# boolean indexing works the same way, it filters the array in one go instead of
# checking condition for every element one by one.


# Q2. steps matrix, four users, three days
steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("\ntotal steps:", steps.sum())
print("mean steps:", steps.mean())
print("max:", steps.max(), " min:", steps.min())
print("total per day (axis=0):", steps.sum(axis=0))
print("total per user (axis=1):", steps.sum(axis=1))

max_pos = np.unravel_index(np.argmax(steps), steps.shape)
print("user/day with max steps:", max_pos)


# Q3.
original = np.array([1, 2, 3, 4, 5, 6])

subset = original[1:5]
subset[0] = 999
print("\noriginal after subset change:", original)
print("subset:", subset)

original = np.array([1, 2, 3, 4, 5, 6])   # resetting since previous slice modified it
copy_slice = original[1:5].copy()
copy_slice[0] = 500
print("original after copy change:", original)
print("copied array:", copy_slice)

mat = np.arange(1, 13).reshape(3, 4)
print("\n3x4 matrix:\n", mat)
print("first row:", mat[0])
print("last row:", mat[-1])
print("second column:", mat[:, 1])
print("rows 1-2, cols 2-3:\n", mat[1:3, 2:4])

flat1 = mat.flatten()
flat2 = mat.ravel()
print("\nflatten:", flat1)
print("ravel:", flat2)

flat2[0] = 111
print("after changing ravel, original matrix:\n", mat)   # ravel gives a view, so original changes

flat1[0] = 222
print("after changing flatten, original matrix:\n", mat)   # flatten gives a copy, original stays same

print("\nshape:", mat.shape, " ndim:", mat.ndim, " size:", mat.size, " dtype:", mat.dtype)


# Q4. predicting assistance score
X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])
y = np.array([40, 65, 30, 85])

print("\nshape of X:", X.shape, " ndim:", X.ndim)

Xt = X.T
print("transpose:\n", Xt)
# transpose just flips rows and columns, so now each row is one feature (sleep, activity, stress)
# and each column is one user, instead of the other way around

XtX = Xt @ X
print("X.T @ X:\n", XtX)

XtX_inv = np.linalg.inv(XtX)
print("inverse of X.T @ X:\n", XtX_inv)

beta = XtX_inv @ Xt @ y
print("coefficients (beta):", beta)
# these coefficients tell how much the assistance score changes per unit change in
# sleep hours, activity level and stress level respectively

new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print("predicted score for new user:", predicted_score)
