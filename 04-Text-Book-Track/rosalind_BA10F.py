import numpy as np

# Configuração para o terminal WSL
np.set_printoptions(precision=3, suppress=True)

def resolver_rosalind_final(theta, sigma, alfabeto, alinhamento):
    n_seqs = len(alinhamento)
    n_cols = len(alinhamento[0])
    
    # 1. Identificar colunas Match
    colunas_match = [j for j in range(n_cols) if sum(1 for i in range(n_seqs) if alinhamento[i][j] == '-') / n_seqs < theta]
    num_m = len(colunas_match)
    
    # 2. Estados (Ordem estrita do Rosalind)
    estados = ['S', 'I0']
    for i in range(1, num_m + 1):
        estados += [f'M{i}', f'D{i}', f'I{i}']
    estados.append('E')
    
    idx_e = {st: i for i, st in enumerate(estados)}
    idx_l = {letra: i for i, letra in enumerate(alfabeto)}
    
    # Matrizes de contagem
    cont_trans = np.zeros((len(estados), len(estados)))
    cont_emiss = np.zeros((len(estados), len(alfabeto)))

    # 3. Contagem de Caminhos
    for seq in alinhamento:
        caminho = ['S']
        m_atual = 0
        for j in range(n_cols):
            if j in colunas_match:
                m_atual += 1
                caminho.append(f'M{m_atual}' if seq[j] != '-' else f'D{m_atual}')
            elif seq[j] != '-':
                if caminho[-1] != f'I{m_atual}':
                    caminho.append(f'I{m_atual}')
        caminho.append('E')

        # Registrar transições e emissões
        res_ptr = 0
        for i in range(len(caminho)-1):
            u, v = caminho[i], caminho[i+1]
            cont_trans[idx_e[u]][idx_e[v]] += 1
            if u[0] in ['M', 'I']:
                while res_ptr < n_cols and seq[res_ptr] == '-': res_ptr += 1
                if res_ptr < n_cols:
                    cont_emiss[idx_e[u]][idx_l[seq[res_ptr]]] += 1
                    res_ptr += 1

    # 4. NORMALIZAÇÃO COM DENOMINADOR FIXO (A CORREÇÃO)
    trans_final = np.zeros_like(cont_trans)
    emiss_final = np.zeros_like(cont_emiss)

    for i, est in enumerate(estados):
        if est == 'E': continue
        
        num = int(''.join(filter(str.isdigit, est))) if any(c.isdigit() for c in est) else 0
        
        # Define os alvos estruturais que DEVEM compor o denominador
        if est in ['S', 'I0']:
            alvos = ['I0', 'M1', 'D1']
        elif num < num_m:
            alvos = [f'M{num+1}', f'D{num+1}', f'I{num}']
        else:
            alvos = [f'I{num}', 'E']
            
        indices_alvo = [idx_e[a] for a in alvos if a in idx_e]
        
        # SOMA ESTRUTURAL: Considera as 3 saídas do Profile HMM
        soma_contagens = np.sum(cont_trans[i, indices_alvo])
        denominador = soma_contagens + (len(indices_alvo) * sigma)
        
        for idx_dest in indices_alvo:
            trans_final[i, idx_dest] = (cont_trans[i, idx_dest] + sigma) / denominador

        # Emissões
        if est[0] in ['M', 'I']:
            denominador_e = np.sum(cont_emiss[i]) + (len(alfabeto) * sigma)
            emiss_final[i] = (cont_emiss[i] + sigma) / denominador_e

    return trans_final, emiss_final, estados

# Dados do seu Input
theta_input = 0.399
sigma_input = 0.01
alf_input = ['A', 'B', 'C', 'D', 'E']
alin_input = ["ED-BCBDAC", "-D-ABBDAC", "ED--EBD-C", "-C-BCB-D-", "AD-BC-CA-", "-DDB-BA-C"]

t, e, nomes = resolver_rosalind_final(theta_input, sigma_input, alf_input, alin_input)

# Impressão para conferência
print("\t" + "\t".join(nomes))
for i, linha in enumerate(t):
    print(nomes[i] + "\t" + "\t".join([f"{val:.3f}" for val in linha]))
