import menuADM
import operacoesFunc
import this
this.opcao = -1

def menu():
    print('\n\nAdm Funcionários: Escolha uma das opções abaixo: \n\n' +
            '1. Cadastrar Funcionário\n'                        +
            '2. Consultar Funcionário\n'                        +
            '3. Atualizar Nome do Funcionário\n'                   +
            '4. Atualizar Celular do Funcionário\n'               +
            '5. Atualizar Salário do Funcionário\n'               +
            '6. Atualizar Senha do Funcionário\n'               +
            '7. Excluir Funcionário\n'               +
            '8. Voltar\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            print('Digite o Nome: ')
            nomeFunc = input()
            while not nomeFunc:
                if not nomeFunc:
                    print("Favor não deixar espaço em branco!")
                    nomeFunc = input()
            print('Digite o CPF: ')
            cpfFunc = input()
            while not cpfFunc:
                if not cpfFunc:
                    print("Favor não deixar espaço em branco!")
                    cpfFunc = input()
            print('Digite o Celular: ')
            celularFunc = input()
            while not celularFunc:
                if not celularFunc:
                    print("Favor não deixar espaço em branco!")
                    celularFunc = input()
            print('Digite a data Salário: ')
            salarioFunc = input()
            while not salarioFunc:
                if not salarioFunc:
                    print("Favor não deixar espaço em branco!")
                    salarioFunc = input()
            print('Digite a data Senha: ')
            senhaFunc = input()
            while not senhaFunc:
                if not senhaFunc:
                    print("Favor não deixar espaço em branco!")
                    senhaFunc = input()
            # utilizar o método cadastrar
            operacoesFunc.inserir(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        elif this.opcao == 2:
            operacoesFunc.selecionar()
        elif this.opcao == 3:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            while not codigo:
                if not codigo:
                    print("Favor não deixar espaço em branco!")
                    codigo = input()
            print('Informe o novo Nome: ')
            nomeFunc = input()
            while not nomeFunc:
                if not nomeFunc:
                    print("Favor não deixar espaço em branco!")
                    nomeFunc = input()
            # Uso do método
            operacoesFunc.atualizarNome(codigo, nomeFunc)
        elif this.opcao == 4:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            while not codigoFunc:
                if not codigoFunc:
                    print("Favor não deixar espaço em branco!")
                    codigoFunc = input()
            print('Informe o novo Celular: ')
            celularFunc = input()
            while not celularFunc:
                if not celularFunc:
                    print("Favor não deixar espaço em branco!")
                    celularFunc = input()
            # Uso do método
            operacoesFunc.atualizarCelular(codigoFunc, celularFunc)
        elif this.opcao == 5:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            while not codigoFunc:
                if not codigoFunc:
                    print("Favor não deixar espaço em branco!")
                    codigoFunc = input()
            print('Informe o novo Salário: ')
            salarioFunc = input()
            while not salarioFunc:
                if not salarioFunc:
                    print("Favor não deixar espaço em branco!")
                    salarioFunc = input()
            # Uso do método
            operacoesFunc.atualizarCelular(codigoFunc, salarioFunc)
        elif this.opcao == 6:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigoFunc = input()
            while not codigoFunc:
                if not codigoFunc:
                    print("Favor não deixar espaço em branco!")
                    codigoFunc = input()
            print('Informe o novo Senha: ')
            senhaFunc = input()
            while not senhaFunc:
                if not senhaFunc:
                    print("Favor não deixar espaço em branco!")
                    senhaFunc = input()
            # Uso do método
            operacoesFunc.atualizarSenha(codigoFunc, senhaFunc)
        elif this.opcao == 7:
            print('Informe o código: ')
            codigoFunc = input()
            while not codigoFunc:
                if not codigoFunc:
                    print("Favor não deixar espaço em branco!")
                    codigoFunc = input()
            operacoesFunc.excluir(codigoFunc)
        elif this.opcao == 8:
            menuADM.operacao()
        elif this.opcao == 0:
            print('Obrigado!')