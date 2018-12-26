# A simple brute-force approach that searches through all possible permutations, beginning to end.  # noqa: E501
#  - Too slow to complete the challenge inputs in less than minutes.
#  - Prints out all possible permutations, not just the first one it finds.

from itertools import permutations


def toInt(assoc, str):
    '''Converts a string to its associated value, e.g. "BOOT" -> 4225'''

    value = 0

    for i in range(len(str)-1, -1, -1):
        value += assoc[str[i]] * (pow(10, len(str)-1-i))

    return value


def check(assoc, inputs, output):
    '''Returns True if the inputs add up to the output.'''

    sum = 0

    for i in inputs:
        val = toInt(assoc, i)
        sum += val

        if sum > toInt(assoc, output):
            break

    return sum == toInt(assoc, output)


# Get input cryptarithm
crypt = input()
crypt = crypt.replace('+ ', '')  # Reduce it to a more simple format
crypt = crypt.replace('== ', '')

# Get set of characters used
crypt_set = set(crypt)
crypt_set.remove(' ')

# Split words into inputs and output
words = crypt.split()
inputs = words[:-1]
output = words[-1]

for p in permutations(range(10), len(crypt_set)):
    assoc = dict(zip(crypt_set, p))

    # If any number would have a leading 0, skip
    for word in words:
        if assoc[word[0]] == 0:
            continue

    if check(assoc, inputs, output):
        print(assoc)
