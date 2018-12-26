def matches(word, pattern):
    for i in range(0, len(word) - len(pattern) + 1):
        checkPattern = pattern
        j = 0

        for c in checkPattern:
            if 65 <= ord(c) <= 90:
                if not word[i + j] in checkPattern:
                    checkPattern = checkPattern.replace(c, word[i + j])

                j += 1

        if checkPattern in word:
            return True


if __name__ == "__main__":
    import sys

    if (len(sys.argv) < 3):
        exit()

    dictFile = open(sys.argv[1])
    for word in dictFile:
        word = word.strip('\n')
        if (matches(word, sys.argv[2])):
            print(word)
