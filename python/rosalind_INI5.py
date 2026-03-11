with open('rosalind_ini5.txt', 'r') as f_entrada:
    with open('resultado_rosalind_INI5.txt', 'w') as f_saida:
        for l, linha in enumerate(f_entrada):
            if l % 2 != 0:
                f_saida.write(linha)

print("Documento 'resposta,txt' gerado com exito")