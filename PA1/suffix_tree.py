# python3
import sys


def build_suffix_tree(text):
    t = SuffixTree(text)
    return [None]


class SuffixTree:
    def __init__(self, t):
        self.root = self.Node('')
        self.count = 1
        if t[-1] != '$':
            t += '$'
        self.text = t
        self.leaves = []
        for i in range(len(text)):
            self.leaves.append(text[i:])
        self.build()

    class Node:
        def __init__(self, s):
            self.outs = dict()
            self.val = -1
            self.s = s

    def build(self):
        for i in self.leaves[::-1]:
            cn = self.root
            for j in range(len(i)):
                cs = i[j]
                if cn.outs.get(cs) is None:
                    while j < len(i):
                        cs = i[j]
                        n = self.Node(cs)
                        cn.outs[cs] = n
                        j += 1
                    n.val = len(self.leaves) - j + 1
                    if j%100 == 0:
                        print(j)
                    break
                else:
                    cn = cn.outs.get(cs)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
