# I got close to a solution by manually working through a solution for n = 5,
# and then attempting to convert that process to a recursive function.
# However, I had to look up a correct solution in the end.

# My manual solution for n = 5 was this:
# 5!-(4!+(4!-3!)+(4!-3!-3!+2!)+(4!-3!-3!+2!-3!+2!+2!-1!)+(4!-3!-3!+2!-3!+2!+2!-1!-3!+2!+2!-1!+2!-1!))
#
# I wasn't sure how the tail end of the operations worked exactly,
# but this calculation is basically the same as what subfact() does.

import sys


# Where I ended my own attempt
def _subfact(n):
    if n == 0:
        return 1
    else:
        return n + subfact(n - 1) - subfact(n - 2)


def subfact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (subfact(n - 1) + subfact(n - 2))


print(subfact(int(sys.argv[1])))
