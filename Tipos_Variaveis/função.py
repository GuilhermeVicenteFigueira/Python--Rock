def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Manu")

# funcao com retorno

def quadrado(numero):
    resultado = numero **2
    return resultado

print("\n Chamando função quadrado")
resultadoQuadrado = quadrado(5)
print("Resultado da função quadrado:", resultadoQuadrado)

#chamando um função com multiplos parametros

def soma(numero1, numero2):
    resultado = (numero1 + numero2) / 10
    return resultado
print ("\nChamando a funcaçao soma:")
numero1 = 620
numero2 = 700
resultadoSoma = soma (numero1 , numero2)
print (f" A soma do numero %s e o numero %s é %s" % (numero1, numero2 , resultadoSoma))
