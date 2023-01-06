from flask import Flask, render_template


app = Flask(__name__)

@app.route('/inicio')
def ola():
    '''
    Não foi precio adicionar um caminho para o return abaixo, apenas definir o nome do arquivo .html, devido
    ao Pytho já identificar que a estrutura .html fica em nome_projeto\templates, caso o nome do diretório
    não fosse template, ai então teriamos que definir um caminho!
    :return:
    '''
    return render_template('lista.html')

app.run()


#O route serve para criarmos a rota após o link de acesso, após a criarmos os passos acima, basta dar um RUN
# e testar no navegador o link disponibilizado no run do pycharm e colocar a /rota no final. ex: http://127.0.0.1:5000/inicio



