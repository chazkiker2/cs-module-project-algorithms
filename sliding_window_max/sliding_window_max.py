'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # nums = list of ints
    # k = int (size of window)

    # - create return list to track largest nums
    max_values = []

    # - look through first k numbers
    for i in range(len(nums) - k + 1):  # every index up until length - k
        max_values.append(max(nums[i:i+k]))

    return max_values
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
