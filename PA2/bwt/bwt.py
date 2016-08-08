# python3
import sys

def BWT(text):
    arry = []
    x = len(text)
    for i in range(len(text)):
        arry.append(text[i:] + text[0:i])
    arry.sort()
    out = ""
    i = [z[-1] for z in arry]
    return ''.join(i)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))