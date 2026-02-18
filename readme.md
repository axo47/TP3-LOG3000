- **Nom du projet** : Devoir #3
- **Numéro d’équipe** : 14
- **Objectif** : Développer un site web qui simule une application de calculatrice 

- **Prérequis d’installation** : 
    - Télécharger Python
    - Télécharger pip


# Description du but
L'application est une calculatrice servant à calculer des multiplications , additions, soustraction, division.

# La portée du projet
L'application permet à l'utilisateur d'effectuer les opérations arithmétiques de base :
- Addition
- Soustraction
- Multiplication
- Division

De plus, nous sommes capable de jouer avec les différents éléments mathématique suivants : 
- Les nombre naturel (représenté par des int) de [0,inf)
- Les nombre Réel (représenté par les float) de (-inf,inf)

# Guide d’installation clair (étape par étape)

Voici les étapes un à un afin de pouvoir lancer l'application

#1 Créer un venv à partir de la ligne de commande suivante  

```
python -m venv venv  ### pour windows  
python3 -m venv venv ### pour linux/macos
```

#2
Rentrer dans le fichier venv à l'aide de la ligne de commande
```
### Pour macos  
source venv/bin/activate  

### Pour Windows  
venv\Scripts\activate  
```

#3 Installer les différentes dépendance avec la ligne de commande suivante  

```pip install -r requirements.txt ```

#4 Execute les deux lignes de code suivant :  
```
cd src 
cd backend
``` 

#5 Une fois que cela est fait, nous pouvons executer la ligne de code suivante  
``` 
python app.py
 ```

#6 Une fois l'application construite : tu peux l'executer comme une calculatrice normal.

# Section sur les tests
Se référer au readme dans le repertoire de test qui couvre cette partie

# Section sur le flux de contribution (branches, PR, issues)

Nous avons en fait pour chaque test échoue un isssues. De ce fait, on a eu les 7 issues suivants :

- Bug : Le serveur Flask retourne une erreur 500
- Bug : Le test de calculer l'expression soustraction (test_calculate_sub) échoue
- Bug : Le test pour calculer la multiplication(test_calculate_mul) échoue
- Bug : le test de multiplication par 0 (test_mul0)échoue
- Bug : le test de division (test_div) échoue
- Bug : le test de multiplication (test_mul) échoue
- Bug : le test de substraction (test_sub) échoue

On a fait une branche pour chaque issues à corriger. Le problème, c'est que certains corrections corriger d'autres bug en même temps. Nous avons eu une problématique en plus lié au démarage de l'application avec notre nouvelle aménagement de fichier. De ce fait nous avons 5 branches à notre actif :

- main : la branche par défaut
- fix/test_mul0 : corrige le test test_mul0
- fix/test-div  : corrige le test test-div
- fix/test_calculate_sub : corrige le test test_calculate_sub
- fix/flask-server : corrige le problème du serveur flask lors du démarage de celui-ci.

En ce qui concerne les pull request : ils sont assigné soit à une personne de l'équipe en excluant celui qui était entrain de programmer sur cette branche ou les deux autres personnes de l'équipe qui n'ont pas travaillé sur cette branche.
