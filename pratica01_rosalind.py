s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

def d(s, t):
    posiçao = 0
    for base_s, base_t in zip(s, t):
        if base_s != base_t:
            posiçao += 1
    return posiçao
print(d(s, t))