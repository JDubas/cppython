alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
rotor = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
reflector = ["z","a","q","x","s","w","c","d","e","v","f","r","b","g","t","n","h","y","m","j","u","k","i","l","o","p"]

mensagem = input("Digite a mensagem para cifrar: ")
posicao = []
rotorPosicao = []
reflectorPosicao = []
mensagemCifrada = ""
dPosicao =[]
dReflctorPosicao = []
dAlphabet = []
mensagemDecifrada = ""
ultima = []
letra = 0
dLetra = 0

for x in range(len(mensagem)):
    for y in range(len(alphabet)):
        if mensagem[x] == alphabet[y]:
            letra = y + 1
            if letra == 26:
                letra = 0
            posicao.append(letra)

print("posicao ",posicao)


for x in range(len(posicao)):
    rotorPosicao.append(rotor[posicao[x]])

print("posicao rotor ", rotorPosicao)

for x in range(len(rotorPosicao)):
    for y in range(len(reflector)):
        if rotorPosicao[x] == reflector[y]:
            reflectorPosicao.append(y)

print("posicao refletor ", reflectorPosicao)

for x in range(len(reflectorPosicao)):
    mensagemCifrada = mensagemCifrada + alphabet[reflectorPosicao[x]]

print("Mensagem cifrada: " , str(mensagemCifrada))

for x in range(len(mensagemCifrada)):
    for y in range(len(alphabet)):
        if mensagemCifrada[x] == alphabet[y]:
            dPosicao.append(y)
print("posicao alphabet ", dPosicao)

for x in range(len(dPosicao)):
        dReflctorPosicao.append(reflector[dPosicao[x]])

print("posicao refletor ", dReflctorPosicao)
for x in range(len(dReflctorPosicao)):
    for y in range(len(alphabet)):
        if dReflctorPosicao[x] == alphabet[y]:
            dAlphabet.append(y)
    
print("posicao alphabet ", dAlphabet)

for x in range(len(dAlphabet)):
    dLetra = dAlphabet[x] - 1
    if dLetra == -1:
        dLetra = 25
    ultima.append(rotor[dLetra])



print("Mensagem decifrada; " , str(ultima))