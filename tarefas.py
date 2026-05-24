from dados import lista_de_livros_cadastrados, status_opcoes, obter_fila, obter_pilha # Importa alguns arquivos da pasta dados

try:
    def CadastroDeLivro(): # Função para cadastrar um novo livro na biblioteca, permitindo ao usuário inserir informações como título, autor, gênero, etc.
        livro = solicitar_dados_livro() 
        lista_de_livros_cadastrados.append(livro) # Põe o livro na lista de livros cadastrados
        print('\nLivro cadastrado com sucesso!')
        mostrar_livro(livro)

        resposta = input('Deseja cadastrar outro livro? (S/N): ')
        if resposta == 'S':
            CadastroDeLivro()


    def solicitar_dados_livro(): # Função para solicitar os dados do livro ao usuário, como título, autor, ano de publicação, gênero e status.
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


    def escolher_status(): # Função para escolher o status do livro, apresentando as opções "Para ler", "Lendo" e "Concluído" para o usuário selecionar. O status escolhido é retornado para ser associado ao livro cadastrado.
        print('\nSelecione o status do livro:')
        for indice, status in enumerate(status_opcoes, start=1): 
            print(f'  {indice} - {status}') # printa "Para ler", "Lendo" e "Concluído"

        escolha = input('Escolha uma opção de status (padrão 1): ')
        if escolha == '':
            return status_opcoes[0] # Retorna para status de opções inicial

        if escolha.isdigit(): # se caso for numero
            indice = int(escolha)
            if 1 <= indice <= len(status_opcoes): # se 1 for menor ou igual à indice
                return status_opcoes[indice - 1] # Retorna em opção "Para ler"

        print('Status inválido. Usando "Para ler" como padrão.')
        return status_opcoes[0]


    def ListarLivros(): # Função para listar todos os livros cadastrados na biblioteca, mostrando detalhes como título, autor, status, etc. Se não houver livros cadastrados, exibe uma mensagem informando que a biblioteca está vazia.
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

        encontrados = [livro for livro in lista_de_livros_cadastrados # se o termo for encontrado no título ou autor do livro, ele é adicionado à lista de encontrados
                        if termo in livro.get('Título', '').lower()
                        or termo in livro.get('Autor', '').lower()]

        if len(encontrados) == 0:
            print('Nenhum livro encontrado para essa busca.')
            return

        print(f'\nForam encontrados {len(encontrados)} livro(s):')
        for livro in encontrados:
            mostrar_livro(livro)


    def AtualizarStatus(): # Função para atualizar o status de um livro na biblioteca. O usuário pode escolher um livro específico e alterar seu status para "Para ler", "Lendo" ou "Concluído". Se não houver livros cadastrados, exibe uma mensagem informando que não há livros para atualizar.
        if len(lista_de_livros_cadastrados) == 0:
            print('Ainda não há livros para atualizar.')
            return

        ListarLivros() # Chama a função ListarLivros() para exibir a lista de livros cadastrados, permitindo ao usuário visualizar os livros disponíveis antes de escolher qual status deseja atualizar.
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


    def MostrarFila(): # Função para mostrar os livros que estão na fila de espera, ou seja, os livros que o usuário deseja ler em seguida.
        fila = obter_fila()
        if len(fila) == 0:
            print('A fila de leitura está vazia.')
            return

        print('\nFila de leitura:')
        for indice, livro in enumerate(fila, start=1):
            print(f'\n{indice} - {livro.get("Título")}')
            mostrar_livro(livro)


    def MostrarPilha(): # Função para mostrar os livros que estão na pilha de leitura, ou seja, os livros que o usuário pretende ler em breve.
        pilha = obter_pilha()
        if len(pilha) == 0:
            print('Não há livros concluídos no histórico.')
            return

        print('\nPilha de livros concluídos (último a entrar é o primeiro a sair):')
        for indice, livro in enumerate(reversed(pilha), start=1):
            print(f'\n{indice} - {livro.get("Título")}')
            mostrar_livro(livro)


    def FiltrarGenero(): # Função para filtrar os livros por gênero, permitindo ao usuário digitar um gênero específico e exibindo os livros que correspondem a esse gênero. Se não houver livros cadastrados ou se nenhum livro corresponder ao gênero digitado, exibe uma mensagem informando o resultado da busca.
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


    def ContarStatus(): # Função para contar e exibir o número de livros em cada status (lidos, lendo, para ler) na biblioteca, fornecendo ao usuário uma visão geral do progresso de leitura e ajudando a organizar melhor a coleção de livros. Se não houver livros cadastrados, exibe uma mensagem informando que a biblioteca está vazia.
        if len(lista_de_livros_cadastrados) == 0:
            print('Nenhum livro cadastrado ainda.')
            return

        contagem = {status: 0 for status in status_opcoes}
        for livro in lista_de_livros_cadastrados:
            contagem[livro.get('Status', 'Para ler')] = contagem.get(livro.get('Status', 'Para ler'), 0) + 1

        print('\nContagem por status:')
        for status, quantidade in contagem.items():
            print(f'  {status}: {quantidade}')


    def RemoverDaFila(): # Função para remover um livro da fila de espera. O usuário pode escolher o primeiro livro da fila e optar por removê-lo, marcando-o como "Lendo". Se a fila estiver vazia, exibe uma mensagem informando que não há livros para remover.
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


    def RemoverDoHistorico(): # Função para remover um livro do histórico de livros concluídos. O usuário pode escolher o último livro da pilha de leitura e optar por removê-lo, marcando-o como "Para ler". Se a pilha estiver vazia, exibe uma mensagem informando que não há livros para remover.
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


    def mostrar_livro(livro): # Função para exibir os detalhes de um livro, mostrando todas as informações associadas a ele, como título, autor, ano de publicação, gênero e status. Essa função é utilizada em várias partes do programa para apresentar os detalhes dos livros de forma clara e organizada.
        for chave, valor in livro.items():
            print(f'  {chave}: {valor}')


    def perguntar_sim_ou_nao(pergunta): # Função para fazer uma pergunta ao usuário e obter uma resposta "S" ou "N". A função exibe a pergunta e espera a resposta do usuário, retornando True se a resposta for "S" e False se for "N". Essa função é útil para confirmar ações ou decisões do usuário de forma simples e direta.
        resposta = input(pergunta)
        return resposta == 'S'

except Exception as error: #se caso algo der errado
    print(f'Ocorreu um erro ao carregar as funções: {error}')
    print('Por favor, reinicie o sistema e tente novamente.')  
