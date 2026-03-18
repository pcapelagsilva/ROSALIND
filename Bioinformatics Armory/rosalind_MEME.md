-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
ESTUDO DE CASO: DESCOBERTA DE MOTIVOS (MEME SUITE)
--------------------------------------------------
Objetivo: Encontrar padrões ocultos (motivos) em sequências de proteínas desconhecidas.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

--> O QUE É UM MOTIVO?
   Um motivo é uma sequência de aminoácidos conservada que geralmente possui uma 
   função biológica importante (ex: sítio de ligação ou centro catalítico).

--------------------------------------------------

--> POR QUE USAR O MEME?
   Diferente de uma busca comum (como o .find()), o MEME usa algoritmos 
   estatísticos para achar padrões que não são 100% idênticos. Ele identifica 
   o que é mais provável aparecer em cada posição.

--------------------------------------------------

--> PASSO A PASSO DA LÓGICA:

   A) INPUT (Entrada):
      Enviamos sequências em formato FASTA. O programa analisa todas as strings 
      ao mesmo tempo para encontrar regiões de similaridade.

   B) WIDTH (Largura):
      Definimos o 'minw' (largura mínima) como 20. Isso força o programa a 
      ignorar ruídos curtos e focar em blocos estruturais maiores.

   C) REGULAR EXPRESSION (Saída do Rosalind):
      É a forma resumida de descrever o motivo.
      - Letras únicas (Ex: D, L, W): Significam que aquele aminoácido é 
        unânime naquela posição em todas as sequências.
      - Colchetes (Ex: [NK]): Significam que houve variação. Naquela posição, 
        algumas sequências têm N (Asparagina) e outras têm K (Lisina).

--------------------------------------------------

--> COMO INTERPRETAR O LOGO (O gráfico colorido):
   - A altura da letra indica o quão conservada ela está (bits).
   - Letras grandes = Aminoácidos essenciais que não mudam.
   - Letras empilhadas = Posições onde ocorre mutação ou variabilidade.

--------------------------------------------------

--> APLICAÇÃO NA BIOLOGIA (Ex: TCC / Genética):
   Ao encontrar um motivo [NK], você identifica uma região onde a proteína 
   aceita trocas de aminoácidos sem perder a função, ou uma região de 
   polimorfismo que pode ser estudada.

--------------------------------------------------

--> Exemplo da Expressão Regular encontrada:
# Sample Dataset:
   >Rosalind_7142
PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQ
FYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFE
WGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNM
SYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY

   >Rosalind_4494
VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERY
PIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADF
QRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFL
KTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM

   >Rosalind_3636
ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCF
NKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMA
GNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMM
GHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN

# Sample Output:
motif_regex = "DLWWCWIPVHK[NK]PHSFLKTWSPAAGHRGWQFDHNFF"
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-