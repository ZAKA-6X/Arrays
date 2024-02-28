# Array Operations with NumPy:

Arrays are fundamental data structures used to store and manipulate collections of elements efficiently. NumPy provides a convenient way to work with arrays in Python, offering a wide range of functions and methods for array manipulation and computation.
Getting Started

To use NumPy, first, ensure you have it installed. You can install NumPy using pip:

    pip install numpy

Once installed, you can import NumPy into your Python script:

    import numpy as np

# Array Operations
## 1. Creating an Array

You can create an array using the np.array() function. Specify the elements of the array within a list:

    my_array = np.array([1, 2, 3, 4, 5], dtype=np.float64)

## 2. Modifying Elements

You can modify individual elements of an array by accessing them using their indices:

    my_array[0] = 7

## 3. Inserting and Deleting Elements

Use np.insert() to add elements at a specific index and np.delete() to remove elements:

    my_array = np.insert(my_array, 0, 33)
    my_array = np.delete(my_array, 0)

## 4. Searching for an Element

Define a function to search for an element within an array:

    def search(array, element):
        index = np.where(array == element)
        if len(index[0]) > 0:
            print(index[0][0])
        else:
            print('-1')

## 5. Arithmetic Operations

Perform arithmetic operations on arrays, such as addition, subtraction, multiplication, and division:

    sum_arrays = array1 + array2

## 6. Statistical Operations

Compute statistical properties of arrays, such as maximum, minimum, mean, median, and standard deviation:

    maxi = np.max(my_array)
    mini = np.min(my_array)
    mean = np.mean(my_array)
    median = np.median(my_array)*
    std = np.std(my_array)

## 7. Sorting and Flipping

Sort and flip arrays:

    sort = np.sort(my_array)
    flip = np.flip(my_array)

## 8. Matrix Operations

Perform matrix operations like multiplication and transpose:

    multi = np.dot(matrix1, matrix2)
    trans = np.transpose(matrix2)
