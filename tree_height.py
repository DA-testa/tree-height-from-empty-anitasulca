#python3
import sys

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
        self.parent = None

def compute_height(n, parents):
    # Create the nodes
    nodes = [Node(i) for i in range(n)]

    # Create the tree by adding each node to its parent's children list
    root = None
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent_index]
            parent_node.children.append(nodes[i])
            nodes[i].parent = parent_node

    # Recursively compute the height of the tree
    def height(node):
        if len(node.children) == 0:
            return 1
        else:
            return 1 + max(height(child) for child in node.children)

    return height(root)

def main():
    # Read the input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute the height of the tree and print the result
    print(compute_height(n, parents))

if __name__ == '__main__':
    # Increase the recursion limit and stack size
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)

    # Start the main thread
    threading.Thread(target=main).start()
    main()



