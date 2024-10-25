Ce projet est une application Python simple pour gérer un fichier texte. Elle permet de lire le contenu du fichier, d’y ajouter des données, de rechercher des mots-clés, et de compter le nombre de lignes.

Les actions effectuées dans le fichier sont enregistrées dans un fichier de logs file_manager.log pour suivre l’historique des opérations.

Fonctionnalités

	1.	Lire le contenu du fichier : Affiche tout le contenu du fichier dans le terminal.
	2.	Écrire dans le fichier : Permet d’ajouter une nouvelle ligne de texte.
	3.	Rechercher un mot-clé : Recherche un mot spécifique et affiche les lignes correspondantes.
	4.	Compter le nombre de lignes : Affiche le nombre de lignes présentes dans le fichier.
	5.	Enregistrer les actions : Tous les changements et actions sont enregistrés dans un fichier de logs file_manager.log.

Pré-requis

	•	Python  doit être installé sur l’ordinateur.
	•	La bibliothèque loguru est utilisée pour gérer les logs. Vous pouvez l’installer via pip :

pip install loguru

Installation et utilisation

	1.	Clonez le projet grâce la commande git clone https://github.com/joelborel/Groupe_4/
	2.	Dans le dossier du projet, ouvrez un terminal et installez loguru si ce n’est pas déjà fait :
“pip install loguru”

	3.	Lancez le programme en exécutant la commande suivante :

python main.py


	4.	Dans le menu, choisissez l’action souhaitée en tapant le numéro correspondant :
	•	1 pour lire le fichier
	•	2 pour écrire dans le fichier
	•	3 pour rechercher un mot-clé
	•	4 pour compter les lignes

Fichier de logs

Les actions effectuées dans le fichier sont enregistrées dans un fichier file_manager.log.
