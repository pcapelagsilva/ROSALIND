from Bio import Entrez #O código 'Entrez' é um módulo do BioPython que permite que o script se conecte à internet e faça a pergunta diretamente ao banco de dados...

# 1. Identificação para o NCBI
Entrez.email = "pedrocapelabioinfo@gmail.com"

# 2. Definição dos dados do problema
# É importante temos em mente que o padrão internacional de Banco de Dados exige que a data seja escrita da seguinte forma: ANO/MÊS/DIA
genero = "Printzina"
data_inicio = "2007/12/26"
data_fim = "2009/06/28"

# 3. Constuir uma 'query' (pergunta) em um formato que o NCBI entende
# Queremos o organismo AND(e) o período de publicação [PDAT]
# [Organism] --> Diz ao NCBI: "Não procure essa palavra em qualquer lugar, procure apenas no campo de espécie/gênero"
# [PDAT] --> Significa: Publication Date (Data de Publicação)
consulta = f'"{genero}"[organism] AND ("{data_inicio}"[PDAT] : "{data_fim}"[PDAT])'

# 4. Usamos a função 'esearch' para pesquisar no banco desejado, no caso 'nucleotide'
# handle --> É como um "cano" aberto entre o computador e o servidor. É importante que sabemos que os dados ainda não estão no computador, o "cano" só está aberto esperando para ser lido
# Entrez.read --> "Puxa" as informações através do "cano" e as transformam em um formato que o Python possa ler (geralmente um dicionário)
# record --> Salva os dados na memória do seu PC nesta variável
handle = Entrez.esearch(db="nucleotide", term=consulta)
record = Entrez.read(handle)

# 5. O resultado de 'Count' nos diz quantos registros foram encontrados
print(record["Count"])