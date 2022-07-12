import mysql.connector
import conexao
import this
this.msg = ""

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserirFunc(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo):
    try:
        sql = "insert into funcionario(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo) values('','{}','{}','{}','{}','{}','{}')".format(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        return con.rowcount, "Inserido!"
    except Exception as erro:
        return erro

#Consultar os dados do BD
def selecionar_func(nome):
    try:
        sql = "select * from funcionario where nomeFunc = '{}'".format(nome)
        con.execute(sql)

        this.msg = ""
        this.msg = " Nenhum Funcionário Encontrado! "
        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo) in con:
            if nomeFunc == nome:
                this.msg = "Código: {}, Nome: {}, CPF: {}, Celular: {}, Salário {}, Senha: {}, Cargo: {}".format(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro

#Consultar os dados do BD
def selecionar_func_cod(codigo):
    try:
        sql = "select * from funcionario where codigoFunc = '{}'".format(codigo)
        con.execute(sql)

        this.msg = ""
        this.msg = " Nenhum Funcionário Encontrado!"
        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo) in con:
            if codigoFunc == int(codigo):
                this.msg = "Código: {}, Nome: {}, CPF: {}, Celular: {}, Salário {}, Senha: {}, Cargo: {}".format(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc, cargo)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro

#Atualizar dados no banco de dados
def atualizarFunc(nomeFunc, campo, novoDado):
    try:
        sql = "update funcionario set {} = '{}' where nomeFunc = '{}'".format(campo, novoDado, nomeFunc)
        con.execute(sql)
        db_connection.commit()
        return " {} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return(erro)

def excluirFunc(codigoFunc):
    try:
        sql = "delete from funcionario where codigoFunc = '{}'".format(codigoFunc)
        con.execute(sql)
        db_connection.commit()
        return " {} Deletado do Sistema!".format(con.rowcount)
    except Exception as erro:
        return erro

def atualizarNome(codigoFunc, nomeFunc):
    try:
        sql = "update funcionario set {} = '{}' where codigoFunc = '{}'".format(nomeFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        return con.rowcount, "Atualizado!"
    except Exception as erro:
        return(erro)

def atualizarCelular(codigoFunc, celularFunc):
    try:
        sql = "update funcionario set celularFunc = '{}' where codigoFunc = '{}'".format(celularFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizaSalario(codigoFunc, salarioFunc):
    try:
        sql = "update funcionario set salarioFunc = '{}' where codigoFunc = '{}'".format(salarioFunc, codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualzado!")
    except Exception as erro:
        print(erro)

def atualizarSenha(codigoFunc, senhaFunc):
    try:
        sql = "update funcionario set senhaFunc = '{}' where codigoFunc = '{}'".format(senhaFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigoFunc):
    try:
        sql = "delete from funcionario where codigoFunc = '{}'".format(codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)