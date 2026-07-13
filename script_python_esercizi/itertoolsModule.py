import itertools
colori = ["rosso","blu","verde","giallo"]
abbinamenti = list(itertools.combinations(colori,1))
print(abbinamenti)
abbinamenti_due = list(itertools.permutations(colori,2))
print(abbinamenti_due)
abbinamenti_tre = list(itertools.product(colori,repeat=2))

modelli = ["Llama-3", "GPT-4", "Claude-3", "Gemini"]
abbinamenti_modelli = list(itertools.combinations(modelli,2))
for sfidante1 , sfidante2 in abbinamenti_modelli:
    print(f"Sfidante 1: {sfidante1} VS Sfidante 2: {sfidante2}")

abbinamenti_modelli_tre = list(itertools.combinations(modelli,3))
for sfidante1 , sfidante2 , sfidante3 in abbinamenti_modelli_tre:
    print(f"Sfidante 1: {sfidante1} VS Sfidante 2: {sfidante2} VS Sfidante 3: {sfidante3}")

numeri = [0,1,2,3,4,5,6,7,8,9,]
abbinamento_numeri = list(itertools.permutations(numeri,4))
print(len(abbinamento_numeri))