class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome

        def emitirSom(self):
            pass

class Mamifero(Animal):
    def amamenta(self):
        return f"{self.nome} está amamentando "
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
    
class Morcego(Mamifero, Ave):
    def emitirSom(self):
        return "Morcegos emitem sons ultrasonicos"
    
morcego = Morcego(nome= "Batman")

#acessamdp metodos da classe base Animal
print("Nome do Morcego", morcego.nome)
print("Som do Morcego", morcego.emitirSom())

# acessando metodos das classe "MAMIFERO" E " AVE"
print("Morcego amamentando:", morcego.amamenta())
print("Morcego voando:", morcego.voar())