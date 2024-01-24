#funcao filter filtra elementos de uma estrutura de dados 
#e filtra o valor q queremos encontrar 

listamista = [1,"joao","pedro",53]

def busca (x):
    return x == "joao"

# nao otimizada
print(list(filter(busca,listamista)))

#Otimizada
print(list(filter(lambda x: x == "pedro",listamista)))