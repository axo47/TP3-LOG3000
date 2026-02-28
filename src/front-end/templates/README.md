# 1 But
Le module `templates` sert à contenir les pages HTML pour afficher l’interface de la calculatrice dans le navigateur.
# 2 Les principaux fichiers qu’il contient et leurs responsabilités.
index.html : page principale de l’application; contient la structure HTML de la calculatrice, le formulaire d’entrée et l’affichage du résultat.
# 3 Hypothèse et dépendance
Hypothèse : le backend envoie les variables attendues par le template.

Dépendance : ce dossier est utilisé par Flask comme `template_folder`.
