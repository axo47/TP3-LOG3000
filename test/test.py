from src.backend.app import app, calculate
from src.backend.operators import add, subtract, multiply, divide
import pytest

def test_add():
    """
    But : vérifier l'entré/sortie de la fonction d'addition
    """
    assert add(2,3) == 5

def test_add0():
    """
    But : Vérifier que l'addition de n'importe quelle nombre avec 0 donne lui même 
    """
    assert add(2,0) == 2

def test_sub():
    """
    But : vérifier l'entré/sortie de la fonction de soustraction
    """
    assert subtract(2,3) == -1

def test_sub0():
    """
    But : Vérifier que la soustraction de n'importe quelle nombre avec 0 donne lui même 
    """
    assert add(2,0) == 2

def test_mul():
    """
    But : vérifier l'entré/sortie de la fonction de multiplication 
    """
    assert multiply(2,3) == 6

def test_mul0():
    """
    But : Vérifier que la multiplication de n'importe quelle nombre avec 0 donne 0
    """
    assert multiply(2,0) == 0

def test_div():
    """
    But : vérifier l'entré/sortie de la fonction de division 
    """
    assert divide(2,3) == 2/3

def test_div0():
    """
    But : Vérifier que la division de n'importe quelle nombre avec 0 donne une erreur
    """
    with pytest.raises(ZeroDivisionError):
            divide(2, 0)

def test_calculate_add():
    """
    But : vérifier l'execution de calculate pour l'addition
    """
    assert calculate("10+5") == 15

def test_calculate_mul():
    """
    But : vérifier l'execution de calculate pour la multiplication
    """
    assert calculate("10*5") == 50

def test_calculate_div():
    """
    But : vérifier l'execution de calculate pour la division
    """
    assert calculate("10/5") == 2

def test_calculate_sub():
    """
    But : vérifier l'execution de calculate pour la soustraction
    """
    assert calculate("10-5") == 5