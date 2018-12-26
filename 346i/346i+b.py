# Uses the Miller-Rabin test to account for Carmichael numbers.

from random import randint


# Credit: https://stackoverflow.com/a/10539256
def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


# This is dumb since there'd be a simple equation to calculate this,
# but idk that equation
def certaintyToIters(req_certainty):
    certainty = 0.0
    iters = 0

    while True:
        certainty += (1 - certainty) / 2
        iters += 1

        if certainty >= req_certainty:
            break

    return iters


def millerRabinTest(number, req_certainty):
    '''Returns False for composite or True for probably prime.'''

    # Write n-1 as 2^r*d
    d = number - 1
    r = 0

    while d % 2 == 0:
        d //= 2  # Standard division results in a float; // is required for integer division  # noqa: E501
        r += 1

    d = int(d)

    # WitnessLoop (have to convert the given required certainty (as percentage) to a number of iterations)  # noqa: E501
    for i in range(certaintyToIters(req_certainty)):
        a = randint(2, number-2)
        x = pow_mod(a, d, number)

        if x == 1 or x == number-1:
            continue

        for j in range(r-1):
            x = pow_mod(x, 2, number)

            if x == 1:
                return False

            if x == number-1:
                break

        if x != number-1:
            return False

    return True


while True:
    inp = input()
    if not inp:
        break

    (number, req_certainty) = inp.split()
    number = int(number)
    req_certainty = float(req_certainty)

    if millerRabinTest(number, req_certainty):
        print(number, ' is prime at >=', req_certainty*100, '% certainty', sep='')  # noqa: E501
    else:
        print(number, 'is not prime')
