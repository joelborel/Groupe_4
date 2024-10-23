from loguru import logger

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
       
        logger.add("file_manager.log", format="{time} {level} {message}", level="INFO")
    
   
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                logger.info(f"Lecture du fichier {self.file_path} réussie.")
                print(content)
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")


    def write_to_file(self, data):
        try:
            with open(self.file_path, 'a') as file:
                file.write(data + '\n')
                logger.info(f"Données ajoutées au fichier {self.file_path} : {data}")
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture dans le fichier {self.file_path}: {e}")

    def count_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                logger.info(f"Nombre de lignes dans {self.file_path} : {len(lines)}")
                return len(lines)
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")
            return 0

    def search_keyword(self, keyword):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                matches = []
                for num, line in enumerate(lines, 1):
                    if keyword in line:
                        matches.append((num, line.strip()))
                        logger.info(f"Mot-clé '{keyword}' trouvé à la ligne {num}.")
                return matches
        except FileNotFoundError:
            logger.error(f"Le fichier {self.file_path} n'existe pas.")
            return []
