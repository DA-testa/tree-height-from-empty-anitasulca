import sys
import threading

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    root = None

    # construct tree
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)

    # depth-first search to compute height
    def dfs(node):
        if not nodes[node]:
            return 1
        heights = [dfs(child) for child in nodes[node]]
        return max(heights) + 1

    return dfs(root)

def main():
    # read input
    n = int(input())
    parents = list(map(int, input().split()))

    # compute height of tree and print result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


