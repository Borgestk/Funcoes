## Funcoes sao usadas quando nao sabemos quantos argumentos 
# teremos na chamada da funcoes
#*args ou *  *var
#**wargs ou **  **vars

def vlsoma (*args):
    print(args)

#chamar a funcao
    
vlsoma (1,443,12,33,12,89)

## somar os valores declarados na funcao 

def soma_total(*args):
    total = 0
    for numero in args:
        total = numero+total
    return total

print(soma_total(31,51,89,12,89,10))