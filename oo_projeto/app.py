from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("BIblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
livro2 = Livro("Brave New WOrld", "Aldous Huxley", 25.0, "084-3245321")
revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")

livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)

# biblioteca_cidade.alterna_estado()
# biblioteca_cidade.receber_avaliacao('Fulano', 8.5)
# biblioteca_cidade.receber_avaliacao('Sicrano', 9.5)
# biblioteca_cidade.receber_avaliacao('Sicrano', 6.5)

def main():
    # Biblioteca.listar_bibliotecas()
    biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()