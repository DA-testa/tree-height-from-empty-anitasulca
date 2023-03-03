# python3

import sys
import threading
import numpy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)]
    root_index = None
    for i in range(n):
        if parents[i] == -1:
            root_index = i
        else:
            nodes[parents[i]].children.append(nodes[i])
    root = nodes[root_index]
    return get_height(root)

def get_height(node):
    if len(node.children) == 0:
        return 1
    else:
        child_heights = []
        for child in node.children:
            child_heights.append(get_height(child))
        return 1 + max(child_heights)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()



