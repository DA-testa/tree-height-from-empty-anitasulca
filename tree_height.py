#python3
import sys
import threading

def compute_height(n, parents):
    # Create an array to store the heights of each node
    heights = [0] * n

    # Iterate through each node, starting from the leaf nodes and moving up the tree
    for i in range(n):
        # If the node is a leaf, set its height to 1
        if heights[i] == 0:
            height = 1
            node = i
            while parents[node] != -1:
                parent = parents[node]
                if heights[parent] != 0:
                    height += heights[parent]
                    break
                height += 1
                node = parent
            heights[i] = height

    # Return the maximum height
    return max(heights)

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute and output the height of the tree
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

