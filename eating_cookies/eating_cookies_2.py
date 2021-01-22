from functools import cache as funccache

t_cache = {
    0: 0,
    1: 0,
    2: 1
}


# def doc_eating_cookies(n):
#     if n == 0:
#         return 1


def trib_memoized(n):
    if n not in t_cache:
        t_cache[n] = trib_memoized(n - 1) + trib_memoized(n - 2) + trib_memoized(n - 3)

    return t_cache[n]


@funccache
def trib_cache(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    return trib_cache(n - 1) + trib_cache(n - 2) + trib_cache(n - 3)


def eating_cookies(n):
    # if n < 0:
    #     return None  # invalid input

    if n < 2:  # 0, 1
        return 1

    if n == 2:  # 1+1=2, 2=2
        return 2

    # if cache == {}:
    #     cache = {0: 0,
    #              1: 0,
    #              2: 1}

    # return trib_cache(n + 2)
    # eating_cookies(3) -> eating_cookies(2) + eating_cookies(1) + eating_cookies(0)
    #
    return trib_memoized(n + 2)


# 0: 0, 1: 0, 2: 1, 3: 2
# 0 0 1 2 4
# 1 1 2 4 7
# 0 1 2 3 4
#     if n == 0:
#         return 1


if __name__ == "__main__":
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
