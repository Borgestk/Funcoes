##e uma funcao que retorna sequencia de elementos em formato de tuplas

dicverduras = {1:'cebola',2:"alface",4:"beterraba"}

dicfrutas = {1:"maca",2:"laranja",3:"pera"}

print(list(zip(dicverduras.items(),dicfrutas.items())))
