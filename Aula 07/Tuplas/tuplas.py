import os
os.system ("cls")

# tuplas_vazias = ()

# tupla_um_elemento = (10,) # para ser considerado do tipo tupla de 1 elemento, precisa da vírgula. Caso contrário, classificará como inteiro
# # print (tupla_um_elemento)
# # print(type(tupla_um_elemento))

# tupla_varios_elementos = (5,4,10,15,12)
# # print (tupla_varios_elementos)
# # print (tupla_varios_elementos[0])

# tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos
# # print (tupla_um_elemento)
# # print (5 in tupla_um_elemento)
# print (sorted (tupla_varios_elementos))

######################################################

nome = input ("Informe o nome: ")
nota1 = int (input ("Informe a nota 1: "))
nota2 = int (input ("Informe a nota 2: "))

tupla_notas = (nome, nota1, nota2)

print(f"Dados do usuário: {tupla_notas}")