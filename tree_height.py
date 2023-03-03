#python3
import sys
import threading

def compute_height(n, parents):
    # Create an array to keep track of the height of each node
    heights = [0] * n
    # Iterate over all nodes, calculate their height and update the max height
    max_height = 0
    for node in range(n):
        height = 0
        # Traverse from the current node to the root node
        while node != -1:
            # If the height of the current node has already been calculated,
            # we can reuse it to avoid redundant computation
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = parents[node]
        # Update the height of all the nodes traversed along the way
        node = parents[node]
        while node != -1:
            heights[node] = height
            height -= 1
            node = parents[node]
        max_height = max(max_height, heights[node])
    return max_height

def main():
    # Read input from stdin
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



