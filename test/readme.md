# 1 But
Le module de test sert à vérifier que les opérations de la calculatrice fonctionnent comme attendu.
Il permet de détecter rapidement les régressions quand on modifie le code du backend.
# 2 Les principaux fichiers qu’il contient et leurs responsabilités.
test.py : contient les tests unitaires des fonctions `add`, `subtract`, `multiply`, `divide` et des tests de la fonction `calculate` avec différentes expressions.
# 3 Hypothèse et dépendance
Dépendance : `pytest` pour l’exécution des tests.
Hypothèse : les fonctions importées depuis `src/operators.py` et `src/app.py` gardent la même signature.
# 4 Comment executer les test
Depuis la racine du projet, executer la commande suivante dans le répertoire test :
python -m pytest test/test.py
NB : vérifier bien d'avoir activer le fichier venv (voir le readme principale à cette effet)
# 5 Ce que les tests couvrent
Nous avons 12 différents cas de tests : 
- 4 tests sont pour vérifier les entrés sorties. Le a et le b ont été choisi de manière arbitraire en tant qu'entrée.
- 4 tests sont pour vérifier le cas du 0 en tant que paramètre b afin de ressortir différentes propriétés.
- 4 tests sont pour vérifier les entrées/sorties de la fonction calculate.


