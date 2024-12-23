# Exemplo de herança

print("\n  Exemplo de herança:")
class Animal:
    def __init__ (self,nome) ->None:
        self.nome = nome


        def andar(self):
           print(f"O Animal {self.nome} está andando")
           return
        
        def emitirSom(self):
            pass

class Cachorro(Animal):
    def emitirSom(self):
        return "Au, au"
    
class Gato(Animal):
    def emitirSom(self):
        return "Miau!"
    
dog= Cachorro(nome = "K9")
cat= Gato(nome = "Felix")

print("\n Exemplo de polimorfismo")
animais = [dog, cat]

for Animal  in animais:
    print(f"{Animal.nome} faz: {Animal.emitirSom()}")

print("\nExemplo de encapsulamento:")
print("\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor para depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saque inválido. Verifique o valor solicitado e o saldo disponível.")

    def verSaldo(self):
        return self.__saldo

# Testando a classe
conta = ContaBancaria(saldo=1000)
print(f"Saldo conta bancária: {conta.verSaldo()}")

conta.depositar(valor=500)
print(f"Saldo conta bancária: {conta.verSaldo()}")

conta.depositar(valor=-500)  # Testando depósito inválido
print(f"Saldo conta bancária: {conta.verSaldo()}")

conta.sacar(valor=200)
print(f"Saldo conta bancária: {conta.verSaldo()}")

conta.sacar(valor=1500)  # Testando saque com saldo insuficiente

print("\n Exemplo de abstração")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
        # ligaçao do carro
    def ligar(self):
        return "carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado utilizando a chave"

carroAmarelo = Carro()
print(carroAmarelo.ligar())
print(carroAmarelo.desligar())
