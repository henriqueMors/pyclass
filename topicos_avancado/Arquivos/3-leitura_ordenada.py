import unicodedata


def chave_alfabetica(texto):
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.casefold()

names = []

with open("topicos_avancado/Arquivos/dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, key=chave_alfabetica):
    print(f"Olá, {name}")