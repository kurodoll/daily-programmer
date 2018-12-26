import math

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
strings = ['E', 'B', 'G', 'D', 'A', 'X']  # X is E, but must be distinguished from the first E  # noqa: E501
stringsO = [4, 3, 3, 3, 2, 2]


def getFrets(tabFile):
    lines = []
    frets = []

    for line in tabFile:
        lines.append(line)

    i = 0
    while True:
        for j in range(0, 6):
            if '0' <= lines[j][i] <= '9':
                if '0' <= lines[j][i + 1] <= '9':
                    frets.append(strings[j] + lines[j][i] + lines[j][i + 1])
                    i += 1
                else:
                    frets.append(strings[j] + lines[j][i])

        i += 1
        if (i == len(lines[0])):
            break

    return frets


def printNotes(noteList):
    for note in noteList:
        noteIndex = notes.index(note[0]) if note[0] != 'X' else notes.index('E')  # noqa: E501

        needed = noteIndex - 3 if noteIndex < 3 else noteIndex - 15   # The fret number needed to increase an octave  # noqa: E501
        octaveChange = math.floor((needed + int(note[1:])) / 12) + 1  # The amount of octaves to change by            # noqa: E501

        print((notes * (math.floor(int(note[1:]) / 12) + 2))[noteIndex + int(note[1:])], stringsO[strings.index(note[0])] + octaveChange, sep='', end=' ')  # noqa: E501


if __name__ == "__main__":
    import sys

    if (len(sys.argv) < 2):
        exit()

    printNotes(getFrets(open(sys.argv[1])))
