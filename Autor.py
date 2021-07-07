class Autor:
    def __init__(self, author_id, nome):
        self._author_id = author_id
        self.nome = nome

    def print(self):
        print(f"Id: {self._author_id} | Nome: {self.nome}")