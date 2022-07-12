import this
import menuCliente
import conexao
this.opcao = 0
this.quant = 0

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


##############################################
            #Iniciando código
##############################################
def PrecoLanche():
    sql = "select * from lanche where nomeLanche = 'Hamburgão'"
    con.execute(sql)

    for (codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
        return valorLanche


def Preco ():
    valor = float(PrecoLanche())
    print('O preço do Hamburgão é: R$ {}'.format(valor))


def QuantidadeLanche():
    sql = "select * from lanche where nomeLanche = 'Hamburgão'"
    con.execute(sql)

    for (codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
        return quantidadeLanche


def Quantidade():
    quantidade = float(QuantidadeLanche())
    print('A quantidade disponível desse lanche é: {}'.format(quantidade))

def Selecao ():
    print('Digite a quantidade que deseja comprar: ')
    this.quant = int(input())
    while (this.quant < 0) or (this.quant > QuantidadeLanche()):
        if (this.quant < 0) or (this.quant > QuantidadeLanche()):
            print('Informe uma quantidade acessível disponível, por favor!')
            this.quant = int(input())

def CalculoQuant():
    resto = int(QuantidadeLanche()) - int(this.quant)
    sql = "update lanche set quantidadeLanche = '{}' where nomeLanche = 'Hamburgão'".format(resto)
    con.execute(sql)
    db_connection.commit()


def Calculo():
    CalculoQuant()
    return this.quant * PrecoLanche()

def Compra():
    Preco()
    Quantidade()
    Selecao()
    print('---------------- O valor total da compra é: '+ str(Calculo()) +' ----------------\n')

def Menu():
    print('Deseja:'
          '\n1. Realizar Compra' +
          '\n2. Cancelar Compra')
    this.opcao = int(input())

def operacao():
        # Mostrar o menu em tela
        while this.opcao != 2:
            Menu()
            #realizar operações
            if this.opcao == 1:
                #operacao para 1.
                Compra()
                print('O código do PIX é 12345678912, acesse https://www.picpay.com/site para efetuar pagamento.')
            elif this.opcao == 2:
                #opereção para 2.
                menuCliente.operacao()
            else:
                print('Opção escolhida inválida! Tente novamente com as opções fornecidas.')