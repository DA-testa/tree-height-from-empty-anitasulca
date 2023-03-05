# python3
 
import sys
import threading

def compute_height(n, parents):
    # Create an array to store the height of each node
    heights = [0] * n
    
    # Compute the height of each node in a bottom-up manner
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            # This is the root node, its height is 1
            heights[i] = 1
        else:
            # Compute the height of this node as the height of its parent plus 1
            heights[i] = heights[parent] + 1
    
    # Return the maximum height
    return max(heights)

def main():
    # Get input from the user
    input_type = input("Enter input type (K for keyboard, F for file): ")
    while input_type not in ["I", "F"]:
        input_type = input("Invalid input type, please enter K or F: ")
    
    if input_type == "I":
        # Read input from the keyboard
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter the parents of the nodes: ").split()))
    else:
        # Read input from a file
        file_name = input("Enter file name (without the letter 'a'): ")
        while "a" in file_name:
            file_name = input("Invalid file name, please enter a file name without the letter 'a': ")
        try:
            with open(f"input/{file_name}.txt", "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except:
            print("Error reading file. Please make sure the file exists in the 'input' folder and is named correctly.")
            return
    
    # Compute the height of the tree and print the result
    height = compute_height(n, parents)
    print(f"The height of the tree is {height}")

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
