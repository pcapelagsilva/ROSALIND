a = 4998
b = 9846
soma = 0

for n in range(a, b+1):
    if n % 2 != 0:
        soma = soma + n

print(soma)
