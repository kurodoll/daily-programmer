import functools
import sys


@functools.lru_cache(maxsize=None)
def subfact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (subfact(n - 1) + subfact(n - 2))


print(subfact(int(sys.argv[1])))
