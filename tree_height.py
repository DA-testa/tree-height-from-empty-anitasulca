# python3

import sys
import threading

def compute_height(n, parents):
    # Create a list to store the depth of each node
    depths = [-1] * n

    # Find the root node
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    # Define a recursive function to calculate the depth of each node
    def get_depth(node):
        if depths[node] != -1:
            return depths[node]

        if parents[node] == -1:
            depths[node] = 1
        else:
            depths[node] = get_depth(parents[node]) + 1

        return depths[node]

    # Calculate the depth of each node
    for i in range(n):
        get_depth(i)

    # Return the maximum depth
    return max(depths)

def main():
    # Read input from stdin
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute the height of the tree
    height = compute_height(n, parents)

    # Output the result
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


