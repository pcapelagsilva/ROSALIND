from Bio import SeqIO
from Bio.Seq import Seq

def resolver_splicing(arquivo_fasta):
    records = list(SeqIO.parse(arquivo_fasta, "fasta"))

    dna_s = str(records[0].seq)

    introns = [str(r.seq) for r in records[1:]]

    for intron in introns:
        dna_s = dna_s.replace(intron, "")

    proteina = Seq(dna_s).translate(to_stop=True)

    return str(proteina)

print(resolver_splicing("introns_SPLC.fasta"))
