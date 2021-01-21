'''
Input: a List of integers
Returns: a List of integers
'''


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
def product_of_all_other_numbers(arr):
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
