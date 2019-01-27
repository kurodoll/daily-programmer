# Warmup 1
def getSubtrees(t):
    trees = []
    cur = ''
    count = 1

    for i in range(1, len(t) - 1):
        if t[i] == '(':
            count += 1

        elif t[i] == ')':
            count -= 1

        else:
            continue

        cur += t[i]

        if count == 1:
            trees.append(cur)
            cur = ''

    return trees


def treeCode(t, count=0):
    if t == '()':
        return [count]

    subtrees = getSubtrees(t)
    ret = []

    for i in range(0, len(subtrees)):
        ret += treeCode(subtrees[i], count + len(subtrees[i]))

    return ret


def equal(t1, t2):
    return sorted(treeCode(t1)) == sorted(treeCode(t2))


w1_tests = [
    equal("((()((())()))(()))", "((())(()(()(()))))"),
    equal("((()))", "(()())"),
    equal("(((()())())()())", "(((()())()())())")
]

w1_answers = [
    True,
    False,
    False
]

print('Warmup 1 tests 1:', w1_tests == w1_answers)

w1_tests2 = open('tree-equal.txt', 'r').readlines()
n_equal = 0

for test in w1_tests2:
    if equal(test.split()[0], test.split()[1]):
        n_equal += 1

print('Warmup 1 tests 2:', n_equal, '/ 200')


# Warmup 2
def embeddable(t1, t2):
    return False


w2_tests = [
    embeddable("(())", "(()())"),
    embeddable("(()()())", "((()())())")
]

w2_answers = [
    True,
    False
]

print('\nWarmup 2 tests 1:', w2_tests == w2_answers)

w2_tests2 = open('tree-embed.txt', 'r').readlines()
n_equal = 0

for test in w2_tests2:
    if embeddable(test.split()[0], test.split()[1]):
        n_equal += 1

print('Warmup 2 tests 2:', n_equal, '/ 200')
