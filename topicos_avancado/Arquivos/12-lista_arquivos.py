import glob, os, zipfile

#1- Diretório de trabalho atual
print(os.getcwd())

#2-Listar todos os arquivos txt
for file in glob.glob("topicos_avancado/Arquivos/dados/*.txt"):
    print(file)
    
#3-Listar todos os arquivos csv
for file in glob.glob("topicos_avancado/Arquivos/dados/*.csv"):
    print(file)
    
#4-Compactar arquivos .txt
with zipfile.ZipFile("topicos_avancado/Arquivos/dados/names.zip", "w") as zip:
    for file in glob.glob("topicos_avancado/Arquivos/dados/*.txt"):
        zip.write(file)
        
#5-Compactar todos os arquivos
with zipfile.ZipFile("topicos_avancado/Arquivos/dados/code.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)