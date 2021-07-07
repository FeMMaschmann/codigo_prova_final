class Livro:
    def __init__(self, book_id, titulo, autor):
        self.book_id = book_id
        self.titulo = titulo
        self.autor = autor
        self.next = None

    def print(self):
        print(f"Id_livro: {self.book_id} | Titulo: {self.titulo} | Id_autor: {self.autor._author_id} | Nome_autor: {self.autor.nome}")
