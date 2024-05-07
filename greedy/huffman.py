import heapq
from collections import defaultdict

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def get_user_input():
    # Prompt the user to enter the number of letters
    num_letters = int(input("Enter the number of letters: "))
    freq_dict = {}
    for _ in range(num_letters):
        # Get letter and frequency input from the user
        char = input("Enter a letter: ")
        freq = int(input(f"Enter the frequency for {char}: "))
        freq_dict[char] = freq
    return freq_dict

def huffman_coding(freq_dict):
    # Create a heap of nodes from the given frequencies
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Build the Huffman tree using the heap
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        merged_node = Node(freq=lo.freq + hi.freq)
        merged_node.left = lo
        merged_node.right = hi
        heapq.heappush(heap, merged_node)

    return heap[0]

def main():
    # Get user input for letter frequencies
    freq_dict = get_user_input()

    # Display user-provided alphabet frequencies
    print("Alphabets and their frequencies:")
    for char, freq in freq_dict.items():
        print(f"{char}: {freq}")

    # Generate Huffman tree and codes
    huffman_tree = huffman_coding(freq_dict)

    encoded_values = {}
    def get_codes(node, code=""):
        # Traverse the Huffman tree to get encoded values for each letter
        if node:
            if node.char:
                encoded_values[node.char] = code
            get_codes(node.left, code + "0")
            get_codes(node.right, code + "1")

    get_codes(huffman_tree)

    # Display the final encoded values for all letters
    print("\nFinal encoded values for all letters:")
    for char, code in encoded_values.items():
        print(f"{char}: {code}")

if __name__ == "__main__":
    main()


# mannnn wud do this
import heapq 

class node: 
    def __init__(self, freq, symbol): 
        self.freq = freq 
        self.symbol = symbol 
        self.left = None
        self.right = None
        self.huff = '' 

    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

def printNodes(node, val=''): 
    newVal = val + str(node.huff) 
    if(node.left): 
        printNodes(node.left, newVal) 
    if(node.right): 
        printNodes(node.right, newVal) 
    if(not node.left and not node.right): 
        print(f"{node.symbol}:{node.freq} -> {newVal}") 
        
def huffman(chars, freq):
    nodes = [] 

    for x in range(len(chars)): 
        heapq.heappush(nodes, node(freq[x], chars[x])) 

    while len(nodes) > 1: 
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes) 
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq+right.freq, left.symbol+right.symbol)
        newNode.left = left
        newNode.right = right
        heapq.heappush(nodes, newNode) 
    return nodes[0]

def main():
    chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
    freq = [5, 9, 12, 13, 16, 45] 
    root = huffman(chars, freq)
    printNodes(root)
     
if __name__=='__main__':
     main()
