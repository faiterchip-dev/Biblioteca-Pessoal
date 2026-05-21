from dados import lista_de_livros_cadastrados, status_opcoes, obter_fila, obter_pilha # Importa alguns arquivos da pasta dados

try:
    def CadastroDeLivro():
        livro = solicitar_dados_livro() 
        lista_de_livros_cadastrados.append(livro) # Põe o livro na lista de livros cadastrados
        print('\nLivro cadastrado com sucesso!')
        mostrar_livro(livro)

        resposta = input('Deseja cadastrar outro livro? (S/N): ')
        if resposta == 'S':
            CadastroDeLivro()


    def solicitar_dados_livro():
        titulo = input('Digite o nome do seu novo livro: ')
        autor = input('Digite o nome do autor do seu novo livro: ')

        while True:
            ano_texto = input('Digite o ano que foi lançado o livro: ')
            if ano_texto.isdigit(): # se caso for numero
                ano = int(ano_texto)
                break
            print('Por favor digite o ano de lançamento apenas em números.')

        genero = input('Digite o gênero do livro: ')
        status = escolher_status()

        return { # Retorna à seleção de opções
            'Título': titulo,
            'Autor': autor,
            'Ano de publicação': ano,
            'Gênero': genero,
            'Status': status
        }


    def escolher_status():
        print('\nSelecione o status do livro:')
        for indice, status in enumerate(status_opcoes, start=1): 
            print(f'  {indice} - {status}') # printa "Para ler", "Lendo" e "Concluído"

        escolha = input('Escolha uma opção de status (padrão 1): ')
        if escolha == '':
            return status_opcoes[0] # Retorna para status de opções inicial

        if escolha.isdigit():
            indice = int(escolha)
            if 1 <= indice <= len(status_opcoes): # se 1 for menor ou igual à indice
                return status_opcoes[indice - 1] # Retorna em opção "Para ler"

        print('Status inválido. Usando "Para ler" como padrão.')
        return status_opcoes[0]


    def ListarLivros():
        if len(lista_de_livros_cadastrados) == 0:
            print('\nNenhum livro cadastrado ainda.')
            return

        print('\nLivros cadastrados:')
        for indice, livro in enumerate(lista_de_livros_cadastrados, start=1): # se houver algum livro cadastrado
            print(f'\n{indice} - {livro.get("Título")} ({livro.get("Status")})') # printa Índice, Título e Status
            mostrar_livro(livro)


    def BuscarLivro():
        termo = input('Digite o título ou autor que quer buscar: ').lower()
        if termo == '':
            print('Busca vazia. Digite um título ou autor.')
            return 

        encontrados = [livro for livro in lista_de_livros_cadastrados
                        if termo in livro.get('Título', '').lower()
                        or termo in livro.get('Autor', '').lower()]

        if len(encontrados) == 0:
            print('Nenhum livro encontrado para essa busca.')
            return

        print(f'\nForam encontrados {len(encontrados)} livro(s):')
        for livro in encontrados:
            mostrar_livro(livro)


    def AtualizarStatus():
        if len(lista_de_livros_cadastrados) == 0:
            print('Ainda não há livros para atualizar.')
            return

        ListarLivros()
        escolha = input('Digite o número do livro que deseja atualizar: ')
        if escolha.isdigit() == False:
            print('Entrada inválida. Use apenas números.')
            return

        indice = int(escolha) - 1
        if indice < 0 or indice >= len(lista_de_livros_cadastrados):
            print('Número de livro inválido.')
            return

        livro = lista_de_livros_cadastrados[indice]
        print(f'Livro selecionado: {livro.get("Título")} - Status atual: {livro.get("Status")}')
        novo_status = escolher_status()
        livro['Status'] = novo_status
        print('Status atualizado com sucesso!')
        mostrar_livro(livro)


    def MostrarFila():
        fila = obter_fila()
        if len(fila) == 0:
            print('A fila de leitura está vazia.')
            return

        print('\nFila de leitura:')
        for indice, livro in enumerate(fila, start=1):
            print(f'\n{indice} - {livro.get("Título")}')
            mostrar_livro(livro)


    def MostrarPilha():
        pilha = obter_pilha()
        if len(pilha) == 0:
            print('Não há livros concluídos no histórico.')
            return

        print('\nPilha de livros concluídos (último a entrar é o primeiro a sair):')
        for indice, livro in enumerate(reversed(pilha), start=1):
            print(f'\n{indice} - {livro.get("Título")}')
            mostrar_livro(livro)


    def FiltrarGenero():
        genero = input('Digite o gênero que deseja filtrar: ').lower()
        if genero == '':
            print('Gênero inválido. Digite um gênero válido.')
            return

        encontrados = [livro for livro in lista_de_livros_cadastrados
                        if genero in livro.get('Gênero', '').lower()]

        if len(encontrados) == 0:
            print('Nenhum livro encontrado para esse gênero.')
            return

        print(f'\nForam encontrados {len(encontrados)} livro(s) no gênero "{genero}":')
        for livro in encontrados:
            mostrar_livro(livro)


    def ContarStatus():
        if len(lista_de_livros_cadastrados) == 0:
            print('Nenhum livro cadastrado ainda.')
            return

        contagem = {status: 0 for status in status_opcoes}
        for livro in lista_de_livros_cadastrados:
            contagem[livro.get('Status', 'Para ler')] = contagem.get(livro.get('Status', 'Para ler'), 0) + 1

        print('\nContagem por status:')
        for status, quantidade in contagem.items():
            print(f'  {status}: {quantidade}')


    def RemoverDaFila():
        fila = obter_fila()
        if len(fila) == 0:
            print('A fila de leitura está vazia.')
            return

        livro = fila[0]
        print('O primeiro livro da fila é:')
        mostrar_livro(livro)

        resposta = input('Deseja remover este livro da fila e marcar como Lendo? (S/N): ')
        if resposta == 'S':
            livro['Status'] = 'Lendo'
            print('Livro removido da fila e marcado como Lendo.')
        else:
            print('Ação cancelada.')


    def RemoverDoHistorico():
        pilha = obter_pilha()
        if len(pilha) == 0:
            print('Não há livros concluídos no histórico.')
            return

        livro = pilha[-1]
        print('O último livro concluído é:')
        mostrar_livro(livro)

        resposta = input('Deseja remover este livro do histórico de concluídos e colocá-lo de volta na fila? (S/N): ')
        if resposta == 'S':
            livro['Status'] = 'Para ler'
            print('Livro removido do histórico de concluídos e colocado na fila de leitura.')
        else:
            print('Ação cancelada.')


    def mostrar_livro(livro):
        for chave, valor in livro.items():
            print(f'  {chave}: {valor}')


    def perguntar_sim_ou_nao(pergunta):
        resposta = input(pergunta)
        return resposta == 'S'

except Exception as error:
    print(f'Ocorreu um erro ao carregar as funções: {error}')
    print('Por favor, reinicie o sistema e tente novamente.')  
