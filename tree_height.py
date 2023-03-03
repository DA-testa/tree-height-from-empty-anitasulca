# python3

import sys
import threading

def compute_height(n, parents):
    # Initialize an array of lists to represent the tree
    tree = [[] for i in range(n)]
    root = None

    # Create the tree
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    # Compute the height of the tree
    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max(height(child) for child in tree[node])

    return height(root)

def main():
    # Read input from user
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute and output the height of the tree
    print(compute_height(n, parents))

# Increase recursion limit and stack size for larger inputs
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

