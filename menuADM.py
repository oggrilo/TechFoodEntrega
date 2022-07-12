import login
import operacoesLanche
import this
import crudFuncionario
import conexao
db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.opcao = -1

def QuantidadeLanche():
    sql = "select * from lanche where nomeLanche = 'Hamburgão'"
    con.execute(sql)

    for (codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
        return codigoLanche





def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Administrar Funcionário\n'                        +
            '2. Cadastrar Lanche\n'                   +
            '3. Consultar Lanche\n'                        +
            '4. Atualizar Nome do Lanche\n'                   +
            '5. Atualizar Descrição do Lanche\n'               +
            '6. Atualizar Valor do Lanche\n'               +
            '7. Atualizar Quantidade do Lanche\n'               +
            '8. Exlcuir Lanche\n'               +
            '9. Voltar\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            crudFuncionario.operacao()
        elif this.opcao == 2:
            # Coletando a digitação do usuário
            print('Digite o Nome: ')
            nomeLanche = input()
            while not nomeLanche:
                if not nomeLanche:
                    print("Favor não deixar espaço em branco!")
                    nomeLanche = input()
            print('Digite a Descrição: ')
            descricaoLanche = input()
            while not descricaoLanche:
                if not descricaoLanche:
                    print("Favor não deixar espaço em branco!")
                    descricaoLanche = input()
            print('Digite o Valor: ')
            valorLanche = float()
            while not valorLanche:
                if not valorLanche:
                    print("Favor não deixar espaço em branco!")
                    valorLanche = input()
            print('Digite a Quantidade: ')
            quantidadeLanche = float()
            while not quantidadeLanche:
                if not quantidadeLanche:
                    print("Favor não deixar espaço em branco!")
                    quantidadeLanche = input()
            # utilizar o método cadastrar
            operacoesLanche.inserir(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche)
        elif this.opcao == 3:
            operacoesLanche.selecionar()
        elif this.opcao == 4:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            while not codigo:
                if not codigo:
                    print("Favor não deixar espaço em branco!")
                    codigo = input()
            print('Informe o novo nome: ')
            nomeLanche = input()
            while not nomeLanche:
                if not nomeLanche:
                    print("Favor não deixar espaço em branco!")
                    nomeLanche = input()
            # Uso do método
            operacoesLanche.atualizarNome(codigo, nomeLanche)
        elif this.opcao == 5:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            while not codigo:
                if not codigo:
                    print("Favor não deixar espaço em branco!")
                    codigo = input()
            print('Informe a nova descrição: ')
            descricaoLanche = input()
            while not descricaoLanche:
                if not descricaoLanche:
                    print("Favor não deixar espaço em branco!")
                    descricaoLanche = input()
            # Uso do método
            operacoesLanche.atualizarDescricao(codigo, descricaoLanche)
        elif this.opcao == 6:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            while not codigo:
                if not codigo:
                    print("Favor não deixar espaço em branco!")
                    codigo = input()
            print('Informe o novo valor: ')
            valorLanche = float()
            while not valorLanche:
                if not valorLanche:
                    print("Favor não deixar espaço em branco!")
                    valorLanche = input()
            # Uso do método
            operacoesLanche.atualizarValor(codigo, valorLanche)
        elif this.opcao == 7:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            while not codigo:
                if not codigo:
                    print("Favor não deixar espaço em branco!")
                    codigo = input()
            print('Informe a nova quantidade: ')
            quantidadeLanche = float()
            while not quantidadeLanche:
                if not quantidadeLanche:
                    print("Favor não deixar espaço em branco!")
                    quantidadeLanche = input()
            # Uso do método
            operacoesLanche.atualizarQauntidade(codigo, quantidadeLanche)
        elif this.opcao == 8:
            print('Informe o código: ')
            codigoLanche = input()
            while not codigoLanche:
                if not codigoLanche:
                    print("Favor não deixar espaço em branco!")
                    codigoLanche = input()
            operacoesLanche.excluir(codigoLanche)
        elif this.opcao == 9:
            login.escolhas()
        elif this.opcao == 0:
            print('Obrigado!')