from file_manager import FileManager

# Chemin du fichier à manipuler
file_path = "log.txt"

# Créer une instance de FileManager
file_manager = FileManager(file_path)

# Menu pour choisir l'action à effectuer
def afficher_menu():
    print("\nQue voulez-vous faire ?")
    print("1. Lire le fichier")
    print("2. Écrire dans le fichier")
    print("3. Quitter")

# Boucle principale pour interagir avec l'utilisateur
while True:
    afficher_menu()
    choix = input("Entrez le numéro de votre choix: ")

    if choix == '1':
        # Lire le fichier
        print("\nLecture du fichier:")
        file_manager.read_file()

    elif choix == '2':
        # Écrire dans le fichier
        data = input("Entrez le texte à ajouter au fichier: ")
        file_manager.write_to_file(data)
        print(f"Le texte '{data}' a été ajouté au fichier.")
  
    elif choix == '3':
        # Quitter le programme
        print("Au revoir!")
        break


    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3 ")
