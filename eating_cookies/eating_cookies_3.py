def eating_cookies(n, cache={}):
    if cache == {}:
        cache = {i: 0 for i in range(n + 1)}
        # Empty Cache Bucket! Dictionary Comprehension {1:0, 2:0,..., n+1: 0}

    # checks if negative cookies which would have no way of eating it
    if n < 0:
        return 0

    # if 0 cookies only 1 way to eat it
    elif n == 0:
        return 1

    # check cache to see if answer is stored in there
    if cache and cache[n] > 0:
        return cache[n]

    else:
        # store answers in cache
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]
