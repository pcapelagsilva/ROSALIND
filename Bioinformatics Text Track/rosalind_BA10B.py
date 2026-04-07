# 1. A String:
# São os dados visíveis, na bioinformática seriam as letras A, C, T, G
x = "xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx"

alfabeto = "x", "y", "z"

# 2. O Caminho:
# Representa o que esta acontecendo "por de trás das câmeras"
# Se estivéssemos falando de clima: A seria Sol e B seria Chuva.
# No modelo abaixo diz em qual estado o modelo estava em cada segundo.
caminho = "BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB"

emissão = {
    'A': {'x':0.612, 'y':0.314, 'z':0.074},
    'B': {'x':0.346, 'y':0.317, 'z':0.336}
}

prob = 1.0

for i in range (len(x)):
    estado_atual = caminho[i]
    simbolo_emitido = x[i]

    prob *= emissão[estado_atual][simbolo_emitido]

print(prob)
