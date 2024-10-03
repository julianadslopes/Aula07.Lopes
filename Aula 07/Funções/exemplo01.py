import os
os.system("cls")

def par_impar(n):
    resultado = n % 2
    resposta = ""
    if resultado == 0:
        resposta = "Par"
    else:
        resposta = "Ímpar"
    return resposta    

n = float(input("Digite um número: "))
resp = par_impar(n)

print (f"{n} é {resp}")



# num = int(input('Informe um numero: '))
# n2 = num % 2

# if n2 != 0:
#     print('Numero impar')
# else:
#     print('Numero par')