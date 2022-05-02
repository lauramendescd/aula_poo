from modelo.banco.banco import Banco
from modelo.conta.conta import Conta


class Criar_banco:
    if __name__ == '__main__':
        banco = Banco()
        conta1 = Conta("21.342-7")
        conta2 = Conta("21.349-7")

        banco.cadastrar(conta1)
        banco.cadastrar(conta2)

        banco.creditar(conta1.get_numero(), 200.50)
        banco.creditar(conta2.get_numero(), 50.50)

        banco.tranferir(conta1.get_numero, conta2.get_numero, 150)

        print(banco.saldo(conta1.get_numero()))
