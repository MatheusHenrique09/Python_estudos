from itertools import zip_longest,count
# filvalue
primeira_lista = ['Salvador','Ubatuba','Belo Horizonte']
segunda_lista = ['BA','SP','MG','RJ']
lista3 = ['Brasil', 'Brasil', 'Brasil']

lis = list(zip_longest(primeira_lista, segunda_lista,lista3,fillvalue='sem valor'))
print(lis)

def zipper(*args):
    terceira_lista = []
    min_len = min(len(lst) for lst in args)
    for i in range(min_len):
        terceira_lista.append(tuple(lst[i] for lst in args))
    return terceira_lista

print(zipper(primeira_lista,segunda_lista,lista3))


lista1 = list(zip(primeira_lista,segunda_lista,lista3))
print(lista1)

inteiro = [1,3,2,45,9,4]
real = [12.5,454.6,4.0,7.9,5.6]

def somaLista(x,y):
    soma = []
    menor = min(len(x),len(y))
    for i in range(menor):
        soma.append(x[i]+y[i])
    return soma

print(somaLista(inteiro,real))

lista_soma = [x + y for x, y in zip(inteiro,real)]
print(lista_soma)

c1 = count()
r1 = range(10)

for i in c1(r1):
    if i > 100:
        break
    print(i)
    
    