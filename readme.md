- **Nom du projet** : Devoir #3
- **Numéro d’équipe** : 14
- **Objectif** : Développer un site web qui simule une application de calculatrice 

- **Prérequis d’installation** : 
    - Télécharger Python
    - Télécharger pip


# Description du but
L'application est une calculatrice servant à calculer des multiplications , additions, soustractions, divisions.

# La portée du projet
L'application permet à l'utilisateur d'effectuer les opérations arithmétiques de base :
- Addition
- Soustraction
- Multiplication
- Division

De plus, nous sommes capable de jouer avec les différents éléments mathématique suivants : 
- Les nombres naturels (représentés par des int) de [0,inf)
- Les nombres réels (représentés par les float) de (-inf,inf)

# Guide d’installation clair (étape par étape) et instructions d'utilisation

Voici les étapes une à une afin de pouvoir lancer l'application

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

#3 Installer les différentes dépendances avec la ligne de commande suivante  

```pip install -r requirements.txt ```

#4 Une fois que cela est fait, executer la ligne de code suivante  
``` 
python -m src.backend.app
 ```

#6 Une fois l'application construite, l'utiliser comme une calculatrice normale.

# Section sur les tests
Se référer au readme dans le répertoire de test qui couvre cette partie

# Section sur le flux de contribution (branches, PR, issues)

Nous avons fait pour chaque test échoué une isssue. De ce fait, nous avons créé les 7 issues suivantes :

- Bug : Le serveur Flask retourne une erreur 500
- Bug : Le test de calculer l'expression soustraction (test_calculate_sub) échoue
- Bug : Le test de calculer la multiplication(test_calculate_mul) échoue
- Bug : le test de multiplication par 0 (test_mul0) échoue
- Bug : le test de division (test_div) échoue
- Bug : le test de multiplication (test_mul) échoue
- Bug : le test de soustraction (test_sub) échoue

Nous avons fait une branche pour chaque issue à corriger. Certaines corrections ont corrigées d'autres bugs en même temps. Nous avons eu une problématique en plus lié au démarage de l'application avec notre nouvelle aménagement de fichier. De ce fait nous avons 5 branches à notre actif :

- main : la branche par défaut
- fix/test_mul0 : corrige le test test_mul0
- fix/test-div  : corrige le test test-div
- fix/test_calculate_sub : corrige le test test_calculate_sub
- fix/flask-server : corrige le problème du serveur flask lors du démarage de celui-ci.

En ce qui concerne les pull request, elles ont été assignées à un ou deux membres de l'équipe qui n'ont pas travaillés sur la branche à merge.
