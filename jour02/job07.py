chaine = "abcdefghijklmnopqrstuvwxyz" * 10

n = 40
for i in range(1, n + 1):
    motif = chaine[:2*i - 2]
    print(motif)
