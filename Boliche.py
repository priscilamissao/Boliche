
def PistaEpinos(pinos):
    for i in pinos:
        print(i, end='')
    print()
       
pista = [
    'I',' ','I',' ','I',' ','I','\n',
    ' ','I',' ','I',' ','I',' ','\n',
    ' ',' ','I',' ','I',' ',' ','\n',
    ' ',' ',' ','I',
]

posicaoP = {
    '1': 27,
    '2': 18,
    '3': 20,
    '4': 9,
    '5': 11,
    '6': 13,
    '7': 0,
    '8': 2,
    '9': 4,
    '10': 6,
}

PistaEpinos(pista)

# Só cuidado aqui. Dá a impressão que o usuário vai entrar com alguma informação. 
# Talvez seria legal deixar como está, mas apenas mudar o texto pra algo como: A sua jogada é:
# E aí imprimir a variavel jogadas, já que pra alterar a jogada é preciso mudar a variável no próprio código.
print("Faça sua jogada!!!!\n")
jogadas = ['6','5','8', '9']

for pino in jogadas:
    posicao = posicaoP[pino]
    pista[posicao] = ' '
print()

PistaEpinos(pista)
# E aqui é interessante incluir uma verificação se há algum pino restante. [
# Da forma como está, o código sempre imprime isso, mesmo que todos os pinos tenham caído.
print("Boa tentativa, porem não conseguiu um stike!!!\n")
print("Game Over")