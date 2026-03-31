# NumPy(Numerical Python) is a library for fast mathematical operations
# it provides the ndarry (N-dimensional arrray) whichh is way faster than python lists
# it is used for -> arrays and matrics , mathematical operations(mean ,sum, std and etc)
# linear algebra and data preprocessing before pandas/ML

#  Core feartures of numPY

# Ndarry (N -dimensional array) -> fast, flexible data structure
# vectorized operations -> perform math on entire arrays without loops
# Broadcasting -> automatic expansion of arrays for operations 
# Linear algebra -> matrix multiplication, eigenvalues, etc 
# Random module -> random numbers, distributions
# Integration with pandas, scikit-learn, TensorFlow -> Backbone of ML/AI
# Example: creating arrays

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type:", type(arr))
print("Shape:", arr.shape)

# Example : Array operations  
arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Example: matrix operations 

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", A + B)
print("A x B:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)

# Example: userful functions 
arr = np.arange(1, 11) 
print("Array:", arr)
print("Even numbers:", arr[arr % 2 == 0])
print("Sqaures:", np.square(arr))
print("Sqrt:", np.sqrt(arr))

# Example: Broadcasting 

arr = np.array([1, 2, 3])
print("Add Scalar:", arr + 4)
print("Multiply scalar: ", arr + 2)

# Example: Random Numbers

rand_arr = np.random.randint(1, 100, size=(5,))
print("Random Array:", rand_arr)

rand_matrix = np.random.rand(3, 3)
print("Random Matrix:\n", rand_matrix)

# Example of mean, median and mode 
import numpy as np 


data = np.array([10, 20, 20, 30, 40, 40, 40, 50])
mean_value = np.mean(data)
median_value = np.median(data)
# mode_value = stats.mode(data, keepdims=True)

print("Data:", data)
print("Mean:", mean_value)
print("Median:", median_value)
# print("Mode:", mode_value)