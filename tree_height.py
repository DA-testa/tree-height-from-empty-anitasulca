# python3

import sys
import threading

def compute_height(n, parents):
    # Create an array to store the height of each node
    heights = [0] * n

    # Find the root node
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    # Define a recursive function to compute the height of a node
    def compute_height_recursive(node):
        # Check if the height of this node has already been computed
        if heights[node] != 0:
            return heights[node]

        # Compute the height of each child and take the maximum
        max_height = 0
        for i in range(n):
            if parents[i] == node:
                height = compute_height_recursive(i)
                if height > max_height:
                    max_height = height

        # Update the height of this node and return it
        heights[node] = max_height + 1
        return heights[node]

    # Compute the height of the entire tree starting at the root
    compute_height_recursive(root)

    # Return the maximum height
    return max(heights)

def main():
    # Read the input
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
