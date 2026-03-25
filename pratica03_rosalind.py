from Bio import Entrez, SeqIO

# Identificação para entrar no NCBI
Entrez.email: "pedrocapelabioinfo@gmail.com"

# 1. Busca o ID específico
id_busca = input("Digite o ID que você esta buscando: ")

print(f"Conectando ao NCBI para baixar a sequência {id_busca}...")

# 2. Fazendo o download (efetch) do ID desejado
# rettype="fasta" baixa em um formato que já conhecemos
handle = Entrez.efetch(db="nucleotide", id=id_busca, rettype="fasta", retmode="text")

# 3. Lê o arquivo FASTA baixado usando o SeqIO (módulo de entrada/saída)
registro = SeqIO.read(handle, "fasta")
handle.close()

print(f"--- Dados da Sequência ---")
print(f"ID: {registro.id}")
print(f"Descrição: {registro.description}")
print(f"Tamanho: {len(registro.seq)} bp")
print(f"Conteúdo GC: {registro.seq.count('G') + registro.seq.count('C') / len(registro.seq) * 100:.2f}%")
print(f"Início da sequência: \n{registro.seq[:50]}...")
print(20*'-')