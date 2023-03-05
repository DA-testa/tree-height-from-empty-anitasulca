# python3

import sys
import threading

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)

    max_height = 0
    stack = [(root, 1)]

    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)

        for child in nodes[node]:
            stack.append((child, height + 1))

    return max_height

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ").upper()

    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ")
        parents = list(map(int, parents_str.split()))

    elif text[0] == "F":
        file_name = input("Enter file name: ").strip()

        if "a" in file_name.lower() or "a" in file_name.lower().split("/")[-1]:
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

    height = compute_height(n, parents)
    print(height)

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    thread = threading.Thread(target=main)
    thread.start()
