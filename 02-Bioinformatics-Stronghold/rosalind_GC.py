from Bio import SeqIO

def calcular_gc(sequencia):
    g = sequencia.count("G")
    c = sequencia.count("C")
    return (g + c)/len(sequencia)*100

maior_gc = 0
vencedor_id = ""

for registro in SeqIO.parse("dados_GC.fasta", "fasta"):
    gc_atual = calcular_gc(registro.seq)

    if gc_atual > maior_gc:
        maior_gc = gc_atual
        vencedor_id = registro.id

print(vencedor_id)
print(f"{maior_gc:.6f}")
