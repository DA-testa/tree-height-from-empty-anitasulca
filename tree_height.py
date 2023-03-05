# python3

import sys
import threading

def compute_height(n, parents):
    if n == 1:
        return 0
    
    tree = [[] for i in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    heights = [-1] * n
    heights[root] = 1
    
    stack = [root]
    while stack:
        node = stack.pop()
        for child in tree[node]:
            heights[child] = heights[node] + 1
            stack.append(child)
    
    return max(heights)

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ").upper()
    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ")
        parents = list(map(int, parents_str.split()))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input("Enter file name: ")
        if "a" in file_name.lower() or "a" in file_name.lower().split("/")[-1]:
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
