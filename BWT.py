def bwt_transform(sequence):
    rotations = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    sorted_rotations = sorted(rotations)
    bwt_sequence = ''.join(rot[-1] for rot in sorted_rotations)
    print( 'bwt_sequence : ', bwt_sequence)
    return bwt_sequence
    # Implémentez ici la transformation BWT de la séquence donnée
    # Retournez la séquence BWT transformée

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
    bwt_sequence = bwt_transform(sequence)
    print("BWT sequence:", bwt_sequence)

    # Transformation inverse de BWT
    inverse_sequence = inverse_bwt_transform(bwt_sequence)
    print("Inverse sequence:", inverse_sequence)

    # Affichage de chaque étape de la transformation BWT
    display_bwt_transformation(sequence)


# Votre code principal pour l'interaction avec l'utilisateur et l'appel des fonctions BWT

if __name__ == "__main__":
    main()
