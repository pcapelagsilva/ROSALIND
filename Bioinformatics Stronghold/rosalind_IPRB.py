def resolver_iprb(k, m, n):
    t = k + m + n

    prob_nn = (n / t) * ((n - 1) / (t - 1))
    # Dois pais Recessivos:
    '''
    (n/t) = Chance do pai escolhido ser recessivo;
    ((n - 1)/(t - 1)) = Como um indivíduo já foi "excluido", agora restam n-1 recessivos e o total da população cai para t-1;
    Lógica = Se ambos os pais são recessivos, 100% dos filhos serão recessivos. Por isso, não precisamos multiplicar por nenhuma fração.
    '''
    prob_mn = 2 * (m / t) * (n / (t - 1)) * 0.5
    # Um pai Heterozigoto e um Recessivo
    '''
    (m/t) * (n/(t - 1)) = Chance de pegar um Heterozigoto e depois um Recessivo;
    2 * = Mostra que a ordem não importa. Você pode pegar o m primeiro e depois o n, ou o n primeiro e depois o m;
    * 0,5 = De acordo com o Quadro de Punnett, um cruzamento Aa X aa tem 50% de chance de gerar um filho aa.
    '''
    prob_mm = (m / t) * ((m - 1) / (t - 1)) * 0.25
    # Dois pais Heterozigotos
    '''
    (m/t) * ((m - 1)/(t - 1)) = Chance de escolher dois indivíduos heterozigotos seguidos;
    * 0,25 = É o ponto crucial da Primeira Lei de Mendel. No cruzamento Aa X Aa, a chance do filho ser recessivo (aa) é de apenas 25%
    '''

    total_recessivos = prob_nn + prob_mn + prob_mm
    # Probabilidade total de ser recessivo

    return 1 - total_recessivos
    # A resposta é o complemento (1 - recessivo)

print(round(resolver_iprb(20, 29, 15), 5))