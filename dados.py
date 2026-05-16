# criar lista
livros = []

# Pedir dados
def continuar():
    livro_titulo = input('Digite o nome do seu novo livro: ')
    livro_autor = input('Digite o nome do autor do seu novo livro: ')
    
    try:
        livro_ano = int(input('Digite o ano que foi lançado o livro: '))
    except ValueError:
        print('Por favor digite o ano de lançamento apenas em números.')
        return

    livro_genero = input('Digite o gênero do livro: ')

    livro = {
        "Título": livro_titulo,
        "Autor": livro_autor,
        "Ano de publicação": livro_ano,
        "Gênero": livro_genero
    }

    # Salva o livro na lista
    livros.append(livro)

    print("\n===== Livro Adicionado =====")
    print(f"Título: {livro_titulo}")
    print(f"Autor: {livro_autor}")
    print(f"Ano de publicação: {livro_ano}")
    print(f"Gênero: {livro_genero}")

    # Adicionar mais livros
while True:
    adicionar = input('\nVocê quer adicionar mais algum livro? (S/N) ').upper()

    if adicionar == 'N':
        print('\nAproveite seus novos livros')
        break

    elif adicionar == 'S':
        continuar()

    else:
        print('Por favor digite apenas S ou N')


# Mostrar todos os livros salvos
print("\n===== TODOS OS LIVROS =====")

for livro in livros:
    print("\n----------------")
    
    for chave, valor in livro.items():
        print(f"{chave}: {valor}")
