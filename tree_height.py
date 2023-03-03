# python3

import sys

def compute_height(n, parents):
    # construct the tree as an adjacency list
    tree = {}
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            if parents[i] not in tree:
                tree[parents[i]] = []
            tree[parents[i]].append(i)

    # recursively compute the height of the tree
    def height(node):
        if node not in tree:
            return 1
        else:
            return max([height(child) for child in tree[node]]) + 1

    return height(root)

def main():
    # read input from stdin
    n = int(input())
    parents = list(map(int, input().split()))

    # compute and output the height of the tree
    print(compute_height(n, parents))

if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()






