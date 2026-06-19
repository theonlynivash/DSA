class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def print_codes(root, code=""):
    if root is None:
        return

    if root.char :
        print(root.char, ":", code)

    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")


def huffman(chars, freqs):

    nodes = []

    for i in range(len(chars)):
        nodes.append(Node(chars[i], freqs[i]))

    while len(nodes) > 1:

        nodes.sort(key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]


chars = ['A', 'B', 'C', 'D', 'E', 'F']
freqs = [5, 9, 12, 13, 16, 45]

root = huffman(chars, freqs)

print("Huffman Codes:")
print_codes(root)
