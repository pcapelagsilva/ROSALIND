# Abre a caixa de ferramentas de Bioinformática
# SeqIO --> É o padrão para lidar com arquivos FASTA.
from Bio import SeqIO

def find_lcs(fasta_file):
    records = list(SeqIO.parse(fasta_file, "fasta"))
    seqs = [str(r.seq) for r in records]

    seqs.sort(key=len)
    shortest_seq = seqs[0]
    n = len(shortest_seq)

    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            susbtring = shortest_seq[start:start + length]
            if all(susbtring in s for s in seqs[1:]):
                return susbtring
    return ""

print(find_lcs("dados_LCSM.fasta"))