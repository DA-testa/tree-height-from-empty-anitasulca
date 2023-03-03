# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Create a list of children for each node
    children = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)

    # Compute the height of the tree
    def height(node):
        if not children[node]:
            return 1
        return 1 + max(height(child) for child in children[node])
    
    root = parents.index(-1)
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


