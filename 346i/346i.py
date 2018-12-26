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


while True:
    inp = input()
    if not inp:
        break

    (number, req_certainty) = inp.split()
    number = int(number)
    req_certainty = float(req_certainty)

    certainty = 0.0

    while True:
        a = randint(2, number-1)
        result = pow_mod(a, number, number)

        if result != a:
            print(number, 'is not prime')
            break

        else:
            certainty += (1 - certainty) / 2

            if certainty >= req_certainty:
                print(number, ' is prime with ', certainty*100, '% certainty', sep='')  # noqa: E501
                break
