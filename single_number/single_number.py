'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # start with a dict
    dic = {}

    # loop through input arr
    for num in arr:
        # if num not in dict: make a new key there equal to 1 (acting as counter)
        if num not in dic:  # this could be refactored for faster time complexity
            dic[num] = 1

        # if it IS in dict: increase count
        else:
            dic[num] += 1

        # fastest fix: if not dic[num] (lookup)

    # loop through dict for wherever the value is 1
    for key in dic:
        if dic[key] == 1:
            # return the key in dict where value is 1
            return key

# REFLECT on FIRST PASS
# Time complexity -> O(n^2)
# possible improvements:
# - take num of `for` loops from 3 to... 1
#   - potential solution would be a clean dict comprehension


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
