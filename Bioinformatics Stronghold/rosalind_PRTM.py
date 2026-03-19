# Tabela de massas monoisotópicas padrão Rosalind
TABELA_MASSAS = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

# 1ª FORMA DE RESOLUÇÃO:
'''def conferir_e_calcular(arquivo):
    with open(arquivo, 'r') as f:
        # Limpa espaços e quebras de linha
        proteina = f.read().strip().replace('\n', '').replace('\r', '')
    
    massa = sum(TABELA_MASSAS[aa] for aa in proteina if aa in TABELA_MASSAS)
    
    print(f"--- RELATÓRIO ---")
    print(f"Aminoácidos lidos: {len(proteina)}")
    print(f"Resultado: {round(massa, 3)}")
    print(f"Resultado (3 casas): {massa:.3f}")
    print(f"Resultado (4 casas para conferir): {massa:.4f}")

# Execute apontando para o seu arquivo
conferir_e_calcular("dados_PRTM.txt") '''

# 2ª FORMA DE RESOLUÇÃO:
'''def calcular_massa(proteina):
    # Limpa a string para garantir que não há espaços ou enters
    proteina_limpa = proteina.strip().replace('\n', '').replace('\r', '')
    
    # Soma a massa de cada aminoácido
    massa_total = sum(TABELA_MASSAS[aa] for aa in proteina_limpa if aa in TABELA_MASSAS)
    
    # Retorna o valor arredondado para 3 casas decimais
    return round(massa_total, 3)

# ==========================================
# 1. TESTANDO O SAMPLE DATASET (Prova de Fogo)
# ==========================================
sample_dataset = 'GSAYCHPNDEAGLEFRDGTVHSWFWDQGCRKMAVFGYYFYQNQNCKEKCHHTHSKIYMFAMGWRNGKCLGSAMNHCYQNRTQFMWEPYEQDTKTYWENHMEGRNAPNCVSFHKYHCKAFKKALKGYKFDGMTWDSTTGYFCQNMHVNMTLLQKQHEMHRVTLENQSMLRTHEMTMRMEGLEDFQTEVAWTDQTQPIQWKWNWCVMMKFCKRCSHCPMPYRGQYKYKNIIGKYMYPHWEFRLMACPSANHTCYVWTNWFCKQWPSCMRPYQHQVLICDMCHCSIVLDVIVDCLIVTFRMNHQWTVISKYQTFHMICMGWCWPSVGLFDYWINYLDYTCELHPDGVVPSFCTGQAGRTLYGILKDMPWCNLLKYSAHVDWHGICHCIIIIEFREEPMCYHCGQRFWDYLDFYTALHRFEQSYYQFYCCMGQAKGFMWHFHYDLANVQIIYNGWMYEAPRTAGCRMYSGHWWWNRQNHLDPYYRVPERLMDVLVQRRKGMAMFKCVGKNAYYNFAHFHCQHHFKHELPLCQIGSAACEYPMVMQPFWKCEYAVMPTATRVKDCECESRKWDKVMYITKDESACPWYCPTHGKGLELFYLLNKDLNLLTRYQDSVDKMIDRIVMVWMKGAGHTSNWTNLTLILCHMYESNQYWTRALLGQCRHGTASQDSFYGVGSGEEWIQEPPTARVYQKPHPGMDERGGYHWIPIVLCMFNLYQETNWTQLGQEAWKNYQHMAVGETDIQHGDHSSRSWWPTIMTENRTGGTCYKKISIDYFELSWKSHICKIQLVSLKFVMGRQPYIEQFFERTKNLKCRACKYTIPWPKHRGCIMASPSFTKCNEGAHCLSCPYCDNGVDLKENKNVAYSAIKPMCHLAHVCFYQAKLIYPMACDCFPLVPIFQHCAK'
resultado_teste = calcular_massa(sample_dataset)

print(f"--- TESTE ---")
print(f"Sequência: {sample_dataset}")
print(f"Resultado do código: {resultado_teste}")

# ==========================================
# 2. RESOLVENDO O SEU DATASET REAL
# ==========================================
# Descomente as linhas abaixo (tire os '#' do início) quando quiser ler o arquivo real.

# nome_do_arquivo = "rosalind_prtm.txt" 
# try:
#     with open(nome_do_arquivo, 'r') as f:
#         sequencia_real = f.read()
#     resultado_real = calcular_massa(sequencia_real)
#     print(f"--- RESULTADO OFICIAL ---")
#     print(f"O peso da sua proteína é: {resultado_real}")
# except FileNotFoundError:
#     print(f"Arquivo '{nome_do_arquivo}' não encontrado. Baixe do Rosalind e coloque na pasta.")'''