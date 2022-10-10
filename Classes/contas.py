from abc import ABC ,abstractmethod

class Conta(ABC):
    def __init__(self,agencia ,conta ,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor


    def extrato(self):
        print(f'Agência: {self.agencia} \n'
              f'Conta : {self.conta}\n'
              f'Saldo : {self.saldo}')

    @abstractmethod
    def sacar(self,valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print('Saldo Insuficiente . ')
            return
        self.saldo -= valor
        self.extrato()


class ContaCorrente(Conta):
    def __init__(self,agencia ,conta ,saldo,limite = 500):
        super().__init__(agencia,conta,saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite)  < valor:
            print('Saldo Insuficiente . ')
            return

        self.saldo -= valor
        self.extrato()

