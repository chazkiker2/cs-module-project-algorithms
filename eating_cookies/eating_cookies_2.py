from functools import cache as functools_cache


@functools_cache
def trib_cache(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    return trib_cache(n - 1) + trib_cache(n - 2) + trib_cache(n - 3)


cache = {
    0: 1,
    1: 1,
    2: 2,
}


# def make_cache(n):
#     cache_ = {i: 0 for i in range(n + 1)}
#     cache_.update({
#         0: 1,
#         1: 1,
#         2: 2
#     })
#     return cache_
#

def eating_cookies(n, t_cache={}):
    if t_cache == {}:
        cache.update({i: 0 for i in range(len(cache) - 1, n + 1)})
        t_cache = cache
        # print(cache)
        # t_cache = {i: 0 for i in range(n + 1)}
        # t_cache.update({
        #     0: 1,
        #     1: 1,
        #     2: 2
        # })

    def trib_memoized(n):
        if t_cache[n] == 0:
            t_cache[n] = trib_memoized(n - 1) + trib_memoized(n - 2) + trib_memoized(n - 3)

        return t_cache[n]

    return trib_memoized(n)


if __name__ == "__main__":
    try:
        num_cookies = 800
        print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
    except:
        import dis
        # import sys

        # exc_type, exc_value, exc_tb = sys.exc_info()
        # dis.distb(exc_tb)
        dis.dis(eating_cookies)
