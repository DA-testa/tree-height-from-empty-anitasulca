# python3

import sys
import threading

def compute_height(n, parents):
    # Handle case where tree has only one node
    if n == 1:
        return 1

    # Build tree data structure
    tree = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    # Traverse tree to compute height
    max_depth = 0
    def traverse(node, depth):
        nonlocal max_depth
        if not tree[node]:
            max_depth = max(max_depth, depth)
        for child in tree[node]:
            traverse(child, depth+1)

    traverse(root, 1)
    return max_depth

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute height of tree
    height = compute_height(n, parents)

    # Output result
    print(height)

# Increase recursion limit and stack size
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# Start main function in a new thread
threading.Thread(target=main).start()






