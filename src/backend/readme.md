# But 
La partie back-end sert à réaliser la requête http envoyé par le front-end

# Les principaux fichiers qu’il contient et leurs responsabilités.
*app.py* : récupère la requête http réalisé par le serveur et si c'est une requête avec une methode post on réalise le calcul de l'expression du client. \
*operators.py* : défini les différents opérateurs qui seront utilisés dans la calculatrice

# Hypothèse et dépendance 
Nous avons la dépendance de ```Flask``` qui est une librairie python.