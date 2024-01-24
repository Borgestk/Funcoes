# retorna indice de uma colecao de dados 

animais=["cachorro","gato","elefante","papagaio"]

print(list(enumerate(animais)))

## iterar uma lista com enumerate

for i,valor in enumerate(animais):
    print(i,valor)

## iterador com condicionais
    
for i,valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)