print("Exemplo de captura de execções")
try:
    numero = int(input("Digite um noumero"))
    resultado  = 10 / numero
    print(f"resultado{resultado}")
except ValueError as e:
    print(f"Erro value error: {e}")
    raise ValueError("Tipo de variavel imcopativel")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"resultado. {resultado}")
finally:
    print("Operação finalizada")
