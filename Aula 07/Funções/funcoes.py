def decoracao ():
    print ()
    print (30* "=")
    print()

def saudacao (txt):
    print (f"Olá {txt}")


def somar_valores (a,b):
    total = a + b
    med = (a+b) /2
    # print (f"Total é: {total}")
    return total, med


# decoracao()
# print ("Iniciando o programa")
# print ("Nome: ")
# print ("Idade: ")
# print ("Cidade: ")

# decoracao()
# print("Dados Pessoais")
# print("CPF")
# print("RG")

# decoracao()
# print("Rede Social")
# print("GitHub")
# print("Linkedin")
    
# print ("Iniciando o programa")
# nome = input("Informe o seu nome: ")
# cpf = input("Informe o seu CPF: ")

# decoracao()
# saudacao(nome)
# saudacao(cpf)
    
n1 = float (input("Número: "))
n2 = float (input("Número: "))

valor, media = somar_valores (n1,n2)

print(valor, media)