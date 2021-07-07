from Livro import Livro

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        book = elem
        book.next = self.top
        self.top = book
        self._size = self._size + 1

    def pop(self):
        if self._size > 0:
            book = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return book.book_id
        raise IndexError("A pilha está vazia")

    def peek(self):
        if (self.top == None):
            return "A pilha está vazia!"
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(f"{pointer.book_id} -> {pointer.titulo}") + "\n"
            pointer = pointer.next
        return r