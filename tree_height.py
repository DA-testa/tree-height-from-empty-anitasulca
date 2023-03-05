# python3

import sys
import threading


class Node:
    def __init__(self, index):
        self.index = index
        self.children = []


def build_tree(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    return root


def compute_height(root):
    if not root:
        return 0

    max_height = 0

    for child in root.children:
        max_height = max(max_height, compute_height(child))

    return max_height + 1


def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ").upper()

    if text == "I":
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parent list separated by space: ").split()))

    elif text == "F":
        file_name = input("Enter file name: ").strip()

        if "a" in file_name.lower().split("/")[-1]:
            print("File name cannot contain letter 'a'.")
            return

        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline().strip())
                parents = list(map(int, file.readline().strip().split()))
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

