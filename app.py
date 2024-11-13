from flask import Flask, render_template,request,redirect,flash,session
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'PI02'


#verificação de usuário e senha para Pais
@app.route("/acessoPais", methods=['POST'])
def acessoPais():
    email = request.form.get('usuarioPais')
    senha = request.form.get('senhaPais')

    with open('cadastros.json') as Pais_json:
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

    with open('cadastros.json') as Pais_json:
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

    with open("cadastros.json", 'w') as Pais_json:
        json.dump(novalista, Pais_json, indent=4)

    return redirect('/loginPais')





if __name__ in '__app__':
    app.run( debug=True )