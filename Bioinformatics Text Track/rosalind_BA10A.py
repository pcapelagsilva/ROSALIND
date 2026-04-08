string = "ABBBBBBABBAABAABBBBABAABAABAAAAABBABBAAAABAAABBBAB"

emissão = {
    "A": {'A': 0.364, 'B': 0.636},
    "B": {'A': 0.971, 'B': 0.029}
}

prob = 0.5

for i in range(len(string)-1):
    atual = string[i]
    proximo = string[i+1]

    prob *= emissão[atual][proximo]

print(prob)