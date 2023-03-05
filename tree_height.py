# python3

import sys
import threading

def compute_height(n, parents):
    # create a list of lists to represent the tree
    tree = [[] for i in range(n)]
    root = None
    # populate the tree with parent-child relationships
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    # start with the root node and its height 0
    queue = [(root, 0)]
    max_height = 0
    # traverse the tree breadth-first and update the maximum height
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height + 1))
    return max_height

def main():
    # ask the user for input from keyboard or file
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        # read input from keyboard
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ")
        parents = list(map(int, parents_str.split()))
    elif text[0] == "F":
        # read input from file
        file_name = input("Enter file name: ")
        if "a" in file_name:
            print("File name cannot contain letter 'a'.")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline())
                parents_str = file.readline().strip()
                parents = list(map(int, parents_str.split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input option.")
        return

    # compute the height of the tree and print it
    height = compute_height(n, parents)
    print(height)

if __name__ == '__main__':
    # increase the recursion limit and stack size to avoid errors
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    thread = threading.Thread(target=main)
    thread.start()





