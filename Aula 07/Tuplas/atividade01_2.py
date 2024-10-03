import os
os.system ("cls")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

tupla_numeros = (n1, n2, n3, n4, n5)
# print (tupla_numeros)

maior = max(tupla_numeros)
# print (f"O maior número é {maior}")

menor = min(tupla_numeros)
# print (f"O menor número é {menor}")

total = sum(tupla_numeros)
# print (f"A soma dos número é {total}")

ordenada = sorted(tupla_numeros)
# print (f"Essa é a tupla ordenada {ordenada}")

print (f"\n ################ \nO maior número é {maior}.\nO menor é o {menor}.\nA soma dos número é {total:.2f}.\nEssa é a tupla ordenada : {ordenada}")