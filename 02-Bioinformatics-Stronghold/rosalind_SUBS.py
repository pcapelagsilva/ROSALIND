s = input("Digite a 1ª sequencia: ").strip().upper()
t = input("Digite a 2ª sequencia: ").strip().upper()

def encontrar_motivos(s, t):
    posiçao = []
    tamanho_s = len(s)
    tamanho_t = len(t)

    for base in range(tamanho_s - tamanho_t + 1):
        if s[base:base+tamanho_t] == t:
            posiçao.append(str(base+1))

    return " ".join(posiçao)

resultado = encontrar_motivos(s, t)
print(resultado)
