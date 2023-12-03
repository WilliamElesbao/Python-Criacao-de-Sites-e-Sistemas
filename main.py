# importar flask
from flask import Flask, render_template

# criar o aplicativo
app = Flask(__name__)

# criar a 1ª página = 1ª rota
    # hashtagtreinamentos.com
    # /blog # rotas
    # /python # rotas
    # /power-bi # rotas

@app.route("/") # decorator - atribui funcionalidade para a funcao
def homepage():
    return render_template("homepage.html")


# rodar o aplicativo

# app.run(debug=True)
#  → debug=True para nao ficar startando toda hora
#  o projeto, mas ao final do projeto
#  precisa ser removido

app.run(debug=True) 



