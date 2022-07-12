import operacoesLogin
import this
import conexao
this.opcao = -1

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
            '1. Cadastrar Cliente\n' +
            '2. Login Cliente\n' +
            '3. Login Adiministrador\n' +
            '0. Sair')
    this.opcao = int(input())

def escolhas():
    while(this.opcao !=0 ):
        menu()
        if this.opcao == 1:
                # Coletando a digitação do usuário
                print('Digite seu nome e sobrenome: ')
                nomeCliente = input()
                print('Digite seu cpf: ')
                cpfCliente = input()
                if operacoesLogin.cpf_validate(cpfCliente):
                    print('CPF válido.')
                else:
                    print('CPF Inválido.')
                    escolhas()
                print('Digite seu celular: ')
                celularCliente = input()
                print('Digite sua senha: ')
                senhaCliente = input()
                if nomeCliente + cpfCliente + celularCliente + senhaCliente == "":#validar para não permitir dados em branco
                    print("Favor não deixe nenhum espaço em branco, Tente novamente!")
                else:operacoesLogin.inserirCliente(nomeCliente, cpfCliente, celularCliente, senhaCliente)
                # utilizar o método cadastrar
        elif this.opcao == 2:
            print("Digite seu CPF: ")
            cpfCliente= input()
            if operacoesLogin.cpf_validate(cpfCliente):
                print('CPF válido.')
            else:
                print('CPF Inválido.')
                escolhas()
            print("Digite sua senha: ")
            senhaCliente = input()
            if cpfCliente + senhaCliente == "":#validar para não permitir dados em branco
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoesLogin.loginCliente(cpfCliente, senhaCliente)
        elif this.opcao == 3:
            print("Digite seu CPF: ")
            cpfFunc = input()
            if operacoesLogin.cpf_validate(cpfFunc):
                print('CPF válido.')
            else:
                print('CPF Inválido.')
                escolhas()
            print("Digite sua senha: ")
            senhaFunc = input()
            if cpfFunc + senhaFunc == "":#validar para não permitir dados em branco
                print("Favor não deixe nenhum espaço em branco, Tente novamente!")
            else:operacoesLogin.loginFunc(cpfFunc, senhaFunc)
        else:
             print("Obrigado e até a proxima!")