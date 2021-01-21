from functools import cache
# from timeit import timeit


# @lru_cache(maxsize=None)
# def trib_lru(n):
#     if n < 2:
#         return 0
#     if n == 2:
#         return 1
#     return trib_lru(n - 1) + trib_lru(n - 2) + trib_lru(n - 3)


@cache
def trib_cache(n):
    # if n < 0:
    #     return None  # incorrect input
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # if n < 0:
    #     return None  # invalid input
    #
    # if n < 2:
    #     return 0
    #
    # if n == 2:
    #     return 1

    return trib_cache(n - 1) + trib_cache(n - 2) + trib_cache(n - 3)


def eating_cookies(n):
    if n < 0:
        return None  # invalid input

    if n < 2:
        return 1

    if n == 2:
        return 2

    return trib_cache(n + 2)


# def test_trib(n):
#     lru_time = timeit(f"trib_lru({n})", globals=globals(), number=1)
#     # lru_time = 100
#     cache_time = timeit(f"trib_cache({n})", globals=globals(), number=1)
#     print(f"n={n} lru_time={lru_time}, cache_time={cache_time} — take 1: winner= {'lru' if lru_time < cache_time else 'cache'}")


if __name__ == "__main__":
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    # test_trib(60)
    # print(trib_cache.cache_info())
