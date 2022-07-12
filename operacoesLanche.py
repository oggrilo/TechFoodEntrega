import conexao
import this
from flask import Flask, render_template, request
this.msg = ""

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserir(nomeLanche, descricaoLanche, quantidadeLanche, valorLanche):
    try:
        sql = "insert into lanche(codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) values('','{}','{}','{}', '{}')".format(nomeLanche, descricaoLanche, quantidadeLanche, valorLanche)
        con.execute(sql)#Prepara o comando para ser executado

        this.msg = ""
        db_connection.commit()#Executa o comando no banco de dados
        return  con.rowcount, "Inserido!"
    except Exception as erro:
        return erro

#Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        this.msg = ""
        for (codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
            this.msg = this.msg + "  #LANCHE {} ----> Código: {} | Nome: {} | Descrição: {} | Quantidade: {} | Valor do Lanche: {} |||".format(codigoLanche, codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche)
        return this.msg
    except Exception as erro:
        print(erro)

def selecionarValor():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        this.msg = ""
        for (valorLanche) in con:
            this.msg = this.msg + "Valor do Lanche: {}".format(valorLanche)
    except Exception as erro:
        print(erro)

def selecionarQuantidade():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        this.msg = ""
        for (quantidadeLanche) in con:
            this.msg = this.msg + "Quantidade do Lanche: {}".format(quantidadeLanche)
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNome(codigoLanche, nomeLanche):
    try:
        sql = "update lanche set nomeLanche = '{}' where codigoLanche = '{}'".format(nomeLanche,codigoLanche)
        con.execute(sql)

        this.msg = ""
        db_connection.commit()
        this.msg = this.msg + con.rowcount, "Atualizada!"
    except Exception as erro:
        print(erro)

def atualizarDescricao(codigoLanche, descricaoLanche):
    try:
        sql = "update lanche set descricaoLanche = '{}' where codigoLanche = '{}'".format(descricaoLanche,codigoLanche)
        con.execute(sql)

        this.msg = ""
        db_connection.commit()
        this.msg = this.msg + con.rowcount, "Atualizada!"
    except Exception as erro:
        print(erro)

def atualizarValor(codigoLanche, valorLanche):
    try:
        sql = "update lanche set valorLanche = '{}' where codigoLanche = '{}'".format(valorLanche,codigoLanche)
        con.execute(sql)

        this.msg = ""
        db_connection.commit()
        this.msg = this.msg + con.rowcount, "Atualizada!"
    except Exception as erro:
        print(erro)

def atualizarQuantidade(codigoLanche, quantidadeLanche):
    try:
        sql = "update lanche set quantidadeLanche = '{}' where codigoLanche = '{}'".format(quantidadeLanche,codigoLanche)
        con.execute(sql)

        this.msg = ""
        db_connection.commit()
        this.msg = this.msg + con.rowcount, "Atualizada!"
    except Exception as erro:
        print(erro)

def atualizar(codigo, campo, novoDado):
    try:
        sql = "update lanche set {} = '{}' where codigoLanche = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def excluir(codigoLanche):
    try:
        sql = "delete from lanche where codigoLanche = '{}'".format(codigoLanche)
        con.execute(sql)
        db_connection.commit()

        return "{} Deletado!".format(con.rowcount)
    except Exception as erro:
        print(erro)

def compra(nomeLanche, quantidadeBD, quantidadeEscolhida):
    quantidadeLanche = quantidadeBD - quantidadeEscolhida
    try:
        sql = "update lanche set quantidadeLanche = '{}' where nomeLanche = '{}'".format(quantidadeLanche, nomeLanche)
        con.execute(sql)
        db_connection.commit()

    except Exception as erro:
        return erro

def totalCompra(nomeLanche, quantidade):
    try:
        sql = "select valorLanche from lanche where nomelanche = '{}'".format(nomeLanche)
        con.execute(sql)

        for(codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
            valor = valorLanche
            quantidadeBanco = quantidadeLanche
            this.msg = ""
            compra(nomeLanche, quantidadeBanco, quantidade)
        return "O total da compra é: " + (valor*quantidade) + "O código do PIX é 12345678912, acesse https://www.picpay.com/site para efetuar pagamento."
    except Exception as erro:
      return erro

##def compraLanche(nomeLanche, quantidadeLanche, valorLanche):
   # quantidadeLanche * valorLanche
    #try:
   #     sql = "select valorLanche * from lanche where nomeLanche = '{}'".format(nomeLanche)
    #    con.execute(sql)

     #   for(codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
      #      this.msg = "Nome lanche: {}, Valor do lanche: {}".format(nomeLanche, valorLanche)

    #except Exception as erro:
      #  return erro