# 1 Comment executer les test
Voici les étapes:

#1 Allumer le terminal et  aller dans le répertoire test à l'aide de la commande 
```
cd test
```
#2 Executer la ligne de commande suivante : 
```
python -m pytest test/test.py
```


NB : vérifier bien d'avoir activer le fichier venv (voir le readme principale à cette effet)


# 2 Ce que les tests couvrent

Nous avons 12 différents tests 

- 4 vérifient les entrées sorties. Le a et le b ont été choisies de manière arbitraire.
- 4 vérifient le cas du 0 comme paramètre b afin d'en ressortir les différentes propriétés.
- 4 vérifient les entrées/sorties de la fonction calculate.