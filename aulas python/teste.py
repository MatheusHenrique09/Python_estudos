"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try :
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
except:
    print("Não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = int(input("Digite o horário: "))
    if horario < 12:
        print("Bom dia")
    elif horario < 17:
        print("Boa tarde")
    elif horario < 24:
        print("Boa noite")
    else:
        print("hora inválidada")
except:
    print("informe um número inteiro:")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite o seu nome:")
num_nome = len(nome)
if num_nome <= 4:
    print("Seu nome é curto")
elif num_nome < 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
