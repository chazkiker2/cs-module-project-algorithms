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


def trib_cache_iter(n, cache):
    if n in cache:
        return cache[n]

    a, b, c = 0, 1, 1

    for i in range(3, n):
        a, b, c = b, c, a + b + c
        cache.update({i - 2: a, i - 1: b, i: c})

    # cache.update({n: c})

    return c


# memoized_fib(9999999)
# 0=0
# 1=0
# 2=1
#
# a(n)=a(n-1) + a(n-2) + a(n-3)
#
def eating_cookies_old(n):
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


def check_cache(key, cache):
    if key in cache:
        return cache[key]

    return None


def check_cache_prev(n, cache):
    if all(key in cache for key in (n - 1, n - 2, n - 3)):
        result = cache[n - 1] + cache[n - 2] + cache[n - 3]
        cache[n] = cache[n - 1] + cache[n - 2] + cache[n - 3]
        return result

    return None


def tribinocci_final(n, cache):
    if n in cache:  # if we've run this problem before:
        return cache[n]

    # else, check to see if n-1, n-2, n-3 are in cache:
    if all(key in cache for key in (n - 1, n - 2, n - 3)):
        result = cache[n - 1] + cache[n - 2] + cache[n - 3]
        cache[n] = cache[n - 1] + cache[n - 2] + cache[n - 3]
        return result

    a, b, c = 1, 1, 2

    for i in range(3, n):
        a, b, c = b, c, a + b + c

        print(f"(i-2={i - 2}: a={a}), (i-1={i - 1}: b={b}), (i={i}: c={c})")
        print(f"cache={cache}")
        cache.update({i - 2: a, i - 1: b, i: c})

    # cache.update({n: c})

    return c


def eating_cookies_iter(n):
    if n < 0:
        return None

    cache = {
        0: 1,
        1: 1,
        2: 2,
    }

    if n in cache:
        return cache[n]

    # a, b, c = 1, 1, 2
    #
    # for i in range(3, n):
    #     a, b, c = b, c, a + b + c
    #     print(f"{i - 2}: {a}, {i - 1}: {b}, {i}: {c}")
    #     cache.update({i - 2: a, i - 1: b, i: c})
    #
    # # cache.update({n: c})
    #
    # return c

    # back1, back2, back3 = n - 1, n - 2, n - 3
    #
    # while n >= 3:
    #     response = back1 + back2 + back3

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


def eating_cookies(n):  # NAIVE RECURSIVE SOLUTION
    if n < 0:  # in case input is invalid (can't eat negative cookies)
        return 0
    elif n == 0:  # the cookies are all gone
        return 1  # there's only one way to eat 0 cookies — not at all
    else:  # there are still cookies left!
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


# NOTES ABOUT eating_cookies
# input = n cookies (int)
# output = number of ways to eat a cookie (int)
#
# transformation
#
# ways to eat: 1 at a time, 2 at a time, or 3 at a time
# - number of cookies left = n
# - eat 1 cookie at a time=(n-1),
# - eat 2 cookies at a time=(n-2)
# - eat 3 cookies at a time=(n-3)
#
# repeat process some number of time: recursion
#
# recursion:
# - base case (a condition to stop recurse)
# - function that calls itself
# - moves toward base case
#
# mental mode: recursion is like a while loop
# recursion can almost always be represented by a while loop
# base case is condition where while loop would exit
# DM Doc if you want more info

# first, function calls itself.
# EXEC STACK: eating_cookies(n-1).... + eating_cookies(n-2) .... + eating_cookies(n-3)
# eat_cookies(n-3) on TOP of stack, so it's first to be pulled OFF
# eating_cookies(n-3) = res -> place result on RESULT STACK
# then take eating_cookies(n-2) off the top of stack, compute, add result to result stack
# finally, take eating_cookies(n-1) off top of stack, compute, add result to result stack

# num_cookies_left = 0 -> how many ways can you eat 0 cookies?
# - the only way to eat 0 cookies is to not eat any cookies at all!
# (so then, 1 way to eat 0 cookies: not at all!)

# three ways to eat cookies:
# 1. n-1 (eat one cookie)
# 2. n-2 (eat two cookies)
# 3. n-3 (eat three cookies)
# if n-3 is called and 3 is n: n will then be 0. next time it's called, return 1 b/c n == 0
#


# the smallest n will ever be is -2
# because any n less than or equal to 0 does not recurse

# the smallest n will ever be is 0
# because any n less than three does not recurse
def eating_cookies_(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies_(n - 1) + eating_cookies_(n - 2) + eating_cookies(n - 3)


# Your version
# eating_cookies(n-3) where n = 3:
# return eating_cookies(2) + eating_cookies(1) + eating_cookies(0)
#   eating_cookies(2) -> return eating_cookies(1) + eating_cookies(0) + eating_cookies(-1)
#       eating_cookies(1) -> return eating_cookies(0) + eating_cookies(-1) + eating_cookies(-2)
#           eating_cookies(0) -> return 1
#   eating_cookies(1) -> return eating_cookies(0) + eating

# My version
# TEST CASE = eating_cookies_naive(3)
# eating_cookies_naive(n) where n = 3:
#
# return eating_cookies_naive(2) + eating_cookies_naive(1) + eating_cookies_naive(0)
#   eating_cookies_naive(2) -> return 2
#   eating_cookies_naive(1) -> return 1
#   eating_cookies_naive(0) -> return 1
# so return 2 + 1 + 1 = 4
# thus, eating_cookies_naive(3) returns 4

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    # num_cookies = 12
    #
    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    # outer_cache = {0: 0, 1: 0, 2: 1, 3: 1}
    outer_cache = {
        0: 1,
        1: 1,
        2: 2,
    }
    for i in range(10):
        print(f"\n------\nRUNNING TRIBONACCI WITH i={i}\n------\n")
        print(f"i={i}, res={tribinocci_final(i, outer_cache)}")

    print(outer_cache)
