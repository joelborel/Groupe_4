from loguru import logger

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
       
        logger.add("file_manager.log", format="{time} {level} {message}", level="INFO")
    
   # lire dans le fichier
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                logger.info(f"Lecture du fichier {self.file_path} réussie.")
                print(content)
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")

    # ecrire dans le fichier
    def write_to_file(self, data):
        try:
            with open(self.file_path, 'a') as file:
                file.write(data + '\n')
                logger.info(f"Données ajoutées au fichier {self.file_path} : {data}")
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture dans le fichier {self.file_path}: {e}")
           
           #pour compter nombre de lignes dans le fichier
    def count_lines(self):
        
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                count = len(lines)
                logger.info(f"Le fichier {self.file_path} contient {count} lignes.")
                return count
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")
            return 0

# pour rechercher un mot-clé dans le fichier.
    def search_keyword(self, keyword):
        
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                matches = [line for line in lines if keyword in line]
                if matches:
                    logger.info(f"Mots-clés '{keyword}' trouvés dans {self.file_path}.")
                    for match in matches:
                        print(match.strip())
                else:
                    logger.warning(f"Aucun match trouvé pour le mot-clé '{keyword}' dans {self.file_path}.")
                    print(f"Aucun match trouvé pour le mot-clé '{keyword}'.")
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")

    
        
