"""# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10

    def __init__(self, nome) -> None:
        self.nome =  nome

    def metodoInstancia(self):
        return f"Metodo de isntancia chamado {self.nome}"
    
    @classmethod
    def metodoClasse(cls):
        return f"Metodo de classe chamado para valor= {cls.valor}"
    @staticmethod
    def motodoEstatico():
        return "Metodo estatico chamadop"

obj = MinhaClasse(nome = "Exemplo")
print(obj.metodoInstancia())
print(MinhaClasse.valor())
print(MinhaClasse.metodoClasse())
print(MinhaClasse.motodoEstatico())
"""

print("\nExemplos")


class Carro:
    def __init__(self, marca , modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criarCarro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
    
config1 = "Toyota,Corola,2022"
carro1 = Carro.criarCarro(config1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


print("\nExemplo 2")


class Matematica:

    @staticmethod
    def soma (a,b):
        return a + b
    
print(Matematica.soma(a= 10, b= 15))