import numpy as np
def search_in_matrix(matrix, target):

    a = np.array(matrix)
    b = np.where(a == target)
    print([b])
    if np.isin(target, matrix) == False:
        print([-1, -1])


matrix = [
    [1, 4, 7, 120, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]]

print(search_in_matrix(matrix, 103))
#print(search_in_matrix(matrix, 16))
#output [-1, -1]

