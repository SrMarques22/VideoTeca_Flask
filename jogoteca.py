from flask import Flask, render_template

class Jogo:
    def __init__(self,nome, categoria, console):
        self.name=nome
        self.cat=categoria
        self.consol=console

# Para inicializar, pela primeira vez, uma aplicação feita em Flask, deve ser utilizado através do código abaixo: app = Flask(__name__)
app = Flask(__name__)

@app.route('/inicio')
def ola():
    '''
    Não foi precio adicionar um caminho para o return abaixo, apenas definir o nome do arquivo .html, devido
    ao Pytho já identificar que a estrutura .html fica em nome_projeto\templates, caso o nome do diretório
    não fosse template, ai então teriamos que definir um caminho!
    :return:
    '''
    jogo1 = Jogo('Donkey Kong','Adventure','Super Nintendo')
    jogo2 = Jogo('Shadow of the Colossus','Puzzle','Play Station')
    jogo3 = Jogo('Wild Rift','MOBA','Smartphone')
    lista = [jogo1,jogo2,jogo3]
    return render_template('lista.html',titulo='GameStation', jogos = lista) #dentro da variável titulo, realizamos a insersão do valor atribuido no arquivo lista.html

app.run()


#O route serve para criarmos a rota após o link de acesso, após a criarmos os passos acima, basta dar um RUN
# e testar no navegador o link disponibilizado no run do pycharm e colocar a /rota no final. ex: http://127.0.0.1:5000/inicio



