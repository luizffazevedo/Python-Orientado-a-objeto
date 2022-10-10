from Classes.banco import Banco
from Classes.cliente import Cliente
from Classes.contas import ContaCorrente,ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz',27)
cliente2 =Cliente('Paula',23)
cliente3 = Cliente('João',28)

conta1 = ContaCorrente(1111,876352,0)
conta2 = ContaPoupanca(2222,876351,0)
conta3 = ContaPoupanca(3333,875435,0)


cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_conta(conta1)
banco.inserir_cliente(cliente1)

if banco.autenticar(cliente1):
    cliente1.conta.sacar(40)
    cliente1.conta.depositar(50)

else:
    print('Cliente não autenticado .')