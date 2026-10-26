import csv

cursos = []

with open("topicos_avancado/Arquivos/dados/cursos.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursos.append({
            "language":row["language"],
            "category":row["category"]
        })
        
print(cursos)