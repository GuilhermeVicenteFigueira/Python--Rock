print("Exeplo de importação de um modulo padrão")
import math
from math import sqrt

raizQuadrada = math(25)
print(f"Raiz quadrada de 25 é {raizQuadrada}")

print("\n Exemplo de ciração de utilização de modulo personalizadao")
import meumodulo 

mensagem = meumodulo.saudacao("Guilherme")
resultadoDobro = meumodulo.dobro(5)
print(mensagem)
print(f"O numero de 5 é {resultadoDobro}")


print("\n Exemplo 2 de ciração de utilização de modulo personalizadao")
from meumodulo import saudacao, dobro

mensagem = saudacao("Guilherme")
resultadoDobro = dobro(5)
print(mensagem)
print(f"O numero de 5 é {resultadoDobro}")