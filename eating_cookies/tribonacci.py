# from math import exp, log, sqrt
# 0 0 1 1 2 4 7 13 ...
# 0 1 2 3 4 5 6 7 ...
"""
trib(0): 0
trib(1): 0
trib(2): 1
trib(n): trib(n - 1) + trib(n - 2) + trib(n - 3)
"""


# def trib_maths(n):
#     n_root = lambda x, y: exp(1.0 / y * log(x))
#     # trConst = (1 + f_nRoot(19 + (3. * sqrt(33)), 3) + f_nRoot(19 - (3. * sqrt(33)), 3)) / 3.
#     tr_const = (1 + n_root(19 + (3.0 * sqrt(33)), 3) + n_root(19 - (3. * sqrt(33)), 3))  / 3.
#
#     # def n_root(x, n_): return exp(1. / n_ * log(x))


def trib_naive(n):
    if n == 0 or n == 1: return 0
    if n == 2: return 1
    return trib_naive(n - 1) + trib_naive(n - 2) + trib_naive(n - 3)


cache = {0: 0, 1: 0, 2: 1}


def trib_memoized(n):
    if n not in cache:
        cache[n] = trib_memoized(n - 1) + trib_memoized(n - 2) + trib_memoized(n - 3)

    return cache[n]


def trib_iter(n):
    if n == 0 or n == 1: return 0
    if n == 2: return 1

    a, b, c = 0, 0, 1
    # current = 0
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c

    return c


print("\n------\ntrib_iter")
for i in range(10):
    print(f"{i:3} {trib_iter(i)}")

print("\n------\ntrib_memoized")
for i in range(10):
    print(f"{i:3} {trib_memoized(i)}")
