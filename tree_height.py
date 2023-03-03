# python3

import sys
import threading

class Node:
    def __init__(self):
        self.children = []
        self.height = None

def compute_height(n, parents):
    # Create nodes for each index
    nodes = [Node() for _ in range(n)]

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
        if node.height is not None:
            return node.height
        if not node.children:
            node.height = 1
        else:
            node.height = 1 + max(height(child) for child in node.children)
        return node.height

    return height(root)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

if __name__ == '__main__':
    main()




