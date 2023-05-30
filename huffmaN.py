import heapq

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{repr(self.left)}, {repr(self.right)}]"


class Leaf:
    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return repr(self.char)


def build_huffman_tree(frequencies):
    heap = []
    for char, freq in frequencies.items():
        leaf = Leaf(char)
        heapq.heappush(heap, (freq, id(leaf), leaf))

    while len(heap) > 1:
        weight1, _, left = heapq.heappop(heap)
        weight2, _, right = heapq.heappop(heap)
        new_node = Node(left, right)
        new_weight = weight1 + weight2
        heapq.heappush(heap, (new_weight, id(new_node), new_node))

    _, _, root = heapq.heappop(heap)
    return root


def generate_huffman_code(node, code, current_code=""):
    if isinstance(node, Leaf):
        code[node.char] = current_code or "0"
    elif isinstance(node, Node):
        generate_huffman_code(node.left, code, current_code + "0")
        generate_huffman_code(node.right, code, current_code + "1")


def encode_sequence(sequence, huffman_code):
    encoded_sequence = ""
    for char in sequence:
        encoded_sequence += huffman_code[char]
    return encoded_sequence


def decode_sequence(encoded_sequence, huffman_tree):
    decoded_sequence = ""
    current_node = huffman_tree
    for bit in encoded_sequence:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if isinstance(current_node, Leaf):
            decoded_sequence += current_node.char
            current_node = huffman_tree

    return decoded_sequence


def compress_sequence(sequence, huffman_code):
    compressed_sequence = ""
    for char in sequence:
        compressed_sequence += huffman_code[char]
    return compressed_sequence


def decompress_sequence(compressed_sequence, huffman_tree):
    decompressed_sequence = ""
    current_node = huffman_tree
    for bit in compressed_sequence:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if isinstance(current_node, Leaf):
            decompressed_sequence += current_node.char
            current_node = huffman_tree

    return decompressed_sequence


sequence = "TCATGGA$GGTCCCAAACCTGTATA"
#sequence = "NNTNACTTNGNNGTTNCCTATACCT"
print(sequence)
# Construction du dictionnaire de fréquences
frequencies = {}
for char in sequence:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Construction de l'arbre de Huffman
huffman_tree = build_huffman_tree(frequencies)

# Génération du code de Huffman
huffman_code = {}
generate_huffman_code(huffman_tree, huffman_code)

# Encodage de la séquence transformée
encoded_sequence = encode_sequence(sequence, huffman_code)

# Compression de la séquence en une chaîne de caractères
compressed_sequence = compress_sequence(sequence, huffman_code)

# Décompression de la chaîne binaire en acides nucléiques
decompressed_sequence = decode_sequence


# Affichage des résultats
print(frequencies)
print("Arbre de Huffman:")
print(repr(huffman_tree))
print("Code associé:")
print(huffman_code)
print("Encodage de la transformée:")
print(encoded_sequence)
print("Compressage en terme de chaîne de charactère:")
print(compressed_sequence) #no
print()
print("Décompressage en acide nucleique:")
print(decompressed_sequence)
