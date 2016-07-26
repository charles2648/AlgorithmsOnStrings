# python3
import sys

NA = -1


def solve(text, patterns):
    t = Trie()
    for p in patterns:
        cn = t.root
        for i in range(len(p)):
            cs = p[i]
            strings = [s.s for s in cn.outs]
            if cs in strings:
                e = strings.index(cs)
                cn = cn.outs[e].tail
            else:
                cn = t.addNode(cn, cs)
        cn.end = True
    return t.trieMatch(text)


class Trie:
    def __init__(self):
        self.root = self.Node(0)
        self.count = 1
        self.nodes = []
        self.edges = []

    class Node:
        def __init__(self, i):
            self.ins = []
            self.outs = []
            self.index = i
            self.end = False

    class Edge:
        def __init__(self, s, n, i):
            self.s = s
            self.head = n
            self.tail = Trie.Node(i)
            self.tail.ins.append(self)

        def __str__(self):
            return self.s

        __repr__ = __str__

    def addNode(self, n, s):
        e = Trie.Edge(s, n, self.count)
        self.edges.append(e)
        self.count += 1
        n.outs.append(e)
        self.nodes.append(e.tail)
        return e.tail

    def prefixMatch(self, text):
        v = self.root
        i = 0
        while True:
            # check if we're done
            if v.end:
                return v.end
            # if not, get next letter, see if it's an edge away
            strings = [s.s for s in v.outs]
            try:
                symbol = text[i]
            except IndexError:
                return False
            if symbol in strings and i < len(text):
                n = strings.index(symbol)
                v = v.outs[n].tail
                i += 1
            else:
                return False

    def trieMatch(self, text):
        matches = []
        for i in range(len(text)):
            if self.prefixMatch(text[i:]):
                matches.append(i)
        return matches

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve(text, patterns)

sys.stdout.write(' '.join (map (str, ans)) + '\n')
