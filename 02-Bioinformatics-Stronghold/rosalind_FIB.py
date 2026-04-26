'''Fn = Fn-1 + (fn-2 * k) - Equação de Fibonacci'''
meses = 31
filhotes = 4
populacao = [1,1]

for i in range(2, meses):
    total_hoje = populacao[i-1] + (populacao[i-2]*filhotes)
    populacao.append(total_hoje)

print(populacao[-1])

            # OUTRA FORMA DE RESOLUÇÃO #
'''
def fib(n, k): # Definição de parâmetros | n = meses; k = filhotes

    população = [1,1] # Criação da base (mês 1 e mês 2 sempre começam com 1 casal)

    for i in range(2, n): # O Loop começa no mês 3 (índice 2 - dois casais) até um mês indeterminado
    
    total_hoje = população[i-1] + (população[i-2] * k) # Aplicação da Equação de Fibonacci - casais antigos + (casais novos * filhotes)

    população.append(total_hoje) # Guarda o valor calculado na lista

    return(população[-1]) # "Devolve" o último valor da lista (O [-1] indica o programa a mostrar apenas o último valor)

resultado = resolver_fib(n, k) # Faz todo o cálculo do código acima automáticamente

print(resultado)
'''
