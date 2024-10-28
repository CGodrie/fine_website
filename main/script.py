
import os
from django.core.files import File
from main.models import CAFile  # Remplacez 'main' par le nom correct de votre application
from django.conf import settings

# Chemin du dossier où se trouvent vos fichiers
ca_files_directory = r'C:\Users\clemg\Desktop\Perso\Web\FINE\ca_files'

# Parcourir tous les fichiers du dossier
for filename in os.listdir(ca_files_directory):
    file_path = os.path.join(ca_files_directory, filename)

    if os.path.isfile(file_path):  # Vérifier si c'est bien un fichier
        with open(file_path, 'rb') as f:  # Ouvrir le fichier en mode binaire
            # Retirer l'extension du nom de fichier
            base_name, ext = os.path.splitext(filename)

            # Créer une nouvelle instance de CAFile
            ca_file = CAFile(title=base_name)  # Utilisez 'title' ou le champ correct
            ca_file.file.save(filename, File(f), save=True)  # Enregistrer le fichier dans le modèle
            print(f"Ajouté : {base_name}")  # Afficher le nom sans l'extension