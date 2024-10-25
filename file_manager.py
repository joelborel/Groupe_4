class FileManager:
    """Classe pour gérer les opérations de fichiers comme la lecture et l'écriture."""
    def __init__(self, file_path):
        """Initialise le gestionnaire de fichiers avec un chemin de fichier donné."""
        self.file_path = file_path

    def read_file(self):
        """Affiche le contenu complet du fichier."""
        with open(self.file_path, 'r') as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)

    def write_to_file(self, data):
        """Ajoute une nouvelle ligne de texte à la fin du fichier."""
        try:
            with open(self.file_path, 'a') as file:
                file.write(data + '\n') 
                print("Les données ont été ajoutées à la fin du fichier.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")
            
    def count_lines(self):
        """Compte le nombre de lignes dans le fichier."""
        try:
            with open(self.file_path, 'r') as file:
                nbr_lignes = file.readlines()  
                return len(nbr_lignes)  
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
            
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
        
            
    def search_keyword(self, keyword):
        """"Recherche et affiche les lignes contenant un mot-clé spécifique."""
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print(f"Le mot-clé '{keyword}' n'a pas été trouvé.")
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la recherche du mot-clé : {e}")
