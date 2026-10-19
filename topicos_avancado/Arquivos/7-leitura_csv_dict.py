cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}
        curso["language"] = linguagem
        curso["category"] = categoria
        cursos.append(curso)

print(cursos)     
   
for curso in cursos:
    print(f"{curso['language']}-{curso['category']}")