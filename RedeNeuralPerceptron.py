quantidadeTerminais = 4
quantidadePadroes = 6
quantidadeTeste = 2
taxaAprendizado = 0.4

padroes = []

for i in range(quantidadePadroes):
    line = []
    for j in range(quantidadeTerminais + 2):
        line.append(0)

    padroes.append(line)

sim = 1
nao = 0
grandes = 1
pequenas = 0
doente = 1
saudavel = -1

padroes[0][0] = 1           # valor 1 da limiar
padroes[0][1] = sim         # Terminal 1
padroes[0][2] = sim         # Terminal 2
padroes[0][3] = pequenas    # Terminal 3
padroes[0][4] = sim         # Terminal 4
padroes[0][5] = doente      # d

padroes[1][0] = 1           # valor 1 da limiar
padroes[1][1] = nao         # Terminal 1
padroes[1][2] = nao         # Terminal 2
padroes[1][3] = grandes     # Terminal 3
padroes[1][4] = nao         # Terminal 4
padroes[1][5] = saudavel    # d

padroes[2][0] = 1           # valor 1 da limiar
padroes[2][1] = sim         # Terminal 1
padroes[2][2] = sim         # Terminal 2
padroes[2][3] = pequenas    # Terminal 3
padroes[2][4] = nao         # Terminal 4
padroes[2][5] = saudavel    # d

padroes[3][0] = 1           # valor 1 da limiar
padroes[3][1] = sim         # Terminal 1
padroes[3][2] = nao         # Terminal 2
padroes[3][3] = grandes     # Terminal 3
padroes[3][4] = sim         # Terminal 4
padroes[3][5] = doente      # d

padroes[4][0] = 1           # valor 1 da limiar
padroes[4][1] = sim         # Terminal 1
padroes[4][2] = nao         # Terminal 2
padroes[4][3] = pequenas    # Terminal 3
padroes[4][4] = sim         # Terminal 4
padroes[4][5] = saudavel    # d

padroes[5][0] = 1           # valor 1 da limiar
padroes[5][1] = nao         # Terminal 1
padroes[5][2] = nao         # Terminal 2
padroes[5][3] = grandes     # Terminal 3
padroes[5][4] = sim         # Terminal 4
padroes[5][5] = doente      # d

pesos = []
pesos.append(0)          #limiar
pesos.append(0.5)        #w1
pesos.append(0.5)        #w2
pesos.append(0.66)       #w3
pesos.append(0.75)       #w4

#Treinamento
isTreined = False

while(not isTreined):
    contador = 0
    for indexPadroes in range(quantidadePadroes):
        v = 0
        for indexTerminais in range(quantidadeTerminais+1):
            v = v + padroes[indexPadroes][indexTerminais] * pesos[indexTerminais]
        v = round(v, 2)
    
        if v >= 0 :
            y = 1
        else:
            y = -1
        
        if(y != padroes[indexPadroes][quantidadeTerminais+1]):
            for indexPesos in range(len(pesos)):
                pesos[indexPesos] = round(pesos[indexPesos] + (taxaAprendizado * padroes[indexPadroes][indexPesos]) * (padroes[indexPadroes][quantidadeTerminais+1] - (y)),2)
        else:
            contador = contador + 1
    if(contador == quantidadePadroes):
        isTreined = True

print(pesos)

#Testes
teste = []

for i in range(quantidadeTeste):
    line = []
    for j in range(quantidadeTerminais + 2):
        line.append(0)

    teste.append(line)

indefinido = 0

teste[0][0] = 1             # valor 1 da limiar
teste[0][1] = nao           # Terminal 1
teste[0][2] = nao           # Terminal 2
teste[0][3] = pequenas      # Terminal 3
teste[0][4] = sim           # Terminal 4
teste[0][5] = indefinido    # d

teste[1][0] = 1             # valor 1 da limiar
teste[1][1] = sim           # Terminal 1
teste[1][2] = sim           # Terminal 2
teste[1][3] = grandes       # Terminal 3
teste[1][4] = sim           # Terminal 4
teste[1][5] = indefinido    # d

for indexTeste in range(len(teste)):
    v = 0
    for indexTerminais in range(quantidadeTerminais+1):
        v = v + teste[indexTeste][indexTerminais] * pesos[indexTerminais]
    v = round(v, 2)

    if v >= 0 :
        teste[indexTeste][quantidadeTerminais+1] = 1
    else:
        teste[indexTeste][quantidadeTerminais+1] = -1

for index in range(len(teste)):

    if(teste[index][5] == 1):
        diagnostico = 'doente'
    else:
        diagnostico = 'saudavel'
    
    print('Paciente ' + str(index) + ' está: ' + str(diagnostico))