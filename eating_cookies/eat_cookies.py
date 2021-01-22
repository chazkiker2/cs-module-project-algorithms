# NAIVE RECURSIVE SOLUTION
# O(n^n) — exponential time complexity
def eating_cookies_naive(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies_naive(n - 1) + eating_cookies_naive(n - 2) + eating_cookies_naive(n - 3)


# MEMOIZED RECURSIVE SOLUTION (EFFICIENT)
# THANKS @Doc and @Ava for your guidance
def eating_cookies(n, cache={}):
    if cache == {}:
        cache = {i: 0 for i in range(n + 1)}
        cache.update({0: 1, 1: 1, 2: 2})

    # BASE CASE
    if n < 3:
        return 1 if n != 2 else 2

    if cache and cache[n] > 0:
        return cache[n]

    cache[n] = eating_cookies(n - 1, cache) \
               + eating_cookies(n - 2, cache) \
               + eating_cookies(n - 3, cache)

    return cache[n]


# NAIVE ITERATIVE SOLUTION (NOT EFFICIENT)
def eating_cookies_iter(n):
    if n == 0 or n == 1:
        return 1

    elif n == 2:
        return 2

    a, b, c = 1, 1, 2

    for _ in range(n - 1):
        a, b, c = b, c, a + b + c

    return c
