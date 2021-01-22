'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque

# doc challenge
def sliding_window_max_docs(nums, k):
    # Use Deque on this
    # create empty list for max(
    maxes = []
    dq = deque()
    # while loop inside for loop WorstCase=O(n^2)
    # pop in while loop
    #
    # need to invoke: pop(), append(), and pop_left()
    # instead of using range(), use enumerate()

    return None


def sliding_window_max(nums, k):
    max_values = [0] * (len(nums) - k + 1)

    for i in range(len(nums) - k + 1):  # every index up until length - k
        max_values[i] = max(nums[i:i + k])

    return max_values


# nums = list of ints
# k = int (size of window)

# - create return list to track largest nums
# max_values = [0 for _ in nums]
# - look through first k numbers
# - then find out which of those numbers is largest
# - add largest number to empty list
# repeat via iterating through whole list taking k numbers at a time
# grab largest num from each k set and append to return list

# return list


# ONE improvement worth making: appending is not fast

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
