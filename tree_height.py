#python3
import sys

def compute_height(n, parents):
    # Create a list to represent the tree
    # Each element of the list will be a list of the indices of the children of the corresponding node
    tree = [[] for _ in range(n)]
    # Find the index of the root node
    root_index = parents.index(-1)
    # Fill in the children lists of the tree
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)
    # Define a recursive function to compute the height of the tree
    def get_height(node_index):
        # If the node has no children, its height is 1
        if not tree[node_index]:
            return 1
        # Otherwise, the height of the node is 1 + the maximum height of its children
        return 1 + max(get_height(child_index) for child_index in tree[node_index])
    # Compute the height of the tree
    return get_height(root_index)

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))
    # Compute and output the height of the tree
    print(compute_height(n, parents))

if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem.
    sys.setrecursionlimit(10**7)
    main()
