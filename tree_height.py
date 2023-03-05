# python3
 
import sys
import threading

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

def compute_height(node):
    if not node.children:
        return 1
    heights = [compute_height(child) for child in node.children]
    return 1 + max(heights)

def build_tree(n, parents):
    nodes = [Node() for _ in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
            nodes[i].parent = nodes[parent]
    return root

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parent list separated by space: ").split()))
        if len(parents) != n:
            print("Invalid input: number of parents does not match number of nodes.")
            return
    elif text[0] == "F":
        file_name = input("Enter file name: ")
        if "a" in file_name:
            print("File name cannot contain letter 'a'.")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline().strip())
                parents_str = file.readline().strip()
                parents = list(map(int, parents_str.split()))
                if len(parents) != n:
                    print("Invalid input: number of parents does not match number of nodes.")
                    return
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input option.")
        return

    root = build_tree(n, parents)
    height = compute_height(root)
    print(height)

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    thread = threading.Thread(target=main)
    thread.start()


