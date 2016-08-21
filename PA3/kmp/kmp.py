# python3

# Implementation of Knuth-Morris-Pratt Algorithm.

import sys


def find_pattern(pattern, text):
    result = []
    # get prefix array
    finds = get_prefix(pattern + '$' + text)[(len(pattern) + 1):]
    # find instances of full pattern, no slower than keeping list as you go.
    for i in range(len(finds)):
        if finds[i] == len(pattern):
            result.append(i - len(pattern) + 1)
    return result


def get_prefix(text):
    out = [0] * len(text)
    for i in range(1, len(text)):
        x = i - 1
        while x >= 0:
            if text[i] == text[out[x]]:
                out[i] = out[x] + 1
                break
            elif x == 0:
                break
            else:
                x = out[x] - 1
    return out


"""
# this code allows automated testing of the three sample tests, rather than relying on the standard in

import os
dir_path = os.path.dirname(os.path.realpath(__file__)) + '/sample_tests/'
for i in os.listdir(dir_path):
    if i.find('.a') == -1:
        f = open(dir_path + i, 'r')
        a, b = f.read().split('\n')[:2]
        f.close()
        f = open(dir_path + i + '.a', 'r')
        c = f.read().split(' ')
        if c != ['']:
            c = list(map(int, c))
        else:
            c = []
        d = find_pattern(a, b)
        if d == c:
            print(True)
        f.close()
exit(14)
"""

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
