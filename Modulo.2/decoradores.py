def decorador (func):
    def wrapper():
        print("antes da função chamda")
        func()
        print("Depois da funçõa ser chamada")
        return wrapper
    
@decorador
def funcao():
    print("Minha funcção foi chamada")

class meuDecoradorClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamda (decorador de clase)")
        self.func()
        print("Deopis da funçãp ser chamada (decorador de classe)")

@meuDecoradorClasse
def segundaFuncao():
    print("Segunda funcao foi add")