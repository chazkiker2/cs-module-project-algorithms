'''
Input: a List of integers
Returns: a List of integers
'''
from math import prod


def product_of_all_other_numbers(arr):
    products = [0 for _ in range(len(arr))]
    product_so_far = 1

    for i in range(len(arr)):  # for each el in arr
        # assign product_so_far to bucket at index i
        products[i] = product_so_far
        # multiply prod_so_far by the element in arr at index i
        product_so_far *= arr[i]

    product_so_far = 1  # reset product to 1

    # if [1,2,3] -> i=2, i=1, i=0
    #
    # for ( i=arr.length(); i>-1; i--) {
    # range(start, stop, step)
    # loops through range backwards (starting at len of arr - 1)
    for i in range(len(arr) - 1, -1, -1):
        products[i] *= product_so_far  # multiply el at index i by product_so_far
        product_so_far *= arr[i]  # multiply product_so_far by el at index i in arr

    return products  # return list of products


# def product_of_all_other_numbers(arr):
#     product = prod(arr)
#
#     product_bucket = [1 for _ in arr]
#     cur_val = 1
#     cur_idx = 0
#
#     if arr[0] is None:
#         return None
#
#     for i in range(len(arr)):
#         if cur_idx != i:
#         # cur_val
#         # temp = arr[i]
#         # arr.pop(i)
#
#         product_bucket[i] = product[i] / arr[i]
#
#     return product_bucket


# we do not yet know the size of the array
# can we assume anything?
# - numbers will be in a list form
# - only integers in list
#
# if not empty: iterate through the array
# cur pointer to mark current value
# keep track of val or index? index (position)
# for all the values that are not at marked position:
# multiply each other value by one another to get the product
#
# then add the product to the return array
#
# return array

# list comprehension from Doc later
def product_of_all_other_numbers_first_pass(arr):
    # multiply everything except the current element
    #
    # check to make sure array is not empty
    # if empty, return -1 or something
    product_bucket = [0] * len(arr)  # holding all products

    current_value = 1

    if arr[0] is None:
        return None

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                current_value *= arr[j]

        product_bucket[i] = current_value

        current_value = 1

    return product_bucket


# REFLECTION AFTER FIRST PASS SOLUTION
#


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8,
           5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
