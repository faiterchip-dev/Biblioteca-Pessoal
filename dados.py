livro_titulo = input('digite o nome do seu novo livro ')
livro_autor = input('digite o nome do autor do seu novo livro ')
livro_ano = int(input('digite o ano que foi lançado o livro '))
livro_genero = input('digite o gênero do livro ')



Livro = {
    "Título": livro_titulo,
    "Autor": livro_autor,
    "Ano de publicação": livro_ano,
    "Gênero": livro_genero
}

print("\n===== Livro =====")

for chave, valor in Livro.items():
    print(f"{chave}: {valor}")
