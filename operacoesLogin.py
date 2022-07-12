import mysql.connector
import conexao
import menuCliente
import menuADM
import login
from random import randint
db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def loginCliente(cpfCliente,senhaCliente):
    try:
            sql = "select * from cliente where cpfCliente = '{}' and senhaCliente = '{}'".format(cpfCliente,senhaCliente)
            con.execute(sql)

            for (codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) in con:
                print(cpfCliente, senhaCliente)
            return menuCliente.operacao()('Logado como CLIENTE!!!\n')
    except Exception as erro:
        print(erro)
def loginFunc(cpfFunc,senhaFunc):
    try:
        sql = "select * from funcionario where cpfFunc = '{}' and senhaFunc = '{}'".format(cpfFunc, senhaFunc)
        con.execute(sql)

        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) in con:
            print(cpfFunc, senhaFunc)
        print('Logado como ADM!!!\n')
        return menuADM.operacao()
    except Exception as erro:
        print(erro)



def inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente):
    try:
        sql = "insert into cliente(codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) values('','{}','{}','{}','{}')".format(nomeCliente, cpfCliente, celularCliente, senhaCliente)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
    except Exception as erro:
        print(erro)


def inserirFunc(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc):
    try:
        sql = "insert into funcionario(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) values('','{}','{}','{}','{}','{}')".format(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, " Funcionário Inserido! ")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionarCliente():
    try:
        sql = "select * from cliente"
        con.execute(sql)

        for (codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente) in con:
            print(codigoCliente, nomeCliente, cpfCliente, celularCliente, senhaCliente)
        print('\n')
    except Exception as erro:
        print(erro)

def selecionarFunc():
    try:
        sql = "select * from funcionario"
        con.execute(sql)

        for (codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) in con:
            print(codigoFunc, nomeFunc, cpfFunc, celularFunc,salarioFunc, senhaFunc)
        print('\n')
    except Exception as erro:
        print(erro)
