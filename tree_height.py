# python3

import sys
import threading
import numpy

def build_tree(n, parents):
    nodes = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    return nodes, root

def tree_height(nodes, root):
    if not nodes[root]:
        return 1
    heights = [tree_height(nodes, child) for child in nodes[root]]
    return max(heights) + 1

def compute_height(n, parents):
    nodes, root = build_tree(n, parents)
    return tree_height(nodes, root)

def main():
    # get input from keyboard or file
    input_type = input().strip()
    if input_type == 'F':
        filename = input().strip()
        if 'a' in filename.lower():
            print("Invalid filename")
            return
        try:
            with open(f"inputs/{filename}") as f:
                input_data = f.read().strip()
        except FileNotFoundError:
            print("File not found")
            return
    elif input_type == 'I':
        input_data = input().strip()
    else:
        print("Invalid input type")
        return
    
    # parse input
    n, *parents = map(int, input_data.split())
    
    # compute and output result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()





    


