# a funcao MAP tem como objetuvo aplicar uma funcao ou acao
# em todos os elementos de uma estrutura de dados retornando 
# um nova sequencia ou resultado 

import math


lista = [1,5,3,15,78]

def soma(x):
    return x+2

print(list(map(soma,lista)))


print(list(map(math.sqrt,lista)))
