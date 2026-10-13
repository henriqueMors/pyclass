class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

# Primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0

# Terceiro Jogo
game3 = Game();
game3.name = "Moto 3"
game3.yearLaunch = 2020
game3.multiplayer = True
game3.note = 7.5

# Quarto Jogo
game4 = Game();
game4.name = "GOW"
game4.yearLaunch = 2019
game4.multiplayer = False
game4.note = 9.5

print("###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")
print(f"\nNome do jogo: {game3.name}\nAno de Lançamento: {game3.yearLaunch}")
print(f"\nNome do jogo: {game4.name}\nAno de Lançamento: {game4.yearLaunch}")