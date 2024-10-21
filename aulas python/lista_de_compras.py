from time import sleep
import os

# Inicializa uma lista vazia para armazenar os itens da lista de compras.
lista_compras = list()

# Loop principal do programa. Ele vai rodar indefinidamente até o usuário optar por sair.
while True:
    # Solicita ao usuário pressionar "Enter" para continuar e iniciar o ciclo de opções.
    input("\nPressione Enter para continuar...")
    
    try:
        # Limpa a tela do terminal (Windows).
        os.system('cls')
        # Exibe as opções ao usuário e captura a entrada, convertendo para minúsculas e removendo espaços extras.
        print('Selecione uma opção:')
        entrada = input('[i]nserir [a]apagar [l]istar [s]air: ').lower().strip()
    except:
        # Se ocorrer algum erro na entrada do usuário, o loop simplesmente continua.
        continue

    # Se a entrada for 's', o programa exibe uma mensagem e encerra o loop, terminando a execução.
    if entrada == 's':
        print("Saindo do programa...")
        break

    # Se a entrada for 'l', o programa verifica se a lista contém itens.
    if entrada == 'l':
        if lista_compras:
            # Se a lista não estiver vazia, exibe os itens com seus respectivos índices.
            print('LISTA: ')
            for indice, produto in enumerate(lista_compras):
                print(f'{indice} - {produto}')
        else:
            # Se a lista estiver vazia, exibe uma mensagem informando que não há itens.
            print('Nada para listar')
        sleep(1)

    # Se a entrada for 'i', o programa solicita ao usuário inserir um novo item na lista.
    elif entrada == 'i':
        # Limpa a tela antes de inserir um novo item.
        os.system('cls')
        # Recebe o novo item do usuário.
        novo_produto = input('Valor: ')
        if novo_produto:
            # Se o item inserido não for vazio, ele é adicionado à lista.
            lista_compras.append(novo_produto)
        else:
            # Caso o usuário não insira um valor válido, exibe uma mensagem de erro.
            print('Valor inválido!')
        sleep(1)

    # Se a entrada for 'a', o programa inicia o processo de apagar um item da lista.
    elif entrada == 'a':
        # Verifica se a lista contém itens antes de permitir a exclusão.
        if lista_compras:
            print('LISTA: ')
            for indice, produto in enumerate(lista_compras):
                print(f'{indice} - {produto}')
            
            try:
                # Solicita ao usuário escolher o índice do item a ser apagado.
                numero_indice = int(input("Escolha o índice para apagar: "))
                # Verifica se o índice inserido é válido.
                if 0 <= numero_indice < len(lista_compras):
                    del lista_compras[numero_indice]
                    print("Item apagado com sucesso!")
                else:
                    # Se o índice for inválido, exibe uma mensagem de erro.
                    print('Índice inválido!')
            except:
                # Caso ocorra um erro, como inserir algo que não seja um número, exibe uma mensagem de erro.
                print('Por favor, insira um número válido.')
        else:
            # Se a lista estiver vazia, exibe uma mensagem informando que não há nada para apagar.
            print('Nada para apagar')
        sleep(1)

# Quando o programa termina, ele imprime a lista final de itens restantes.
print('LISTA FINAL: ')
for indice, produto in enumerate(lista_compras):
    print(f'{indice} - {produto}')
