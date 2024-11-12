from flask import Flask, render_template,request,redirect,flash,session
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'PI02'

#caminhos definidos para as páginas
@app.route("/")
def cadastro():

    return render_template('cadastro.html')


@app.route('/login')
def index():

    return render_template('index.html')


@app.route('/loginPais')
def loginPais():

    return render_template('loginPais.html')


@app.route('/loginadministracao')
def loginadministracao():

    return render_template('loginadministracao.html')

@app.route('/layout')
def layout():

    return render_template('layout.html')


@app.route('/chamados')
def chamados():

    return render_template('chamados.html')

@app.route('/sair')
def sair():

    return render_template('index.html')

@app.route('/relatorio')
def relatorio():

    return render_template('documentos.html')


#verificação de usuário e senha para Pais
@app.route("/acessoPais", methods=['POST'])
def acessoPais():
    email = request.form.get('usuarioPais')
    senha = request.form.get('senhaPais')

    with open('Pais.json') as Pais_json:
        listaDeUsuarios = json.load(Pais_json)
        cont = 0
        for usuario in listaDeUsuarios:
            cont += 1

            if email == usuario['email'] and senha == usuario['senha']:
                return redirect('/layout')
            if cont >= len(listaDeUsuarios):
                flash('Email ou senha incorretos.')
                return redirect('/loginPais')

#verificação de usuário e senha para administracao 

@app.route("/acessoadministracao", methods=['POST'])
def acessoadministracao():
    usuario = request.form.get('usuarioadministracao')
    senha = request.form.get('senhaadministracao')

    if usuario == 'grupo10' and senha == '123':
        return redirect('/layout')
    else:
        return redirect('/loginadministracao')
    
#Enviar os dados dos cadastros de  Pais para o JSON


@app.route("/Paiscadastro", methods=['POST'])
def Paiscadastro():

    email = request.form.get('emailPais')
    nome = request.form.get('nomePais')
    senha = request.form.get('senhaPais')

    with open('Pais.json') as Pais_json:
        listaDeUsuarios = json.load(Pais_json)
        for usuario in listaDeUsuarios:
            if usuario['email'] == email:
                flash('Email já cadastrado.')
                return redirect('/loginPais')
            
    user = [
        {   
            "email": email,
            "nome": nome,
            "senha": senha,
        }
    ]

    novalista = listaDeUsuarios + user

    with open("Pais.json", 'w') as Pais_json:
        json.dump(novalista, Pais_json, indent=4)

    return redirect('/loginPais')





if __name__ in '__main__':
    app.run( debug=True )