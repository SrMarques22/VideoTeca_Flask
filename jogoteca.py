from flask import Flask, render_template, request, redirect, session, flash
#Vamos instalar o BootStrap para aglizar e facilitar  os layouts CSS da nossa aplicação, através do link abaixo
# mas sempre se deve verificar a versão antes:
# https://getbootstrap.com/docs/5.1/getting-started/download/
# após baixado, abrir a pasta CSS e pegar apenas o arquivo botstrap.css copiar e criar a pasta static dento do projeto e colar dentro
# depois referenciamos ele nos arquivos .html no <head> com a linha <link rel="stylesheet" href="../static/bootstrap.css">,


#Session é um recurso do Flask que permite um armazenamento temporário de dados que persiste as
# informações coletadas por mais de um ciclo de request.Isso é feito através do armazenamento
# dos dados no Client-side (Lado do cliente) da aplicação, ou seja, no navegador, através dos cookies

class Jogo:
    def __init__(self,nome, categoria, console):
        self.name=nome
        self.cat=categoria
        self.consol=console

#Colocamos a lista com os games fora do DEF para que as variáveis se tornem GLOBAIS
jogo1 = Jogo('Donkey Kong','Adventure','Super Nintendo')
jogo2 = Jogo('Shadow of the Colossus','Puzzle','Play Station')
jogo3 = Jogo('Wild Rift','MOBA','Smartphone')
lista = [jogo1,jogo2,jogo3]

# Para inicializar, pela primeira vez, uma aplicação feita em Flask, deve ser utilizado através do código abaixo: app = Flask(__name__)
app = Flask(__name__)
#é necessário colocar essa chave abaixo, com o valor que preferir para que o navegador aceite os cookies, é uma camada de segurança
app.secret_key='alura'


#OBS: O APP.ROUTE deve ficar antes do seu respectivo def!
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #o ?proxima=novo serve para me redirecionar para a pagina certa após tentar acessa-la e não tiver sucesso pois não estou logado
        return redirect('/login?proxima=novo')

    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/')
def index():
    '''
    Não foi precio adicionar um caminho para o return abaixo, apenas definir o nome do arquivo .html, devido
    ao Pytho já identificar que a estrutura .html fica em nome_projeto\templates, caso o nome do diretório
    não fosse template, ai então teriamos que definir um caminho!
    :return:
    '''

    return render_template('lista.html',titulo='GameStation', jogos = lista) #dentro da variável titulo, realizamos a insersão do valor atribuido no arquivo lista.html



@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    #Colocamos o redirect para voltar a pagina inicial sempre que for utilizada a função criar, o / é a nossa página principal
    return redirect('/')



@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/logout')
def logout():
    session['usuario_logado']=None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'admin' == request.form['senha']: #O request pega as informações do formulario
        session['usuario_logado'] = request.form['usuario']
        #flash é o responsável pelos avisos
        flash(session['usuario_logado']+" logado com sucesso!")
        proxima_pagina = request.form['proxima']
        return redirect(f'/{proxima_pagina}')
    else:
        flash('Usuário não logado.')
        return redirect('/login')


#Para executar o debugger e facilitar os ajustes sem ter que dar stop e start na aplicação:
app.run(debug=True)
#app.run()


#O route serve para criarmos a rota após o link de acesso, após a criarmos os passos acima, basta dar um RUN
# e testar no navegador o link disponibilizado no run do pycharm e colocar a /rota no final. ex: http://127.0.0.1:5000/inicio



