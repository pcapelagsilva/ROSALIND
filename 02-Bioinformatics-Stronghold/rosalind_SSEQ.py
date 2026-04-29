def ler_fasta(caminho_arquivo):
    sequencia = []
    seq_atual = ""
    with open(caminho_arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha: continue
            if linha.startswith(">"):
                if seq_atual:
                    sequencia.append(seq_atual)
                    seq_atual = ""
            
            else:
                seq_atual += linha
        if seq_atual:
            sequencia.append(seq_atual)
    return sequencia

def encontrar_spliced_motif(s, t):
    indices = []
    posicao_atual_s = 0

    # Para cada base no motif t
    for base in t:
        # Procuramos a base em s a partir de onde paramos
        while posicao_atual_s < len(s):
            if s[posicao_atual_s] == base:
                indices.append(posicao_atual_s + 1)
                posicao_atual_s += 1
                break

            posicao_atual_s += 1

    return indices

if __name__ == "__main__":
    caminho = "rosalind_SSEQ.txt"
    
    try:
        seq = ler_fasta(caminho)
        s, t = seq[0], seq[1]

        resultado = encontrar_spliced_motif(s, t)

        print(*(resultado))
    
    except FileNotFoundError:
        print(f"Erro: O Arquivo '{caminho}' não foi encontrado!!")