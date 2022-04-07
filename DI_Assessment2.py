def TwoSum(my_array, target_sum):
    for x in range(len(my_array) - 1):
        for y in range(x + 1, len(my_array)):
            if my_array[x] + my_array[y] == target_sum:
                print([my_array[x], my_array[y]])
            else:
                print([])



my_array = [3, 5, 2, -4, 8, 11]
target_sum = 7

TwoSum(my_array, target_sum)
