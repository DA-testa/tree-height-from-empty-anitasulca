#python3
import sys

def compute_height(n, parents):
    # Create a list of empty lists to represent the tree
    tree = [[] for _ in range(n)]
    # Find the root node
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            # Add each node to its parent's list of children
            tree[parents[i]].append(i)
    # Define a helper function to recursively compute the height of a node
    def height(node):
        # If the node has no children, its height is 1
        if not tree[node]:
            return 1
        # Otherwise, its height is the maximum height of its children plus 1
        return max(height(child) for child in tree[node]) + 1
    # Compute the height of the root node
    return height(root)

def main():
    # Read input from keyboard
    n = int(input())
    parents = list(map(int, input().split()))
    # Compute and output the height of the tree
    print(compute_height(n, parents))

if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

