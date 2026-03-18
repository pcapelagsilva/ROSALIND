from Bio import Entrez

# 1. Idenficação (Regra de etiqueta do NCBI)
Entrez.email = "pedrocapelabioinfo@gmail.com"

# 2. Dados do problema
genero = input("Insira o genero: ")
data_incio = input("Insira a data de início: ")
data_final = input("Insira a data final: ")

# 3. Construindo a pergunta para o servidor
#  A data deve ser ANO/MÊS/DIA para o NCBI
consulta = f'"{genero}"[Organism] AND ("{data_incio}"[PDAT] : "{data_final}"[PDAT])'

# 4. Enviando a busca
# db="nucleotide" foca no banco específico pedido
# esearch --> Envia seus termos de busca (gênero, data, etc.) para o servidor.
# handle --> É o canal por onde os dados estão passando.
# read --> Ele lê o texto bruto que veio do servidor (que geralmente vem em um formato chato chamado XML) e o transforma em um Dicionário do Python.
handle = Entrez.esearch(db="nucleotide", term=consulta)
registro = Entrez.read(handle)
handle.close()

# 5. O campo "Count" traz o número total de entradas
print(registro["Count"])