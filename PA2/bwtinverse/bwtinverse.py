# python3
import sys


def InverseBWT(bwt):
    bwt = list(bwt)
    cs = countSort(bwt)
    numb = [0] * 5
    pointer = []
    for i in range(len(bwt)):
        x = select(bwt[i])
        pointer.append(numb[x])
        numb[x] += 1
    x = 0
    og = []
    for i in range(len(bwt) - 1):
        a = bwt[x]
        n = select(a)
        og.append(a)
        x = cs[n] + pointer[x]
    og.reverse()
    return ''.join(og) + '$'


def BWT(text):
    arry = []
    x = len(text)
    for i in range(len(text)):
        arry.append(text[i:] + text[0:i])
    arry.sort()
    out = ""
    i = [z[-1] for z in arry]
    return ''.join(i)


def countSort(inp):
    out = [0] * 5
    for i in inp:
        out[select(i)] += 1
    out = [0] + out[:4]
    for i in range(1,5):
        out[i] += out[i-1]
    return out

def select(inp):
    a = ['$','A','C','G','T']
    return a.index(inp)

if __name__ == '__main__':
    inp = sys.stdin.readline().strip()
    print(InverseBWT(inp))
