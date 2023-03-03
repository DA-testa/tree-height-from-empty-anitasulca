# python3

import sys

def compute_height(n, parents):
    # Create an array to store the depth of each node
    depth = [0] * n

    # Traverse the tree and compute the depth of each node
    for i in range(n):
        # If the node has not been visited yet, compute its depth
        if depth[i] == 0:
            node = i
            d = 1
            while parents[node] != -1:
                # If the parent node has already been visited, use its depth
                if depth[parents[node]] != 0:
                    d += depth[parents[node]]
                    break
                # Otherwise, move up to the parent node and increment the depth
                node = parents[node]
                d += 1
            # Store the depth of the current node
            depth[i] = d

    # Return the maximum depth as the height of the tree
    return max(depth)

def main():
    # Read the input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute the height of the tree
    height = compute_height(n, parents)

    # Print the height
    print(height)

# Increase the recursion limit and stack size
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# Start the main function in a new thread
threading.Thread(target=main).start()




