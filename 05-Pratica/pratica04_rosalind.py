'''
EXERCÍCIO 1: O Contador de GC Deslizante (Janelas)
-------------------------------------------------------------------------
CONTEXTO: Áreas do genoma com alto conteúdo GC (Ilhas CpG) costumam estar 
associadas a regiões promotoras de genes.

DESAFIO:
1. Crie uma função que receba uma sequência de DNA e um tamanho de 
   janela (ex: 100).
2. O script deve percorrer a sequência e calcular a porcentagem de GC 
   para cada janela, "deslizando" 1 base por vez.
3. Retorne uma lista com os valores de GC encontrados.

DICA: Use o conceito de slicing de strings: sequencia[i : i + janela]
-------------------------------------------------------------------------
'''
'''dna_exemplo = "ATATATATATGCGCGCGCGCTATATATATA"
tamanho = 5

def valor_gc(sequencia, tamanho_janela):
    resultado = []
    for i in range(len(sequencia) - tamanho_janela + 1):
        janela = sequencia[i: i + tamanho_janela].upper()
        gc = janela.count("G") + janela.count("C")
        porcentagem_gc = (gc / tamanho_janela) * 100

        resultado.append(porcentagem_gc)

    return resultado

print(f"A lista de valores é igual a: {valor_gc(dna_exemplo, tamanho)}")
print(f"\nEnquanto a quantidade total de janelas é:{len(valor_gc(dna_exemplo, tamanho))}")'''

'''
EXERCÍCIO 2: Filtro de Qualidade de Sequências (FASTQ)
-------------------------------------------------------------------------
CONTEXTO: Diferente do FASTA, o formato FASTQ possui uma 4ª linha com 
caracteres que representam a qualidade (Phred Score) de cada base.

DESAFIO:
1. Simule a leitura de uma 4ª linha de um arquivo FASTQ (ex: "@ABCDE").
2. Converta cada caractere para seu valor numérico usando a fórmula: 
   Q = ord(caractere) - 33
3. Calcule a média de qualidade da sequência e diga se ela deve ser 
   "aprovada" (média > 30) ou "rejeitada".
-------------------------------------------------------------------------
'''

'''def analisar_qualidade_fasta(linha_qualidade):
    score = []
    # 1. Olhamos cada símbolo de qualidade presente na linha
    for simbolo in linha_qualidade:
        # 2. Transforma o símbolo em número e subtraímos 33
        # Exemplo: Se o símbolo for '@', ord('@') é 64. 64 - 33 = 31
        qualidade = ord(simbolo) - 33

        # 3. Guardamos esse número em nossa lista de score
        score.append(qualidade)

    # 4. Calculamos a média: (Soma de todos os valores) / (Quantidade de valoes)
    soma_total = sum(score)
    quantidade = len(score)
    media = soma_total / quantidade

    return media'''

# --- FAZENDO O EXERCÍCIO 02 ---
'''qualidade_teste = "@ABCDE"
media_final = analisar_qualidade_fasta(qualidade_teste)

print(f"Símbolos lidos: {qualidade_teste}")
print(f"Média de qualidade calculada: {media_final:.2f}")

# Na Bioinformáica, a média acima de 30 é considerada excelente!!
if media_final >= 30:
    print("Resultado: Esta sequência é confiável para pesquisa!!!")
else:
    print("Resultado não confiável para pesquisa... CUIDADO!!")'''


'''
EXERCÍCIO 3: Identificador de Open Reading Frames (ORF)
-------------------------------------------------------------------------
CONTEXTO: Uma ORF é uma parte da sequência que tem potencial para ser 
traduzida, começando com um Start Codon e terminando em um Stop Codon.

DESAFIO:
1. Dada uma sequência de DNA, encontre a posição (índice) onde começa 
   o primeiro "ATG" e onde termina o primeiro Stop Codon (TAA, TAG ou TGA) 
   que esteja no mesmo frame.
2. Extraia apenas esse trecho (a ORF) e ignore o restante da sequência.

DICA: Lembre-se que o Stop Codon deve estar em uma posição múltipla 
de 3 em relação ao Start Codon.
-------------------------------------------------------------------------
'''

'''def seq_orf (seq):
    inicio  = seq.find("ATG")
    if inicio == -1:
        return "Nenhuma ORF encontrada"
    
    for i in range(inicio, len(seq), 3):
        codon = seq[i:i+3]

        if codon in ["TAA", "TAG", "TGA"]:
            orf_final = seq[inicio: i+3]
            return orf_final
    
    return "Início encontrado, mas sem Stop Codon no frame."'''

# --- TESTANDO O CÓDIGO ---
'''dna = "GGCCATGCCCCGCTAGCGGTAGTAAATTT"

resultado = seq_orf(dna)
print(f"Sequência original: {dna}")
print(f"ORF encontrada: {resultado}")'''

'''
EXERCÍCIO 4: Identificador de Mutação de Ponto (SNP)
-------------------------------------------------------------------------
CONTEXTO: Um SNP (Single Nucleotide Polymorphism) ocorre quando uma única 
base na sequência difere entre indivíduos.

DESAFIO:
1. Receba duas sequências de DNA de mesmo tamanho (Referência e Amostra).
2. O script deve comparar as duas e retornar uma lista de strings 
   indicando a posição e a mudança.
   Exemplo: "Posição 4: A -> G"

DICA: Use a função zip(seq1, seq2) para comparar as letras lado a lado.
-------------------------------------------------------------------------
'''

'''
EXERCÍCIO 5: Localizador de Motifs com "Mismatches"
-------------------------------------------------------------------------
CONTEXTO: Na biologia, proteínas nem sempre se ligam a sequências 
perfeitas; às vezes, elas aceitam um ou dois erros na sequência.

DESAFIO:
1. Dada uma sequência alvo (ex: "GATACA") e um genoma longo.
2. Encontre todas as posições onde o "GATACA" aparece com, no máximo, 
   1 letra errada.
   Exemplo: "GATAGA" seria aceito, mas "GATCCC" não.

DICA: Reutilize a lógica da janela deslizante e compare a janela 
atual com o seu motif alvo.
-------------------------------------------------------------------------
'''

'''
EXERCÍCIO 6: Simulador de Enzima de Restrição (Corte)
-------------------------------------------------------------------------
CONTEXTO: Enzimas de restrição "cortam" o DNA em locais específicos. 
A enzima EcoRI, por exemplo, corta sempre na sequência "GAATTC".

DESAFIO:
1. Crie uma função que receba uma sequência de DNA.
2. Onde encontrar "GAATTC", o script deve "quebrar" a string e 
   retornar uma lista com os fragmentos resultantes.

DICA: O Python tem o método .split() que faz exatamente isso para strings!
-------------------------------------------------------------------------
'''