# python3
 
import sys


class Node:
    def __init__(self):
        self.children = []


def compute_height(n, parents):
    nodes = [Node() for i in range(n)]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    queue = [root]
    max_height = 0

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
        max_height += 1

    return max_height


def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ")
        parents = list(map(int, parents_str.split()))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input("Enter file name: ")
        if "a" in file_name:
            print("File name cannot contain letter 'a'.")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline())
                parents_str = file.readline().strip()
                parents = list(map(int, parents_str.split()))
                height = compute_height(n, parents)
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input option.")
        return

    print(height)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    thread = threading.Thread(target=main)
    thread.start()




