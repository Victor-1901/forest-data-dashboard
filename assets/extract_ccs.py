{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "41606e83-e831-485d-9661-049813c6f030",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Le fichier CSS n'a pas été trouvé dans les dossiers imbriqués.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "# Chemin du dossier \"assets\" imbriqué dans deux dossiers\n",
    "old_assets_path = \"C:/Users/victo/assets/assets\"\n",
    "new_assets_path = \"C:/Users/victo/assets\"  # Le chemin où tu veux mettre le fichier CSS\n",
    "\n",
    "# Le nom du fichier CSS\n",
    "css_file_name = \"fichier.css\"\n",
    "\n",
    "# Vérification si le fichier existe dans le dossier imbriqué\n",
    "old_css_path = os.path.join(old_assets_path, css_file_name)\n",
    "\n",
    "if os.path.exists(old_css_path):\n",
    "    # Si le fichier CSS existe, on va le déplacer\n",
    "    new_css_path = os.path.join(new_assets_path, css_file_name)\n",
    "\n",
    "    # Déplacer le fichier CSS dans le bon dossier\n",
    "    shutil.move(old_css_path, new_css_path)\n",
    "    print(f\"Fichier CSS déplacé vers : {new_css_path}\")\n",
    "\n",
    "    # Supprimer les dossiers inutiles\n",
    "    shutil.rmtree(old_assets_path)\n",
    "    print(f\"Dossiers inutiles supprimés : {old_assets_path}\")\n",
    "else:\n",
    "    print(\"Le fichier CSS n'a pas été trouvé dans les dossiers imbriqués.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b610879d-e0cf-4659-8dd3-b99ebaa6a5d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Le fichier CSS a été trouvé à : C:/Users/victo\\fichier.css\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Répertoire de départ\n",
    "start_dir = \"C:/Users/victo\"\n",
    "\n",
    "# Nom du fichier CSS\n",
    "css_file_name = \"fichier.css\"\n",
    "\n",
    "# Fonction pour rechercher le fichier dans tous les sous-dossiers\n",
    "def find_file(start_dir, file_name):\n",
    "    for root, dirs, files in os.walk(start_dir):\n",
    "        if file_name in files:\n",
    "            return os.path.join(root, file_name)\n",
    "    return None\n",
    "\n",
    "# Recherche du fichier CSS\n",
    "css_file_path = find_file(start_dir, css_file_name)\n",
    "\n",
    "if css_file_path:\n",
    "    print(f\"Le fichier CSS a été trouvé à : {css_file_path}\")\n",
    "else:\n",
    "    print(f\"Le fichier CSS '{css_file_name}' n'a pas été trouvé dans '{start_dir}'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb52c191-c5a6-4f70-819e-fad808f35350",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
