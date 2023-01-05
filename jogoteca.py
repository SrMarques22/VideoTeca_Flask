#Projeto Videoteca Flask
from flask import Flask

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return '<h1>Olá Mundo!</h1>'

app.run()

#O route serve para criarmos a rota após o link de acesso, após a criarmos os passos acima, basta dar um RUN
# e testar no navegador o link disponibilizado no run do pycharm e colocar a /rota no final. ex: http://127.0.0.1:5000/inicio

