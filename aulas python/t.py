import copy 
produtos = [
    {'nome': 'Produto 5', 'Preco': 10.00},
    {'nome': 'Produto 1', 'Preco': 22.32},
    {'nome': 'Produto 3', 'Preco': 10.11},
    {'nome': 'Produto 2', 'Preco': 105.87},
    {'nome': 'Produto 4', 'Preco': 69.90},
]
novo_produtos = [
    {**produto, 'Preco': round((produto['Preco']* 1.1),2)} for produto in copy.deepcopy(produtos)
]

def ordem_preco(produtos):
    ordem_preco = sorted(produtos, key=lambda x: x['Preco'])
    return ordem_preco

def ordem_nome(produtos):
    ordem_nome = sorted(produtos, key=lambda x: x['nome'])
    return ordem_nome

# Exemplo de uso
print("\nProdutos ordenados por nome:")
for produto in ordem_nome(produtos):
    print(produto)
print()
print("Produtos ordenados por preço:")
for produto in ordem_preco(produtos):
    print(produto)


    


