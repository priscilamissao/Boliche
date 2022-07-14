
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

print("Faça sua jogada!!!!\n")
jogadas = ['3','5','9']

for pino in jogadas:
    posicao = posicaoP[pino]
    pista[posicao] = ' '
print()

PistaEpinos(pista)
print("Boa tentativa, porem não conseguiu um stike!!!\n")
print("Game Over")