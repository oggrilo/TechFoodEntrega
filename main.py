import menuADM
import menuCliente
import login
from flask import Flask, render_template, request, flash, url_for

import operacoesFunc
import operacoesLogin
import operacoesLanche
import this

#var_lanches
this.nomeLanche = ""
this.descricaoLanche = ""
this.valorLanche = 0
this.quantidadeLanche = 0
codigoLanche = ""

#var_func
this.nomeFunc = ""
this.cpfFunc = ""
this.celularFunc = ""
this.salarioFunc = ""
this.senhaFunc = ""
this.cargo = ""

this.campo = ""

this.nDado = ""
this.dados = ""
this.dado = ""

this.mensagem = ""

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET', 'POST'])
def pag_inicial():
    return render_template('/index.html', titulo='Página Principal')

#cadastrar Funcionário
@pessoa.route('/cadastrarFunc.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nomeFunc = request.form['tNovoNomeFunc']
        this.cpfFunc = request.form['tNovoCpfFunc']
        this.celularFunc = request.form['tNovoCelularFunc']
        this.salarioFunc = request.form['tNovoSalarioFunc']
        this.senhaFunc = request.form['tNovoSenhaFunc']
        this.cargo = request.form['Cargo']

        if operacoesLogin.cpf_validate(this.cpfFunc) == True:
            this.dados = operacoesFunc.inserirFunc(this.nomeFunc, this.cpfFunc, this.celularFunc, this.salarioFunc, this.senhaFunc, this.cargo)
            return render_template('/cadastrarFunc.html', titulo='Página De Cadastro Dos Funcionário', resultado=this.dados)
        else:
            this.dados = "CPF não é válido, favor cadastrar com CPF existente!"
    return render_template('/cadastrarFunc.html', titulo='Página De Cadastro Dos Funcionário', resultado=this.dados)


#consultar Funcionário por nome
@pessoa.route('/consultarFunc.html', methods=['GET', 'POST'])
def consultar_por_nome():
    if request.method == 'POST':
        this.nomeFunc = request.form['tNovoNomeFunc']
        this.mensagem = operacoesFunc.selecionar_func(this.nomeFunc)
    else:
        this.mensagem = ""
    return render_template('/consultarFunc.html', titulo='Página De Consulta Dos Funcionários', dados=this.mensagem)

#atualizar dados do funcionário
@pessoa.route('/atualizarFunc.html', methods=['GET', 'POST'])
def atualizarDados():
    if request.method =='POST':
        this.nomeFunc = request.form['tNomeFunc']
        this.campo = request.form['Campo']
        this.novoDado = request.form['tNovoDado']
        this.dados = operacoesFunc.atualizarFunc(this.nomeFunc, this.campo, this.novoDado)
    return render_template('/atualizarFunc.html', titulo='Página De Atualização Dados Do Funcionário', resultado=this.dados)

#excluir algum funcionário
@pessoa.route('/excluirFunc.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method =='POST':
        this.codigo = request.form['tCodigoFunc']
        this.mensagem = operacoesFunc.selecionar_func_cod(this.codigo)
        this.dados = operacoesFunc.excluirFunc(this.codigo)
    return render_template('/excluirFunc.html', titulo='Excluir Funcionário', valor=this.mensagem, resultado=this.dados)


#-------------------------------------------------------------------------------------------------------#


#cadastrar lanche
@pessoa.route('/cadastrarLanche.html', methods=['GET', 'POST'])
def cadastrarLanche():
    if request.method == 'POST':
        if request.form['tNovoNome'] == "" or request.form['tNovaDescricao'] == "" or request.form['tNovaQuantidade'] == "" or request.form['tNovoValor'] == "":
            this.dados = "Preencha todos os campos acima, por favor!"
        else:
            this.nomeLanche       = request.form['tNovoNome']
            this.descricaoLanche  = request.form['tNovaDescricao']
            this.quantidadeLanche = request.form['tNovaQuantidade']
            this.valorLanche      = request.form['tNovoValor']
            this.dados = operacoesLanche.inserir(this.nomeLanche, this.descricaoLanche, this.quantidadeLanche, this.valorLanche)
    return render_template('/cadastrarLanche.html', titulo='Cadastrar Lanche', resultado=this.dados)

#consultar lanches
@pessoa.route('/consultarLanche.html', methods=['GET', 'POST'])
def consultar():
    if request.method == 'POST':
        this.mensagem = operacoesLanche.selecionar()
    return render_template('/consultarLanche.html', titulo='Consultar Lanches', dados=this.mensagem)

#atualizar lanches
@pessoa.route('/atualizarLanche.html', methods=['GET','POST'])
def atualizar():
    if request.method == 'POST':
        if request.form['tCodigo'] == "" or request.form['tCampo'] == "" or request.form['tNovoDado'] == "":
            this.dado = "Preencha todos os campos acima, por favor!"
        else:
            this.codigo = request.form['tCodigo']
            this.campo  = request.form['tCampo']
            this.nDado  = request.form['tNovoDado']
            this.dado = operacoesLanche.atualizar(this.codigo, this.campo, this.nDado)
    return render_template('/atualizarLanche.html', titulo='Atualizar Lanche', dados=this.dado)

#deletar lanches
@pessoa.route('/excluirLanche.html', methods=['GET', 'POST'])
def deletar():
        if request.method == 'POST':
            if request.form['tCodigo'] == "":
                this.dado = "Preencha todos os campos acima, por favor!"
            else:
                    this.codigo = request.form['tCodigo']
                    this.mensagem = operacoesLanche.excluir(this.codigo)
        return render_template('/excluirLanche.html', titulo='Deletar Lanche', resultado=this.mensagem)

#compra de lanches
@pessoa.route('/compra.html', methods=['GET', 'POST'])
def compra():
        if request.method == 'POST':
            if request.form['tCampo'] == "" or request.form['tQuantidade'] == "":
                this.msg = "Preencha todos os campos acima, por favor!"
            else:
                    this.campo = request.form['tCampo']
                    this.quantidadeLanche = float(request.form['tQuantidade'])
                    this.msg = operacoesLanche.totalCompra(this.campo, this.quantidadeLanche)
        return render_template('/compra.html', titulo='Comprar Lanche', resultado=this.msg)


if __name__ == "__main__":
    pessoa.run(debug=True, port=5000)
    #login.escolhas()
    #menuADM.operacao()
    #menuCliente.operacao()