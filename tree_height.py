# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = {}
    root = None
    # Create tree
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)
    
    def traverse(node, depth):
        if node not in tree:
            return depth
        max_depth = depth
        for child in tree[node]:
            child_depth = traverse(child, depth+1)
            if child_depth > max_depth:
                max_depth = child_depth
        return max_depth
    
    return traverse(root, 1)

def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    file_input = input("Enter 'i' to input from keyboard or 'F' to input from file: ").strip().lower()
    if file_input == 'f':
        filename = input("Enter filename (without the letter 'a'): ").strip()
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    else:
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of nodes (space-separated): ").strip().split()))
    
    # call the function and output it's result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()






    


