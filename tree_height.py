#python3
import sys
import threading

def compute_height(n, parents):
    # Create a list of lists to represent the tree
    tree = [[] for i in range(n)]

    # Fill the tree by adding each node to its parent's list of children
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    # Define a recursive function to calculate the height of the tree
    def height(node):
        if not tree[node]:
            return 1
        return max(height(child) for child in tree[node]) + 1

    # Call the recursive function on the root node to get the height of the tree
    return height(root)

def main():
    # Get input from the user
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute and print the height of the tree
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


