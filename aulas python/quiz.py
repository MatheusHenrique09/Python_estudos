import os  # Importa o módulo os para manipulação do sistema operacional
from time import sleep

# Lista de perguntas, cada uma com suas opções e resposta correta
perguntas = [
    {
        "Pergunta": "Qual é o maior animal marinho?",
        "Opções": ["Tubarão-branco", "Baleia-azul", "Orca", "Baleia-jubarte", "Golfinho"],
        "Resposta": "Baleia-azul"
    },
    {
        "Pergunta": "Qual é a capital da Alemanha?",
        "Opções": ["Berlim", "Munique", "Frankfurt", "Hamburgo", "Colônia"],
        "Resposta": "Berlim"
    },
    {
        "Pergunta": "Quem pintou 'A Última Ceia'?",
        "Opções": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Michelangelo"],
        "Resposta": "Leonardo da Vinci"
    },
    {
        "Pergunta": "Qual é o maior continente do mundo?",
        "Opções": ["África", "América do Norte", "Ásia", "Europa", "Oceania"],
        "Resposta": "Ásia"
    },
    {
        "Pergunta": "Em que país se encontra a Grande Muralha?",
        "Opções": ["Japão", "China", "Coreia do Sul", "Índia", "Mongólia"],
        "Resposta": "China"
    },
    {
        "Pergunta": "Qual é o elemento químico com o símbolo 'Na'?",
        "Opções": ["Sódio", "Nitrogênio", "Neônio", "Nióbio", "Nitrato"],
        "Resposta": "Sódio"
    },
    {
        "Pergunta": "Qual é o rio mais longo do mundo?",
        "Opções": ["Amazonas", "Nilo", "Yangtze", "Mississippi", "Ganges"],
        "Resposta": "Nilo"
    },
    {
        "Pergunta": "Qual é o país conhecido como a Terra do Sol Nascente?",
        "Opções": ["China", "Japão", "Tailândia", "Coreia do Sul", "Filipinas"],
        "Resposta": "Japão"
    },
    {
        "Pergunta": "Qual é a capital do Brasil?",
        "Opções": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador", "Belo Horizonte"],
        "Resposta": "Brasília"
    },
    {
        "Pergunta": "Qual é a fórmula química do gás carbônico?",
        "Opções": ["CO2", "H2O", "O2", "CH4", "NH3"],
        "Resposta": "CO2"
    },
    {
        "Pergunta": "Quem foi o autor de 'A Divina Comédia'?",
        "Opções": ["Homero", "Dante Alighieri", "Virgílio", "Cervantes", "Shakespeare"],
        "Resposta": "Dante Alighieri"
    },
    {
        "Pergunta": "Qual é o maior órgão interno do corpo humano?",
        "Opções": ["Coração", "Fígado", "Pulmões", "Rins", "Estômago"],
        "Resposta": "Fígado"
    },
    {
        "Pergunta": "Qual é a principal religião da Índia?",
        "Opções": ["Cristianismo", "Hinduísmo", "Islamismo", "Budismo", "Jainismo"],
        "Resposta": "Hinduísmo"
    },
    {
        "Pergunta": "Qual é o planeta vermelho?",
        "Opções": ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter"],
        "Resposta": "Marte"
    },
    {
        "Pergunta": "Quem foi o primeiro presidente do Brasil?",
        "Opções": ["Getúlio Vargas", "Deodoro da Fonseca", "Juscelino Kubitschek", "Fernando Henrique Cardoso", "Lula"],
        "Resposta": "Deodoro da Fonseca"
    }
]

qtd_acertos = 0  # Inicializa o contador de acertos

# Loop para percorrer cada pergunta na lista
for i, pergunta in enumerate(perguntas):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela, dependendo do sistema operacional
    print(f'{i+1}) {pergunta['Pergunta']}')  # Exibe a pergunta
    print()

    opcoes = pergunta['Opções']  # Obtém as opções da pergunta
    # Exibe as opções numeradas
    for i, opcao in enumerate(opcoes):
        print(f'{i+1}) {opcao}')

    print()

    escolha = input('Escolha uma opção: ')  # Solicita ao usuário que escolha uma opção

    acertou = False  # Inicializa a variável que indica se o usuário acertou
    escolha_int = None  # Inicializa a variável para armazenar a escolha convertida em inteiro
    qtd_opcoes = len(opcoes)  # Obtém a quantidade de opções

    # Verifica se a escolha é um número
    if escolha.isdigit():
        escolha_int = int(escolha)  # Converte a escolha para inteiro

    # Verifica se a escolha é válida
    if escolha_int is not None:
        if 0 <= escolha_int < qtd_opcoes:  # Verifica se a escolha está dentro do intervalo válido
            escolha_fomatada = escolha_int - 1
            if opcoes[escolha_fomatada] == pergunta['Resposta']:  # Verifica se a opção escolhida é a resposta correta
                acertou = True  # Atualiza a variável para indicar que o usuário acertou

    # Exibe o resultado da escolha
    if acertou:
        qtd_acertos += 1  # Incrementa o contador de acertos
        print('Acertou 👍')  # Mensagem de acerto
    else:
        print('Errou ❌')  # Mensagem de erro
        print('Resposta certa:',pergunta['Resposta'])
    print()
    
    sleep(2)
    
os.system('cls' if os.name == 'nt' else 'clear')

# Exibe o total de acertos e o número total de perguntas
print('Você acertou:', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

if qtd_acertos <= 5:
    print('Precisa melhora, quase um idiota! 🙀')
elif qtd_acertos < 10:
    print('Só isso!! kkkk😝')
elif qtd_acertos <=14:
    print('Muito bom! 🤓')
else:
    print('Ah papai, o muleke é brabo! 🏅')


        
    
    
         