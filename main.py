from tarefas import *   #importa todas as funções do arquivo tarefas.py
from utils import limpar_tela  #importa a função limpar_tela do arquivo utils.py

while True:
    limpar_tela() #limpa tela toda vez que o menu for exibido para manter a interface limpa e organizada

    print('======= Biblioteca Pessoal =======') #exibe o título da biblioteca para o usuário
    print('    1 - Cadastrar Livro')
    print('    2 - Listar Livros')
    print('    3 - Buscar Livro')
    print('    4 - Atualizar Status')
    print('    5 - Mostrar Fila')
    print('    6 - Mostrar Pilha')
    print('    7 - Filtrar Gênero')
    print('    8 - Contar Status')
    print('    9 - Remover da fila')
    print('   10 - Remover do histórico de Concluídos')
    print('   11 - Sair')

    opcao = input('Escolha uma opção da Biblioteca: ') #solicita ao usuário que escolha uma opção do menu e armazena a escolha na variável opcao
    try: #tenta executar o bloco de código abaixo, se ocorrer algum erro durante a execução, ele será capturado e tratado no bloco except
            if opcao == '1':
                CadastroDeLivro() #chama a função CadastroDeLivro() que é responsável por cadastrar um novo livro na biblioteca, permitindo ao usuário inserir informações como título, autor, gênero, etc.

            elif opcao == '2':
                ListarLivros() #chama a função ListarLivros() que  exibe uma lista de todos os livros cadastrados na biblioteca, mostrando detalhes como título, autor, status, etc.

            elif opcao == '3':
                BuscarLivro() #chama a função BuscarLivro() que permite ao usuário pesquisar por um livro específico na biblioteca, utilizando critérios como título, autor ou gênero para encontrar o livro desejado.

            elif opcao == '4':
                AtualizarStatus() #chama a função AtualizarStatus() que permite ao usuário atualizar o status de um livro na biblioteca.

            elif opcao == '5':
                MostrarFila() #chama a função MostrarFila() que exibe os livros que estão na fila de espera, ou seja, os livros que o usuário deseja ler em seguida.

            elif opcao == '6':
                MostrarPilha() #chama a função MostrarPilha() que exibe os livros que estão na pilha de leitura, ou seja, os livros que o usuário pretende ler em breve. A pilha de leitura é uma estrutura de dados onde os livros são organizados em ordem de prioridade, permitindo ao usuário visualizar quais livros estão próximos de serem lidos.

            elif opcao == '7':
                FiltrarGenero()

            elif opcao == '8':
                ContarStatus() #chama a função ContarStatus() que conta e exibe o número de livros em cada status (lidos, lendo, para ler) na biblioteca, fornecendo ao usuário uma visão geral do progresso de leitura e ajudando a organizar melhor a coleção de livros.

            elif opcao == '9':
                RemoverDaFila() #chama a função RemoverDaFila() que permite ao usuário remover um livro da fila de espera.

            elif opcao == '10':
                RemoverDoHistorico() #chama a função RemoverDoHistorico() que permite ao usuário remover um livro do histórico de livros concluídos.

            elif opcao == '11':
                print('Obrigado por acessar a biblioteca! O sistema será encerrado.')
                break

            else:
                print('Opção Inválida. Por favor digite números de 1 a 11.')

            input('\nPressione ENTER para continuar.')
    except Exception as erro: #captura qualquer erro que possa ocorrer durante a execução do programa guarda na variavel erro e exibe uma mensagem de erro para o usuário
        print(f'Ocorreu um erro: {erro}')
        print("provalvelmente foi erro de sistema reinicie o sistema e tente novamente.")
        input('\nPressione ENTER para continuar.')
        break