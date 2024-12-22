# Declaração

nomeCompleto = "Guilherme Vicente"

nomeCompletoAspas = """"Guilherme 
Vicente"""

nomeCompletoQuebra = "Guilherme \  Vicente"

nome = "Guilherme "
sobrenome = "Vicente"


print("Nome completo (1-forma): ", nomeCompleto)
print("Nome completo (2-forma): " + nomeCompleto)
print("Nome completo (3-forma):" + "Guilherme " + "Vicente")
print("Nome completo (4-forma):" + "Guilherme " , "Vicente")
print("Nome completo (5-forma):", nomeCompletoAspas)
print("Nome completo (6-forma):",  nomeCompletoQuebra)
print("Nome completo (7-forma): %s" % nomeCompleto)
print("Nome completo (8-forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9-forma): {nome} {sobrenome}")
print("Nome completo (10-forma):{} {}". format(nome,sobrenome))


