'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque


# doc challenge
def sliding_window_max_doc(nums, k):
    """@Doc's hints for anyone hoping to make an efficient solution"""
    # Use collections.deque on this (from collections import deque)
    # create empty list for max(
    maxes = []
    deq = deque(nums)
    # while loop inside for loop
    # pop in while loop

    # need to invoke: pop(), append(), and pop_left()
    # instead of using range(), use enumerate()

    for num in nums:
        count = 0
        while count < k:


    return None


def sliding_window_max(nums, k):
    """O(n^2) — could use improvement but definitely a very readable solution"""
    max_values = [0] * (len(nums) - k + 1)

    for i in range(len(nums) - k + 1):  # every index up until length - k
        # max() is O(n) and we stuck it in a for loop...
        # for loops are O(n)
        # the line below is the problem with our time complexity
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
