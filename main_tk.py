import tkinter as tk
from tkinter import messagebox, filedialog
import bwt as b

def detransform_bwt_BIS(bwt_sequence):
    """
    Réalise la détransformation de la séquence transformée en utilisant l'algorithme de Burrows-Wheeler (BWT).

    Args:
        bwt_sequence (str): La séquence transformée.

    Returns:
        str: La séquence détransformée.
    """
    table = [''] * len(bwt_sequence)
    for i in range(len(bwt_sequence)):
        table = [bwt_sequence[i] + table[i] for i in range(len(bwt_sequence))]
        table = sorted(table)
        
    inverse_bwt = [row for row in table if row.endswith("$")][0]
    inverse_bwt = inverse_bwt.rstrip('$')
    
    return inverse_bwt



def display_steps(sequence):
    """
    Affiche chaque étape de la transformation BWT dans une boîte de dialogue.

    Args:
        sequence (str): La séquence à transformer.
    """
    table_no_sorted = b.bwt_transform(sequence)[1]
    for i, bwt in enumerate(table_no_sorted):
        messagebox.showinfo(f"Step {i + 1}", bwt)
        
def display():
    """
    Affiche la séquence transformée avec les étapes de la transformation BWT.
    """
    sequence = sequence_entry.get()
    if sequence:
        transformed_sequence = b.bwt_transform(sequence)
        messagebox.showinfo("BWT Transformation", f"{transformed_sequence}")
        #display_steps(sequence)


def transform_sequence():
    """
    Transforme la séquence saisie en utilisant l'algorithme BWT.
    """
    sequence = sequence_entry.get()
    if sequence:
        transformed_sequence, _ = b.bwt_transform(sequence)
        messagebox.showinfo("BWT Transformation", f"Transformed sequence:\n{transformed_sequence}")
        

def detransform_sequence():
    """
    Détransforme la séquence transformée en utilisant l'algorithme BWT.
    """
    sequence = sequence_entry.get()

    transformed_sequence, _ = b.bwt_transform(sequence)
    if transformed_sequence:
        inverse_sequence = detransform_bwt_BIS(transformed_sequence)
        messagebox.showinfo("BWT Detransformation", f"Inverse sequence:\n{inverse_sequence}")
        b.save_results(sequence_entry.get(), transformed_sequence, inverse_sequence)

def browse_file():
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier FASTA et insère son contenu dans le champ de saisie.
    """
    file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta" or "*.fa")])
    if file_path:
        sequences = process_fasta_file(file_path)
        if sequences:
            sequence_entry.delete(0, tk.END)
            sequence_entry.insert(tk.END, sequences[0])  # Insérer la première séquence dans le champ de saisie

def process_fasta_file(file_path):
    sequences = []
    current_sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line

        if current_sequence:
            sequences.append(current_sequence)

    return sequences

            
def save_bwt():
    """
    Sauvegarde la séquence originale, transformée et détransformée dans un fichier.
    """
    sequence = sequence_entry.get()
    bwt_sequence = b.bwt_transform(sequence)[0]
    inverse_sequence = b.detransform_bwt(bwt_sequence)
    b.save_results(sequence, bwt_sequence, inverse_sequence)
    messagebox.showinfo("Sauvegerder",f"Transformation sauvegardee dans le fichier : bwt_results.txt")


# Créer une fenêtre
window = tk.Tk()

# Définir la taille de la fenêtre
window.geometry("400x300")

# Définir le titre de la fenêtre
window.title("BWT Transformation")

# Créer une étiquette pour le champ de saisie
label = tk.Label(window, text="Enter sequence ")
label.pack()

# Créer un champ de saisie
sequence_entry = tk.Entry(window)
sequence_entry.pack()

# Créer un bouton pour parcourir les fichiers
browse_button = tk.Button(window, text="Choose a FASTA file \n Browse", command=browse_file)
browse_button.pack()

# Créer un bouton pour la transformation
transform_button = tk.Button(window, text="Transform", command=transform_sequence)
transform_button.pack()

# Créer un bouton pour afficher les étapes de transformation en matrice
transform_button = tk.Button(window, text="Transform matrix", command=display)
transform_button.pack()

# Créer un bouton pour afficher les étapes de transformation
transform_button = tk.Button(window, text="Transform Step", command=display_steps)
transform_button.pack()

# Créer un bouton pour la détransformation
detransform_button = tk.Button(window, text="Detransform", command=detransform_sequence)
detransform_button.pack()

# Créer un bouton pour sauvegarder les résultats
detransform_button = tk.Button(window, text="Save", command=save_bwt)  # Non fonctionnel
detransform_button.pack()

# Lancer la boucle principale de la fenêtre
window.mainloop()
