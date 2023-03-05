# python3
 import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None
    for i in range(n):
        parent_idx = parents[i]
        if parent_idx == -1:
            root = nodes[i]
        else:
            nodes[parent_idx].children.append(nodes[i])
    return root

def height(node):
    if not node.children:
        return 1
    return 1 + max(height(child) for child in node.children)

def main():
    input_type = input("Enter input type (F for file, K for keyboard): ").upper()
    if input_type == "F":
        filename = input("Enter filename (without the letter 'a'): ")
        if 'a' in filename:
            print("Invalid filename")
            return
        try:
            with open(f"inputs/{filename}") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found")
            return
    elif input_type == "K":
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents of nodes separated by spaces: ").split()))
    else:
        print("Invalid input type")
        return

    root = build_tree(n, parents)
    print(height(root))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()







    


