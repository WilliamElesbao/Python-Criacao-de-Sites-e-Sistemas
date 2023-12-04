# pip install python-socketio flask-socketio simple-websocket
# http://127.0.0.1:5000/ → IP/endereço do localhost, por padrão o flask usa a porta 5000

# importar flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# criar o aplicativo
app = Flask(__name__)

# tunel para enviar as mensagens
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a 1ª página = 1ª rota
    # https://github.com/WilliamElesbao/
    # /Python-Criacao-de-Sites-e-Sistemas # rotas
    # /Python-AI-e-Previsoes # rotas
    # /Python-Automacao-Web # rotas

@app.route("/") # decorator - atribui funcionalidade para a funcao
def homepage():
    return render_template("index.html")

# rodar o aplicativo

# app.run(debug=True) → debug=True para nao ficar startando toda hora o projeto, mas ao final do projeto precisa ser removido
# app.run(debug=True) 

# (app, host="localhost") → localhost: rodar localmente na sua máquina para fazer os testes iniciais
# (app, host="192.168.0.104") → IP: disponibilizar o acesso para sua rede interna ter acesso
socketio.run(app, host="192.168.0.104")

# websocket → tunel

