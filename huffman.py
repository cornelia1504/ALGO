import heapq
from collections import Counter, namedtuple

# Noeud de l'arbre de Huffman
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# Feuille de l'arbre de Huffman
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(sequence):
    # Compter les fréquences des caractères d'ADN
    frequencies = Counter(sequence)

    # Construire l'arbre de Huffman
    huffman_tree = []
    for char, freq in frequencies.items():
        huffman_tree.append((freq, len(huffman_tree), Leaf(char)))

    heapq.heapify(huffman_tree)
    count = len(huffman_tree)
    while len(huffman_tree) > 1:
        freq1, _count1, left = heapq.heappop(huffman_tree)
        freq2, _count2, right = heapq.heappop(huffman_tree)
        heapq.heappush(huffman_tree, (freq1 + freq2, count, Node(left, right)))
        count += 1

    # Générer la table de correspondance des codes binaires Huffman
    code = {}
    if huffman_tree:
        [(_freq, _count, root)] = huffman_tree
        root.walk(code, "")

    # Encoder la séquence d'ADN en utilisant les codes binaires Huffman
    encoded_sequence = "".join(code[char] for char in sequence)
    
    print('tree : ', huffman_tree)
    print('code associe : ', code)

    return encoded_sequence

def encode_dna_sequence(sequence):
    # Implémentez ici la transformation de la séquence d'ADN en binaire en utilisant Huffman
    # Retournez le binaire encodé
    # Transformer la séquence d'ADN en binaire en utilisant Huffman
    binary_sequence = huffman_encode(sequence)

    return binary_sequence

def main():
    #sequence = "ATTTCCGCCCGTAGAGAGCAAATT"
    #sequence = input('sequence :')
    sequence = 'ATTTCCGCCCGTAGAGAGCAAATT'

    # Transformation de la séquence d'ADN en binaire
    binary_sequence = encode_dna_sequence(sequence)
    print("Binary sequence:", binary_sequence)

def decode_binary_sequence(binary_sequence):
    pass
    # Implémentez ici la transformation du binaire en caractères en utilisant Huffman
    # Retournez la séquence de caractères décodée
    # Retournez la séquence d'ADN décodée

def encode_character_sequence(character_sequence):
    pass
    # Implémentez ici la transformation des caractères en binaire en utilisant Huffman
    # Retournez le binaire encodé

if __name__ == "__main__":
    
    main()
