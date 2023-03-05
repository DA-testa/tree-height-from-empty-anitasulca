# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)
    root = np.where(parents == -1)[0][0]
    queue = [(root, 0)]
    max_height = 0
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height + 1))
    return max_height

def main():
    text = input().strip()
    if text[0] == "I":
        n = int(input().strip())
        parents_str = input().strip()
        parents = np.array(list(map(int, parents_str.split())))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input().strip()
        if "a" in file_name:
            print("wrong")
            return
        with open("folder/" + file_name, 'r') as file:
            n = int(file.readline().strip())
            parents_str = file.readline().strip()
            parents = np.array(list(map(int, parents_str.split())))
            height = compute_height(n, parents)
    print(height)

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # Increase recursion limit to avoid stack overflow errors
    threading.stack_size(2**27)  # Increase stack size to avoid stack overflow errors
    thread = threading.Thread(target=main)
    thread.start()





    


