# we use NumPy Pack to make an array:

import numpy as np

# ------Synthax of an array ------
my_array = np.array([1,2,3,4,5], dtype = np.float64)

# ------ Modify an array's element ------
my_array[0] = 7

# ------ Isert in an array ------
my_array = np.insert(my_array,0,33)

# ------ Deleete an element ------
my_array = np.delete(my_array, 0) # [index]
print(my_array)

# ------Search an element ------
def search(array, element):
    index = np.where(array == element)
    if len(index[0]) > 0:
        print(index[0][0])
    else:
        print('-1')

# ------ Sum two arrays ------
array1 = np.array([1,2,3,4,5])
array2 = np.array([4,5,6,7,4])
sum_arrays = array1 + array2

# ------ Min and Max element ------
maxi = np.max(my_array)
mini = np.min(my_array)

# ------ Sort an array ------
sort = np.sort(my_array)

# ------ Flip an array -------
flip = np.flip(my_array)

# ------ Mean and Median od an array ------
mean = np.mean(my_array)
median = np.median(my_array)

# ------ Standard deviation ------
std = np.std(my_array)

# ------ Matrix ------
matrix1 = np.array([[1,4,5],[7,8,9],[1,4,6]])
matrix2 = np.array([[1,4],[5,7],[54,24]])

# ------ Multiplication of matrix ------
multi = np.dot(matrix1, matrix2)

# ------ Transpose the matrix ------
trans = np.transpose(matrix2)

