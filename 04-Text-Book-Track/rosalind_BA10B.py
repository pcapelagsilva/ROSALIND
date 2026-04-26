# 1. A String:
# São os dados visíveis, na bioinformática seriam as letras A, C, T, G
x = "yxyyxzyzyzxxyyyxyzzyxyyyxxyyyyzxxxxyxxxxxxyxyxxxxy"

alfabeto = "x", "y", "z"

# 2. O Caminho:
# Representa o que esta acontecendo "por de trás das câmeras"
# Se estivéssemos falando de clima: A seria Sol e B seria Chuva.
# No modelo abaixo diz em qual estado o modelo estava em cada segundo.
caminho = "BABABBBBBABBABABBBBBAAABABBABBAAAABABBABBBAAABBBAA"

emissão = {
    'A': {'x':0.49, 'y':0.264, 'z':0.246},
    'B': {'x':0.517, 'y':0.085, 'z':0.398}
}

prob = 1.0

for i in range (len(x)):
    estado_atual = caminho[i]
    simbolo_emitido = x[i]

    prob *= emissão[estado_atual][simbolo_emitido]

print(prob)
