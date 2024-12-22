# POO


# Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade)-> None :
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá meu nome é {self.nome} eu detenho {self.idade} anos."

# Objetos

pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rogerio", idade = 40)
mensagem = pessoa2.saudacao()
print(mensagem)

