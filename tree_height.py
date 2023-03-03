# python3

import sys
import threading

def compute_height(n, parents):
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
    def traverse(node):
        if not tree[node]:
            return 1
        heights = [traverse(child) for child in tree[node]]
        return 1 + max(heights)

    return traverse(root)

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





