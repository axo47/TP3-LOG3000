from flask import Flask, request, render_template
from src.operators import add, subtract, multiply, divide

app = Flask(
    __name__, template_folder="front-end/templates", static_folder="front-end/static"
)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule l'expression selon les opérations d'addition, 
    de soustraction , de multiplication et de division

    Paramètres l'expresision (ex: a+b)

    Il va prendre le a et le b et les transformer en float 

    Retourne: un float qui est le resultat de l'opération
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Middleware vérifiant les différents requête http executé 
    Paramètres : rien
    Retourne: un float si la méthode de la requet est post (appelle la fonction calculate) ou rien si c'est un autre type de requête.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)