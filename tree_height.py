# python3

import sys
import threading

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

def compute_height(n, parents):
    # Create nodes for each index
    nodes = [Node(i) for i in range(n)]

    # Build tree by linking children to parents
    root = None
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent_index]
            parent_node.children.append(nodes[i])

    # Compute the height of the tree
    def height(node):
        if not node.children:
            return 1
        return 1 + max(height(child) for child in node.children)

    return height(root)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()



