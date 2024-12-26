def decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper  

@decorador
def funcao():
    print("Minha função foi chamada")

funcao()

class MeuDecoradorClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")

@MeuDecoradorClasse
def segundaFuncao():
    print("Segunda função foi chamada")

segundaFuncao()
