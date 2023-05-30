def bwt_transform(sequence):
    """
    Transforme une séquence en utilisant l'algorithme de transformation de Burrows-Wheeler (BWT).

    Returns:
        tuple: Un tuple contenant la séquence transformée et la table des rotations non triée.
    """
    # Verifie que l'entrée ne contient pas le symbole $
    assert '$' not in sequence  

    # Ajouter le marqueur de début et de fin de texte
    sequence = sequence + '$'

    # Créer la table des rotations
    # for i in range(len(sequence)):
    #     print(sequence[i:] )
    #     print(sequence[i:] + sequence[:i])
    table_no_sorted = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    table_no_sorted.reverse
    table_no_sorted = table_no_sorted[::-1]
    print(table_no_sorted)
    # Trier la table des rotations
    table = sorted(table_no_sorted)
    #print(table)
    # Récupérer la dernière colonne de la table (symboles BWT)
    bwt = ''.join(row[-1] for row in table)

    return bwt, table_no_sorted


def detransform_bwt(bwt_sequence):
    """
    Réalise la détransformation de la séquence transformée en utilisant l'algorithme de Burrows-Wheeler (BWT).

    Returns:
        str: La séquence détransformée.
    """
    # Crée une liste de chaînes vides de même longueur que la séquence transformée
    table = [''] * len(bwt_sequence)  
    for i in range(len(bwt_sequence)):
        # Ajoute la colonne 'r' en concaténant chaque caractère de la séquence transformée avec la chaîne correspondante dans la table
        table = [bwt_sequence[i] + table[i] for i in range(len(bwt_sequence))]  
         # Trie la table des rotations
        table = sorted(table) 
        
    # Trouve la bonne ligne dans la table qui se termine par le symbole de fin $
    inverse_bwt = [row for row in table if row.endswith("$")][0]  
    # Supprime les marqueurs de début et de fin de la séquence
    inverse_bwt = inverse_bwt.rstrip('$')  
    # Affiche la séquence détransformée
    print(inverse_bwt)  

    # Retourne la séquence détransformée
    return inverse_bwt  

def save_results(original_sequence, transformed_sequence, inverse_sequence):
    """
    Sauvegarde les résultats de la transformation BWT dans un fichier texte.

    Args:
        original_sequence (str): La séquence originale.
        transformed_sequence (str): La séquence transformée.
        inverse_sequence (str): La séquence détransformée.
    """
    with open("bwt_results.txt", "w") as file:
        file.write("Séquence originale:\n")
        file.write(original_sequence + "\n\n")
        file.write("Transformée de BWT:\n")
        file.write(transformed_sequence + "\n\n")  # Modifier cette ligne pour accéder à la séquence transformée uniquement
        file.write("Détransformée:\n")
        file.write(inverse_sequence)
    print("Transformation sauvegardee dans le fichier : bwt_results.txt")

if __name__ == "__main__":
    sequence = 'ATTTCCGCCCGTAGAGAGCAAATT'
    #sequence= 'ACTTGATC'
    bwt_sequence = bwt_transform(sequence)[0]
    inverse_sequence = detransform_bwt(bwt_sequence)
    save_results(sequence, bwt_sequence, inverse_sequence)