# TIPOS DE CRUZEMENTOS DE ALELOS DIFERENTES (A/a B/b):
#2ª Lei de Mendel --> Alelos de genes diferentes (A/a B/b) são herdados de forma independente
'''Se cruzarmos dois indivíduos heterozigotos para dois genes (AaBb X AaBb). a probabilidade do filho ser igual aos pais "AaBb" é sempre de 1/4 (0,25):
    - P(Aa) = 1/2
    - P(Bb) = 1/2
    - P(AaBb) = 1/2 * 1/2 = 1/4
'''
'''tom = AaBb
filhos_por_geração = 2
parceiros = AaBb
Qual a probabilidade de na geração K ter, pelo menos, N indivíduos AaBb??

k = 2**k
chance_de_AaBb = 0.25 # Pela lei de mendel e a situação do exercício (tom e parceiros) o valor sempre vai ser 0.25'''

from math import comb # Importa a função de combinação: n! / (k! * (n-k)!)

def seg_lei_mendel(k, n):
    # 1. DEFINIÇÃO DO ESPAÇO AMOSTRAL
    # Como cada casal tem 2 filhos a cada geração, a população total na geração 'k' é calculada por 2 elevado a 'k'
    pop_total = 2**k

    # 2. 2ª LEI DE MENDEL - PROBABILIDADE FIXA
    # No cruzamento AaBb X AaBb, a chance de um descendente ser AaBb é 1/4 (0.25)
    prob_AaBb = 0.25

    # 3. ACUMULADOR DE PROBABILIDADE
    # Inicia com 0 para somar as chances de sucesso de 'N' até o total da população.
    prob_pelo_menos_n = 0

    # 4. LOOP DE SOMA (PELO MENOS 'N')
    # O problema pede "pelo menos N", então somamos a probabilidade de termos exatamente N, N+1, N+2... até o máximo de indivíduos daquela geração
    for i in range(n, pop_total + 1):

        # 5. FÓRMULA DA DISTRIBUIÇÃO BINOMIAL
        # comb(total_pop, i): Quantas combinações diferentes de 'i' indivíduos podem ser AaBb.
        # (prob_success**i): Probabilidade dos 'i' sucessos ocorrerem.
        # ((1-prob_success)**(total_pop-i)): Probabilidade dos demais não serem AaBb.
        prob_pelo_menos_n += comb(pop_total, i) * (prob_AaBb ** i) * ((1 - prob_AaBb) ** (pop_total - i))

    # 6. RETORNO FORMATADO
    # O Rosalind geralmente pede 3 casas decimais de precisão
    return round(prob_pelo_menos_n, 3)

print(seg_lei_mendel(7, 38))