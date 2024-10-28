from file_manager import FileManager

def afficher_menu():
    print("\n------MENU------ ")
    print("1. Lire le fichier")
    print("2. Écrire dans le fichier")
    print("3. Compter les lignes")
    print("4. Rechercher un mot-clé")
    print("5. Quitter")

def gerer_choix(file_manager, essais_restants):
    if essais_restants == 0:
        print("Nombre maximum de tentatives incorrectes atteint. Fin du programme.")
        return  # Arrête le programme si les tentatives sont épuisées
    
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == '1':
        file_manager.read_file()
    elif choix == '2':
        contenu = input("Entrez le contenu à écrire : ")
        file_manager.write_to_file(contenu)
    elif choix == '3':
        print(f"Nombre de lignes : {file_manager.count_lines()}")
    elif choix == '4':
        keyword = input("Entrez le mot-clé à rechercher : ")
        file_manager.search_keyword(keyword)
    elif choix == '5':
        print("Au revoir !")
        return  # Quitte la fonction main et termine le programme
    else:
        essais_restants -= 1  # Décrémente le compteur seulement en cas d’option invalide
        print(f"Choix invalide. Il vous reste {essais_restants} tentatives.")
    
    # Appel récursif pour continuer à interagir avec l'utilisateur
    gerer_choix(file_manager, essais_restants)

def main():
    file_path = 'log.txt'  # Chemin vers le fichier log.txt
    file_manager = FileManager(file_path)
    essais_restants = 5  # Limite des tentatives pour choix invalide
    gerer_choix(file_manager, essais_restants)

if __name__ == "__main__":
    main()
