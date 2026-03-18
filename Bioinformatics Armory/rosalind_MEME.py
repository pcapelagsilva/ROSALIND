from Bio import SeqIO
from collections import Counter

def achar_motivo_rapido(fasta_file, k=15):
    records = list(SeqIO.parse(fasta_file, "fasta"))
    seqs = [str(r.seq) for r in records[:3]]


    k_mers = [seqs[0][i:i+k] for i in range(len(seqs[0]) - k + 1)]

    for kmer in k_mers:
        if all(kmer[:8] in s for s in seqs[1:]):
            return kmer
        
print(f"Possivel motivo = {achar_motivo_rapido('rosalind_meme_seq.fasta')}")