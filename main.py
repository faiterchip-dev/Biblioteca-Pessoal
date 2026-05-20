from tarefas import *   #importa todas as funções do arquivo tarefas.py
from utils import limpar_tela  #importa a função limpar_tela do arquivo utils.py

while True:
    limpar_tela()

    print('======= Biblioteca Pessoal =======')
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

    opcao = input('Escolha uma opção da Biblioteca: ')
    try:
            if opcao == '1':
                CadastroDeLivro()

            elif opcao == '2':
                ListarLivros()

            elif opcao == '3':
                BuscarLivro()

            elif opcao == '4':
                AtualizarStatus()

            elif opcao == '5':
                MostrarFila()

            elif opcao == '6':
                MostrarPilha()

            elif opcao == '7':
                FiltrarGenero()

            elif opcao == '8':
                ContarStatus()

            elif opcao == '9':
                RemoverDaFila()

            elif opcao == '10':
                RemoverDoHistorico()

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