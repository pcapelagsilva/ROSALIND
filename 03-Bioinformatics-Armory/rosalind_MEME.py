# 1ª Resolução Através do Python:
from Bio import SeqIO
from collections import Counter
import os

arquivo = 'rosalind_meme_seq.fasta'


def achar_motivo_rapido(fasta_file, k=15):
    records = list(SeqIO.parse(fasta_file, "fasta"))
    seqs = [str(r.seq) for r in records[:3]]


    k_mers = [seqs[0][i:i+k] for i in range(len(seqs[0]) - k + 1)]

    for kmer in k_mers:
        if all(kmer[:8] in s for s in seqs[1:]):
            return kmer

if os.path.exists(arquivo):
    print(f"Possível motivo = {achar_motivo_rapido(arquivo)}")
else:
    print(f"❌ ERRO: O arquivo '{arquivo}' não foi encontrado na pasta atual!")
    print(f"Pasta atual do terminal: {os.getcwd()}")
        
#print(f"Possivel motivo = {achar_motivo_rapido('rosalind_meme_seq.fasta')}")

# 2ª Resolução através do Site MEME:
'''# 🧬 Guia de Uso: MEME Suite para Rosalind (Problema MEME)

Este guia serve para identificar motivos (motifs) em sequências de proteínas quando o Rosalind exige uma **Regular Expression** de tamanho específico.

## 🚀 Passo 1: Acesso ao Servidor
   1. Acesse o site oficial do MEME (Classic Mode):
   - [meme-suite.org/tools/meme](https://meme-suite.org/tools/meme)

## 🛠️ Passo 2: Configuração do Job (Parâmetros)
Para garantir que o resultado bata com o que o Rosalind pede:

   1. **Select the motif site distribution:** - Escolha: `One Occurrence Per Sequence (OOPS)`
   - *Isso diz ao programa que o motivo aparece exatamente uma vez em cada sequência.*

   2. **Select the number of motifs:**
   - Deixe em `1` (geralmente o Rosalind só quer o melhor).

   3. **Advanced Options (Crucial):**
   - **Motif Width:** No campo `Min`, coloque `20` (ou o tamanho que o exercício pedir).
   - No campo `Max`, coloque `50`.

## 🔍 Passo 3: Identificando a Resposta
Assim que o processamento terminar e a página de resultados abrir:

   1. Localize o **Motif 1**.
   2. Abaixo do gráfico de Logo (letras coloridas), procure a linha:
   - **`Regular Expression`**
   3. A resposta será algo parecido com isto:
   - `DLWWCWIPVHK[NK]PHSFLKTWSPAAGHRGWQFDHNFF`

## ⚠️ Dicas de Ouro
- **O que são os colchetes `[]`?** Significam que naquela posição a proteína pode ter qualquer um daqueles aminoácidos.
- **Erro de arquivo:** Se o MEME não aceitar seu arquivo, verifique se ele está no formato FASTA correto (começando com `>`).'''
