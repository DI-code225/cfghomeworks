#after a simple solution (in comments lower) didn't work, I added an empty list to append indeces there
def search_in_matrix(matrix, target):

        indices_list = []
        for list_index, list in enumerate(matrix):
            if target in list:
                for integer_index, integer in enumerate(list):
                    if target == integer:
                       indices_list.append(list_index)
                       indices_list.append(integer_index)
        if indices_list != []:
            return indices_list
        else:
            return [-1, -1]



print(search_in_matrix([
    [1, 4, 7, 120, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
], 8))


#simple solution, that didn't work
# def search_in_matrix(matrix, target):
#     for list_index, my_list in enumerate(matrix):
#         for integer_index, my_integers in enumerate(my_list):
#             if target in my_integers:
#                 print([list_index, integer_index])
#             else:
#                 return [-1, -1]