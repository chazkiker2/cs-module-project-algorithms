'''
Input: an integer
Returns: an integer
'''


# tribonacci: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3
# cookies = c(x) = a(x+1)
# cache
#
# def memoize(func):
#     cache = dict()
#
#     def memoized_func(*args):
#         if args in cache:
#             return cache[args]
#
#         result = func(*args)
#         cache[args] = result
#         return result
#
#     return memoized_func


def tribonacci_recursive(n):
    if n < 0:
        return None  # incorrect input
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return tribonacci_recursive(n - 1) + tribonacci_recursive(n - 2) + tribonacci_recursive(n - 3)


# memoized_fib = memoize(tribonacci_recursive)


def trib_cache(n, cache):
    if n in cache:
        return cache[n]
    else:
        # if n == 0 or n == 1:
        #     return 0
        # elif n == 2 or n == 3:
        #     return 1
        # else:
        res = trib_cache(n - 1, cache) + trib_cache(n - 2, cache) + trib_cache(n - 3, cache)
        cache[n] = res
        print(f"cache[{n}]={cache[n]}")
        return res


# memoized_fib(9999999)
# 0=0
# 1=0
# 2=1
#
# a(n)=a(n-1) + a(n-2) + a(n-3)
#
def eating_cookies(n):
    if n < 0:
        return None  # invalid input

    if n == 0 or n == 1:
        return 1

    if n == 2:
        return 2

    cache = {0: 0, 1: 0, 2: 1, 3: 1}

    if n in cache:
        return cache[n]

    return trib_cache(n + 2, cache)

    # opt_dict = {}
    # while n >= 1:  #
    #     for i in range(1, 4):
    #         # print(i)
    #         if n - i > 0:
    #             opt_dict[n] = i
    #             n -= i
    #             print(f"n={n}, opt_dict={opt_dict}")
    #
    # return len(opt_dict) * 2

    # n: int
    # returning x of type int
    #
    # the return value represents how many permutations cookie
    # monster can eat n cookies
    #
    # 1, 2, 3
    # Ava's least favorite problem

    # iterate through a range of n (count downwards from n times)
    # do math — this is why I'm the cookie monster
    # (n - 3!) % 4
    # 3 - 3 = 0 -> 0 -> 1, 3
    # 3 - 2 = 1 -> 2, 1
    # 3 - 1 = 2 -> 3, 1
    # 3! = 3 * 2 * 1
    #
    #
    # base case of n == 1 (only one option left)
    # base case means this is going to be recursive
    # while loop
    # use dict
    # declare

    # pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 12

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
