from functools import cache

t_cache = {0: 0, 1: 0, 2: 1}


def trib_memoized(n):
    if n not in t_cache:
        t_cache[n] = trib_memoized(n - 1) + trib_memoized(n - 2) + trib_memoized(n - 3)

    return t_cache[n]


@cache
def trib_cache(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    return trib_cache(n - 1) + trib_cache(n - 2) + trib_cache(n - 3)


def eating_cookies(n):
    if n < 0:
        return None  # invalid input

    if n < 2:
        return 1

    if n == 2:
        return 2

    return trib_cache(n + 2)
    # return trib_memoized(n + 2)


if __name__ == "__main__":
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
