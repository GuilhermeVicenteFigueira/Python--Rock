import random

class Personagem:
    def __init__(self, nome, vida ,nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def getNome(self):
        return self.__nome
    
    def getVida(self):
        return self.__vida
    
    def getNivel(self):
        return self.__nivel
    
    def exibirDetalhes(self):
        return f"Nome: {self.getNome()}\nVida: {self.getVida()}\nNivel: {self.getNivel()}"
    
    def receberDano(self,dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self._vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.getNivel() * 2, self.getNivel() * 4)
        alvo.receberDano(dano)
        print(f"{self.getNome()} atacou {alvo.getNome()} e causou {dano} de dano")
        







  
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def getHabilidade(self):
        return self.__habilidade
    
    def exibirDetalhes(self):
        return f"\n {super().exibirDetalhes()} Habilidade: {self.getHabilidade()}"
    
    def habilidadeEspecial(self, alvo):
        dano = dano = random.randint(self.getNivel() * 5, self.getNivel() * 8)
        alvo.receberDano(dano)
        print(f"{self.getNome()} Uso a habilidade especial {self.getHabilidade()} em {alvo.getNome()} e causou {dano} de dano!")
    








class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel,tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo 

    def getTipo(self):
        return self.__tipo
    
    def exibirDetalhes(self):
        return f"\n {super().exibirDetalhes()} Tipo: {self.getTipo()}"
    






class Orquestrador:

    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome ="pythonLovers", vida = 1000000000, nivel = 1000000 ,habilidade = "FDS O POO EU SOU MACACO")
        self.inimigo = Inimigo(nome = "phpNoggers", vida = 1, nivel = 1, tipo = "PATO")



    def inicioBatalha(self):

        """Fazer a gestao do combate """

        print(" Iniciando o Combate !")
        while self.heroi.getVida() > 0 and self.inimigo.getVida() > 0:
            print ("\n Detalhes dos Personagens: ")
            print(self.heroi.exibirDetalhes())
            print(self.inimigo.exibirDetalhes())

            input("\n Precione Enter para atacar...")
            escolha = input("\n Escolha: (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.habilidadeEspecial(self.inimigo)
            else:
                print("Escolha invalida")


            if self.inimigo.getVida() > 0:
                #Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)


        if self.heroi.getVida() > 0:
            print (f"Parabens você venceu o {self.inimigo.getNome()}")
        else:
            print("Você foi derotado!")








jogatina = Orquestrador()
jogatina.inicioBatalha()
