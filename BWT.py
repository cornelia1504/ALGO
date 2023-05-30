""" """

def bwt_transform(sequence):
    assert '$' not in sequence  # L'entrée ne peut pas contenir le symbole $

    # Ajouter le marqueur de début et de fin de texte
    sequence = sequence + '$'

    # Créer la table des rotations
    table_no_sorted = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    #print(table_no_sorted)
    # Trier la table des rotations
    table = sorted(table_no_sorted)
    #print('\n' ,table)

    # Récupérer la dernière colonne de la table (symboles BWT)
    bwt = ''.join(row[-1] for row in table)

    return bwt , table_no_sorted

def display(sequence):
    table_no_sorted = bwt_transform(sequence)[1]
    for i, bwt in enumerate(table_no_sorted):
        print(f"Step {i + 1}: {bwt}")
        input("Press Enter to continue...")

def detransform_bwt(bwt_sequence):
    table = [''] * len(bwt_sequence)
    for i in range(len(bwt_sequence)):
        table = [bwt_sequence[i] + table[i] for i in range(len(bwt_sequence))] #add column of r ??
        #print('unsorted = ', table)
        table = sorted(table)
        #print('sorted = ', table)
        
    inverse_bwt = [row for row in table if row.endswith("$")][0] #find the correct row (ending with $)
    inverse_bwt = inverse_bwt.rstrip('$') #get rid of start and end markers
    print(inverse_bwt)
    
    return inverse_bwt





    
def Hinverse_bwt_transform(bwt_sequence):
    table = [''] * len(bwt_sequence)
    for _ in range(len(bwt_sequence)):
        table = sorted(bwt_sequence[i] + table[i] for i in range(len(bwt_sequence)))
    inverse_sequence = [row for row in table if row.endswith('$')][0][:-1]
    return inverse_sequence
    # Implémentez ici la transformation inverse de BWT pour la séquence BWT donnée
    # Retournez la séquence transformée en utilisant l'algorithme de votre choix

def inverse_bwt_transform(bwt_sequence):
    table = [''] * len(bwt_sequence)
    for _ in range(len(bwt_sequence)):
        table = sorted(bwt_sequence[i] + table[i] for i in range(len(bwt_sequence)))

    # Check if the table contains a row ending with '$'
    potential_rows = [row for row in table if row.endswith('$')]
    if len(potential_rows) > 0:
        inverse_sequence = potential_rows[0][:-1]
    else:
        # Handle the case when the sentinel character is missing
        inverse_sequence = ""

    return inverse_sequence

def display_bwt_transformation(sequence):
    rotations = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    sorted_rotations = sorted(rotations)
    bwt_transformations = [rot[-1] for rot in sorted_rotations]
    for i, bwt in enumerate(bwt_transformations):
        print(f"Step {i + 1}: {bwt}")
        input("Press Enter to continue...")
    # Implémentez ici l'affichage de chaque étape de la transformation BWT
    # Vous pouvez demander à l'utilisateur d'appuyer sur une touche pour afficher chaque étape

def main():
    sequence = "ATTTCCGCCCGTAGAGAGCAAATT"

    # Transformation BWT
    bwt_sequence = bwt_transform(sequence)[0]
    print("BWT sequence:", bwt_sequence)

    # Transformation inverse de BWT
    inverse_sequence = inverse_bwt_transform(bwt_sequence)
    print("Inverse sequence:", inverse_sequence)

    # Affichage de chaque étape de la transformation BWT
    display_bwt_transformation(sequence)


# Votre code principal pour l'interaction avec l'utilisateur et l'appel des fonctions BWT

if __name__ == "__main__":
    sequence = "ATTTCCGCCCGTAGAGAGCAAATT"
    print('sequence originale :', sequence)
    bwt_sequence = bwt_transform(sequence)[0]
    print("Transformée de BWT :", bwt_sequence)
    display(sequence)
    print("\n Détransformée:", detransform_bwt(bwt_sequence))
    # print("Détransformée:")
    # print(detransformed_sequence)
    #display_bwt_transformation(sequence)
    #main()
