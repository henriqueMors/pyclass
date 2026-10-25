numeros = [5, 12, 3, 18, 7, 20]

maiores = [n for n in numeros if n > 10]   # 1. separa os maiores que 10

if maiores:                                 # 2. depois, decide uma vez só
    for n in maiores:
        print(n)
else:
    print("Não tem número maior que 10")