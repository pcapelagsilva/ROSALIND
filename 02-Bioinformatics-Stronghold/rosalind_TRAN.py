def ler_fasta(caminho_arquivo):
    '''Lê o arquivo FASTA e retorna uma lista com as sequências'''
    sequencias = []
    seq_atual = ""
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith(">"):
                if seq_atual:
                    sequencias.append(seq_atual)
                    seq_atual = ""
            else:
                seq_atual += linha
        if seq_atual:
            sequencias.append(seq_atual)
    return sequencias
            

def calcular_razao(s1, s2):
    transicoes = 0 # Troca das bases do mesmo grupo químico
    transversoes = 0 # Troca das bases entre grupos diferentes (Purinas <--> Pirimidina)

    # Conjunto de tipos de bases
    purinas = {'A', 'G'}
    pirimidinas = {'C', 'T'}

    for b1, b2 in zip(s1, s2):
        if b1 != b2: # Só nos interessam os mismatches (distância de Hamming)
            # Verifica se ambos pertencem ao mesmo grupo (Transição)
            if b1 != b2:
            # Transição: Ambas são purinas OU ambas são pirimidinas
                if (b1 in purinas and b2 in purinas) or (b1 in pirimidinas and b2 in pirimidinas):
                    transicoes += 1
                else:
                    # Se não for do mesmo grupo, é Transversão
                    transversoes += 1
    
    return transicoes/transversoes

# --- EXECUÇÃO USANDO ARQUIVO DE TEXTO ---
if __name__ == "__main__":
    caminho = "rosalind_tran.txt"

    try:
        seqs = ler_fasta(caminho)
        if len(seqs) >= 2:
            resultado = calcular_razao(seqs[0], seqs[1])
            print(f"{resultado:.11f}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado")

# --- EXECUÇÃO DIRETO NO CÓDIGO ---
'''s1 ="GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

resultado = calcular_razao(s1, s2)
print(f"{resultado:.11f}")'''