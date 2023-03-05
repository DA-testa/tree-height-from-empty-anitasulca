# python3
 
import sys
import threading

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    indices = [i for i in range(n)]
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)

    heights = [0] * n
    for i in indices:
        if not tree[i]:
            # leaf node
            heights[i] = 1
        else:
            heights[i] = 1 + max(heights[j] for j in tree[i])

    return max(heights)

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ").strip()
        if n == 0:
            height = 0
        else:
            parents = list(map(int, parents_str.split()))
            height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input("Enter file name: ").strip()
        if "a" in file_name:
            print("File name cannot contain letter 'a'.")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline())
                if n == 0:
                    height = 0
                else:
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



