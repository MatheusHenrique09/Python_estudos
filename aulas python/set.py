# Lista de listas de números
lista_num = [
    [91, 3, 2, 5, 4, 6, 6],
    [5, 44, 4, 5, 7, 5, 4, 5],
    [3, 6, 6, 5, 7, 9, 5, 1, 1],
    [9, 6, 5, 5, 2, 1, 4, 7, 8, 5]
]

def identificador_repetidos(lista):
    numeros_vistos = set()  # Usar um conjunto para armazenar números já vistos
    primeiro_duplicado = -1  # Inicializa como -1 (sem duplicado)

    # Percorre cada número na lista
    for num in lista:
        # Se o número já foi visto, é um duplicado
        if num in numeros_vistos:
            primeiro_duplicado = num  # Armazena o primeiro duplicado encontrado
            break  # Sai do loop assim que encontrar o primeiro duplicado
        
        numeros_vistos.add(num)  # Adiciona o número ao conjunto de vistos
    
    return primeiro_duplicado  # Retorna o primeiro duplicado ou -1 se não houver

# Loop para verificar cada sublista em lista_num
for sublista in lista_num:        
    resultado = identificador_repetidos(sublista)  # Chama a função para cada sublista
    print(f'Primeiro duplicado na lista {sublista}: {resultado}')  # Exibe o resultado

 
 
 