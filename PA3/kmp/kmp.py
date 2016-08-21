# python3
import sys


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = get_prefix(text)
    return result


def get_prefix(text):
    out = [0] * len(text)
    for i in range(1, len(text) - 1):
        x = i - 1
        while x > 0:
            if text[i] == text[out[x]]:
                out[i] = out[x] + 1
            else:
                x = out[x]
    return out


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
