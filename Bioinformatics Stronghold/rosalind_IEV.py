#         Alelos  | Probabilidade de filhos dominantes | Filhos dominantes |
# casal_0 = AA-AA |             (100%)                 |          2        |
# casal_1 = AA-Aa |             (100%)                 |          2        |
# casal_2 = AA-aa |             (100%)                 |          2        |
# casal_3 = Aa-Aa |             (75%)                  |         1.5       |
# casal_4 = Aa-aa |             (50%)                  |          1        |
# casal_5 = aa-aa |             (0%)                   |          0        |

# 1ª Resolução:
'''casal_de_filhos = [18560, 17228, 18996, 18095, 19008, 18457]

probabilidade_filhos_dom = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]

calculo_dominancia = (casal_de_filhos[0]*probabilidade_filhos_dom[0] + casal_de_filhos[1]*probabilidade_filhos_dom[1] + casal_de_filhos[2]*probabilidade_filhos_dom[2] + casal_de_filhos[3]*probabilidade_filhos_dom[3] + casal_de_filhos[4]*probabilidade_filhos_dom[4] + casal_de_filhos[5]*probabilidade_filhos_dom[5])

print(calculo_dominancia) '''
# 2ª Resolução:
'''casais = [18560, 17228, 18996, 18095, 19008, 18457]
resultado = (casais[0]*2 + casais[1]*2 + casais[2]*2 + casais[3]*1.5 + casais[4]*1 + casais[5]*0)

print(resultado)'''
# 3ª Resolução:
'''def calcular_expectativa_dominante(caminho_arquivo):
    # Lista de descendentes dominantes esperados por casal
    # Referente a: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    esperado = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]
    
    try:
        with open(caminho_arquivo, 'r') as f:
            # Lê a linha, divide pelos espaços e converte cada número para inteiro
            casais = list(map(int, f.read().split()))
        
        # Multiplica a quantidade de casais pelo seu respectivo "esperado" e soma tudo
        expectativa_total = sum(c * p for c, p in zip(casais, esperado))
        
        print(f"Expectativa de descendentes dominantes: {expectativa_total}")
        
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# Execução
calcular_expectativa_dominante("dados_IEV.txt")'''