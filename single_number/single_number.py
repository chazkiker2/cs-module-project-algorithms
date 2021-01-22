'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from functools import reduce


def single_num_chaz(arr):
    # reduce(fn_to_execute, iterable_to_iterate, optional_seed_value)
    return reduce(lambda x, y: x ^ y, arr, 0)


def single_num_doc(arr):
    """Thank you @Doc"""
    ans = 0

    for x in arr:
        ans ^= x  # bitwise xor equals

    # INFO ABOUT ^= xor
    # (a ^= b) is the same as (a = a ^ b)
    # exclusive or (or "xor")
    # xor(a, b) -> return (a and not b) or ((not a) and b)
    # a^b = (a + b) % 2
    # for every time an int

    return ans


def single_number(arr):
    """THIS IS NOT A GREAT SOLUTION, BUT IT'S WHERE WE GOT"""
    # start with a dict
    dic = {}

    # loop through input arr
    for num in arr:
        # if num in dict: delete
        if dic.get(num):  # dic.get(x) returns None if num is not in dict
            del dic[num]

        # if it is NOT in dict, initialize that value
        else:
            dic[num] = 1

    return next(iter(dic.keys()))  # O(n) — return the first el in iteration of dic.keys()

    # fastest fix: if not dic[num] (lookup)

    # loop through dict for wherever the value is 1
    # for key in dic:
    #     if dic[key] == 1:
    #         # return the key in dict where value is 1
    #         return key


# REFLECT on FIRST PASS
# Time complexity -> O(n^2)
# possible improvements:
# - take num of `for` loops from 3 to... 1
#   - potential solution would be a clean dict comprehension


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_num_chaz(arr)}")
