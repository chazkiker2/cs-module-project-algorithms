'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # overall goal: find the non-zero integers in
    # given List of integers

    for num in arr:
        # move each non-zero integer to the LEFT side of the array
        # move each zero integer to the RIGHT side of the array

        if num != 0:
            # don't move number right so leave num on left
            # (or alternatively move num left)
            continue

        else:  # num is 0
            # move num right
            arr.append(num)  # add duplicate of num to end of list
            arr.remove(num)  # remove the first instance of num (leftmost instance)

    # final objective: return the sorted List of integers
    return arr

# REFLECTING ON FIRST PASS
# white-boarding is all about showing how you think
#
# Alternative solution: make a results_arr and eventually modify arr by changing arr to results_arr
#
# First pass was pretty efficient, only a couple of details worth changing:
# - append and remove are not the most efficient



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr1 = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr1)}")
