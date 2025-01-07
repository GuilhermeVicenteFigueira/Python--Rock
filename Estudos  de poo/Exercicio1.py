"""Crie uma classe Conta, está classe deve ter os atributos:
a) Banco
b) Agência
c) Número da conta
d) Saldo
Sua classe deve ter um construtor que inicializa todos os atributos. Crie os
métodos get e set para cada atributo. Só é possível iniciar uma conta com um
valor positivo ou zero, caso negativo deve ser colocado como zero. Deve
implementar a função deposito(), que recebe um valor por parâmetro e caso o
valor seja mais que zero, será feito um depósito no saldo da conta e retornar
true, caso não seja, deve retornar false e não alterar o saldo. Deve-se
implementar a função saque(), que também recebe um valor por parâmetro que
será sacado da conta, o saque só é efetivado se o valor a ser sacado for positivo
e não superior ao saldo da conta, se o saque for efetivo deve-se retornar o valor
do saque, caso contrário, retorna false, lembre-se de subtrair o valor sacado do
saldo da conta. Para testar, crie pelo menos duas instâncias e faça os prints
necessários para demonstrar o funcionamento."""



class Conta:
    def __init__(self, banco, agencia, numeroConta, saldo):
        self.__banco = banco
        self.__agencia = agencia
        self.__numeroConta = numeroConta
        self.__saldo = saldo

    def getBanco(self):
        return self.__banco
    
    def setBanco(self,)
    
    def getAgencia(self):
        return self.__agencia
    
    def getNumeroConta(self):
        return self.__numeroConta
    
    def getSaldo(self):
        return self.__saldo
    

