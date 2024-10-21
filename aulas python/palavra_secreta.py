import os
import random
print("     ****    PALAVRA SECRETA     ****       ")

# Variáveis de controle
letras_acertadas = ""  
numero_tentativas = 0

# Loop do jogo
while True:
    if numero_tentativas == 0:
        # Lista de palavras
        palavras = ["Abacaxi", "Elefante", "Montanha", "Estrela", "amor", "Livro", "Oceano", "Sorriso", "felicidade", "Borboleta", "Perfume"]
        
        # Escolhe uma palavra aleatória e converte para minúsculas
        palavra_secreta = random.choice(palavras).lower()

    letra_digitada = input("Digite uma letra: ").lower()
    numero_tentativas += 1

    # Verifica se foi digitada mais de uma letra
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    # Verifica se a letra está na palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Forma a palavra com as letras acertadas
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print("Palavra formada: ", palavra_formada)

     # Verifica se a palavra foi completamente formada
    if palavra_formada == palavra_secreta:
        os.system('cls')  # Limpa a tela (no Windows)
        print("Você ganhou!! PARABÉNS!")
        print("A palavra era:", palavra_secreta)
        print("Tentativas: ", numero_tentativas)
        
        # Verifica se o jogador quer sair
        if input("Quer sair?[S]im:?").lower().strip().startswith("s"):
            break 

        os.system('cls')
        print("     ****    PALAVRA SECRETA     ****       ")
        letras_acertadas = ""  
        numero_tentativas = 0
        
