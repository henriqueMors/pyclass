from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)
        
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(40)} | {'Nota média'.ljust(40)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(40)} | {str(biblioteca.media_avaliacoes).ljust(40)} {biblioteca.ativo}")
            
    def alterna_estado(self):
        self._ativo = not self._ativo
        
    @property
    def ativo(self):
       return "ativada" if self._ativo else "desativada" 
   
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media
    
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"Itens da Biblioteca {self.nome}\n")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "isbn"):
                msg_livro = f"{i}. {'(Livro)'.ljust(10)} -> Título: {item._titulo.ljust(20)} | Autor: {item._autor.ljust(15)} | Preço: {str(item._preco).ljust(6)} | ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"{i}. {'(Revista)'.ljust(10)} -> Título: {item._titulo.ljust(20)} | Autor: {item._autor.ljust(15)} | Preço: {str(item._preco).ljust(6)} | Edição: {item.edicao}"
                print(msg_revista)