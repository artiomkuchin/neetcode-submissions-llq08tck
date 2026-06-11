from typing import List

# 1
# Return Index of first occurance of number 7
# If number 7 is not found return -1

#2
# Return distance between first and second occurance of num 7
# Assume atleast 2 occurances of 7
# Find index of each and subtract one from the other

def get_index_of_seven(nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if num == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_i = -1 # memory empty

    for i, num in enumerate(nums):
        if num == 7:   #
            if first_i == -1:  # Have we seen 7 before?
                first_i = i    # first memory of 7
            else:
                return i - first_i


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
