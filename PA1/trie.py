#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
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
    return t


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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for edge in tree.edges:
        print("{}->{}:{}".format(edge.head.index, edge.tail.index, edge.s))
