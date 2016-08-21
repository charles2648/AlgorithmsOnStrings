# python3
import sys


def PreprocessBWT(bwt):

    bwt = list(bwt)
    starts = countSort(bwt)

    numb = [0] * 5
    pointer = [numb.copy()]
    for i in range(len(bwt)):
        x = select(bwt[i])
        numb[x] += 1
        pointer.append(numb.copy())
    return starts, pointer


def CountOccurrences(pattern, bwt, starts, occ):
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if pattern != '':
            s = pattern[-1]
            x = select(s)
            pattern = pattern[:-1]
            top = starts[x] + occ[top][x]
            bottom = starts[x] + occ[bottom + 1][x] - 1
        else:
            return bottom - top + 1
    return 0


def select(inp):
    a = ['$','A','C','G','T']
    return a.index(inp)


def countSort(inp):
    out = [0] * 5
    for i in inp:
        out[select(i)] += 1
    out = [0] + out[:4]
    for i in range(1,5):
        out[i] += out[i-1]
    return out

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
