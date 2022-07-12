import this
import hamburgao
import login
import pizza
import bauru
this.opcao = 0

def Menu ():
    print('Escolha uma das opções abaixo:\n'+
          '\n1. Hamburgão '+
          '\n2. Pizza '+
          '\n3. Bauru '+
          '\n4. Voltar '+
          '\n5. Fechar Programa')
    this.opcao = int(input())

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 4:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para 1.
            hamburgao.operacao()
        elif this.opcao == 2:
            #operacao para 2.
            pizza.operacao()
        elif this.opcao == 3:
            # operacao para 3.
            bauru.operacao()
        elif this.opcao == 4:
            login.escolhas()
        elif this.opcao == 5:
            exit()
        else:
            print('Opção escolhida inválida! Tente novamente com as opções fornecidas.')