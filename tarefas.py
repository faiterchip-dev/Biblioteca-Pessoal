from dados import livros, status, fila_leitura, pilha_livro_concluidos

##########################################################################################

# Cadastrar livro

def cadastrar_livro():
    
    titulo = input('Título: ')
    autor = input('Autor: ')
    ano = input('Ano: ')
    genero = input('Gênero: ')
    prioridade = input('Prioridade: ')

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'genero': genero,
        'prioridade': prioridade,
        'status': status[0]
    }

    livros.append(livro)

    fila_leitura.append(livro)

    print(f'Livro cadastrado com sucesso!')
    
def listar_livros():

    if len(livros) == 0:
        print('Nenhum livro cadastrado.')
        return
    
    print('\n======= LISTA DE LIVROS =======')

    for livro in livros:
        print(f'Título: {livro['titulo']}')
        print(f'Autor: {livro['autor']}')
        print(f'Ano: {livro['ano']}')
        print(f'Gênero: {livro['genero']}')
        print(f'Prioridade: {livro['prioridade']}')
        print(f'Status: {livro['status']}')
        print('----------------------------------------')

##########################################################################################

# Buscar Livros

def buscar_livro():

    pesquisa = input('Digite título ou autor do livro: ').lower()

    encontrados = []

    for livro in livros: #

        if (
            pesquisa in livro['titulo'].lower()
            or
            pesquisa in livro['autor'].lower()
        ):
            
            encontrados.append(livro)

    if len(encontrados) == 0:
        print('Livro não encontrado.')

    else:

        print('\n======= RESULTADOS ENCONTRADOS =======')

    for livro in encontrados:
        print(f'{livro['titulo']} - {livro['autor']}')

##########################################################################################

# Atualizar Status

def atualizar_status():

    titulo = input('Digite o título do livro: ').lower()

    for livro in livros:
        
        if livro['titulo'].lower() == titulo:

            if livro['status'] == status[0]:

                livro['status'] = status[1]

                fila_leitura.remove(livro)

                print('Livro atualizado para "Lendo".')
                return
            
            elif livro['status'] == status[1]:

                livro['status'] = status[2]

                pilha_livro_concluidos.append(livro)

                print('Livro atualizado para "Concluído".')
                return
            
            elif livro['status'] == status[2]:

                print('O livro já foi concluído.')
                return
            
    print('Livro não encontrado.')

##########################################################################################

# Mostar FIFO

def mostrar_fila():

    print('\n======= FILA DE LEITURA =======')

    for livro in fila_leitura:

        print(livro['titulo'])

##########################################################################################

# Mostrar LIFO

def mostrar_pilha():

    print('\n======= PILHA DE LIVROS CONCLUÍDOS =======')

    for livro in reversed(pilha_livro_concluidos):

        print(livro['titulo'])

##########################################################################################

# Filtrar livros por gênero (Função bônus)

def filtrar_genero():

    genero = input('Digite o gênero do livro: ')

    encontrados = []

    for livro in livros:

        if livro['genero'].lower() == genero:
            encontrados.append(livro)

        if len(encontrados) == 0:
            print('Nenhum livro encontrado.')

        else:

            for livro in encontrados:
                print(livro['titulo'])

##########################################################################################

# Contar total de livros por status (Função bônus)

def contar_status():

    a_ler = 0
    lendo = 0
    concluido = 0

    for livro in livros:

        if livro['status'] == status[0]:
            a_ler += 1

        elif livro['status'] == status[1]:
            lendo += 1

        elif livro['status'] == status[2]:
            concluido += 1

    print(f'A ler: {a_ler}')
    print(f'Lendo: {lendo}')
    print(f'Concluído: {concluido}')

##########################################################################################

# Removendo livros da fila

def remover_da_fila():

    if len(fila_leitura) == 0:

        print('Fila vazia.')
        return
    
    livro_remover = fila_leitura.pop(0)

    print('Livro removido da fila.')
    print(livro_remover['titulo'])

##########################################################################################

# Removendo livros da pilha

def remover_da_pilha():

    if len(pilha_livro_concluidos) == 0:

        print('Histórico vazio.')
        return
    
    livro_remover = pilha_livro_concluidos.pop()

    print('Livro removido do histórico de concluídos.')
    print(livro_remover['titulo'])

##########################################################################################
