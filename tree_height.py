# python3

import sys
import threading

def compute_depth(i, parents, depths):
    if depths[i] != 0:
        return depths[i]
    if parents[i] == -1:
        depths[i] = 1
    else:
        depths[i] = 1 + compute_depth(parents[i], parents, depths)
    return depths[i]

def compute_height(n, parents):
    depths = [0] * n
    max_depth = 0
    for i in range(n):
        max_depth = max(max_depth, compute_depth(i, parents, depths))
    return max_depth

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

