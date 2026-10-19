import glob, os, zipfile

#1- Diretório de trabalho atual
print(os.getcwd())

#2-Listar todos os arquivos txt
for file in glob.glob("dados/*.txt"):
    print(file)
    
#3-Listar todos os arquivos csv
for file in glob.glob("dados/*.csv"):
    print(file)
    
#4-Compactar arquivos .txt
with zipfile.ZipFile("dados/names.zip", "w") as zip:
    for file in glob.glob("dados/*.txt"):
        zip.write(file)
        
#5-Compactar todos os arquivos
with zipfile.ZipFile("dados/code.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)