#if elif e else


#  Exemplo de "if"

idade = int(input("Quantos  anos você tem?"))
print("Exeplo de comando if")
if idade >= 18:
    print("Você é maior de idade")
elif idade >=12:
    print("Você é um adolecente")
else :
    print("Você é menor de idade")


mensagem = "Pode tirar carteira de habilitação" if idade >= 18 else "Você não pode  tirar habilitação"
print(mensagem)