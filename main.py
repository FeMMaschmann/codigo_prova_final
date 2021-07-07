from Livro import Livro
from Autor import Autor
from Pilha import Pilha

linha = "---------------------------"

autor1 = Autor(1, "Fernando")
autor2 = Autor(2, "Pittacus")
autor3 = Autor(3, "Jay")

autor1.print()
autor2.print()
autor3.print()

print(linha)

book1 = Livro(1, "O caçador", autor1)
book2 = Livro(2, "Unidos somos um", autor2)
book3 = Livro(3, "Nevernight", autor3)

book1.print()
book2.print()
book3.print()

print(linha)

pilha = Pilha()
print(pilha.peek())

print(linha)

pilha.push(book1)
pilha.push(book2)
pilha.push(book3)
print(pilha.peek())

print(linha)

pilha.pop()
print(pilha.peek())
