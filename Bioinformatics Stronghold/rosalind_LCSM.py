# Abre a caixa de ferramentas de Bioinformática
# SeqIO --> É o padrão para lidar com arquivos FASTA.
from Bio import SeqIO

def find_lcs(fasta_file):
    # Transforma o arquivo em uma lista de objetos
    records = list(SeqIO.parse(fasta_file, "fasta"))
    # "Limpa" os dados. Arquivos FASTA possuem cabeçalho (>Rosalind_1), mas para busca, só nos interessam a sequência de DNA (A, C, T, G). Transformando tudo em texto (string)
    seqs = [str(r.seq) for r in records]

    # Ordena as sequências de forma crescente
    seqs.sort(key=len)
    # Escolhe a menor sequência para se a "Base de testes", isso importa pois, se a menor sequ~encia tem 100 letras, é impossível existir algo comum a todos que tenha 101 letras, economizando processamento do PC
    shortest_seq = seqs[0]
    n = len(shortest_seq)

    # Inicia no tamanho máximo (n) e vai diminuindo até 1. Isso funciona com a seguinte estratégia, como queremos a maior substring, começamos testando a grande. A primeira que funcionar é nossa resposta final.
    for length in range(n, 0, -1):
        # Cria uma "janela deslizante", se testarmos o tamanho 10, por exemplo, ele olhas as letras de 0 a 10, de pois de 1 a 11, de 2 a 12... até o fim da sequência base
        for start in range(n - length + 1):
            susbtring = shortest_seq[start:start + length]
            # Para cada "janela" que recortamos, o código pergunta: "Este pedaço está na sequência 2? e na 3? e na 100? ..."
            # Se a resposta for SIM para todas, o return encerra o programa e te entrega a sequência vencedora
            if all(susbtring in s for s in seqs[1:]):
                return susbtring
    return ""

# Chama a função passando o nome do arquivo baixado.
print(find_lcs("dados_LCSM.fasta"))