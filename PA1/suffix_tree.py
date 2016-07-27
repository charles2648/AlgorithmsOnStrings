# python3
import sys


def build_suffix_tree(text):
    t = SuffixTree(text)
    output = []
    for i in t.edges:
        if i.s != '':
            output.append(i.s)
    return output


class SuffixTree:
    def __init__(self, text):
        self.root = self.Node(0)
        self.count = 1
        self.nodes = []
        self.edges = []
        if text[-1] != '$':
            text += '$'
        self.text = text
        self.buildTree(text)

    class Node:
        def __init__(self, i):
            self.ins = []
            self.outs = []
            self.index = i

    class Edge:
        def __init__(self, s, n, i):
            self.s = s
            self.head = n
            self.tail = SuffixTree.Node(i)
            self.tail.ins.append(self)

        def __str__(self):
            return self.s

        __repr__ = __str__

    def addNode(self, n, s):
        e = SuffixTree.Edge(s, n, self.count)
        self.edges.append(e)
        self.count += 1
        n.outs.append(e)
        self.nodes.append(e.tail)
        return e.tail

    def buildTree(self, t):
        for p in range(len(t)):
            chunk = t[p:]
            cn = self.root
            for i in range(len(chunk)):
                cs = chunk[i]
                strings = [s.s for s in cn.outs]
                if cs in strings:
                    e = strings.index(cs)
                    cn = cn.outs[e].tail
                else:
                    cn = self.addNode(cn, cs)
        self.collapse()

    def collapse(self):
        for n in self.nodes:
            # if a node has only one outgoing edge
            if len(n.outs) == 1:
                # merge outgoing edge into incoming edge
                e1 = n.ins[0]
                e2 = n.outs[0]
                self.mergeEdges(e1, e2, n)

    def mergeEdges(self, e1, e2, n):
        n.ins = []
        n.outs = []
        n.index = -1
        e1.tail = e2.tail
        e2.tail.ins[0] = e1
        e1.s += e2.s
        e2.s = ''
        e2.head = None
        e2.tail = None


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
