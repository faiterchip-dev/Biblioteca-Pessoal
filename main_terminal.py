from tarefas import *

from utils import limpar_tela

while True:

    limpar_tela()

    print('======= Biblioteca Pessoal =======')
    print('1 - Cadastrar Livro')
    print('2 - Listar Livros')
    print('3 - Buscar Livro')
    print('4 - Atualizar Status')
    print('5 - Mostrar Fila')
    print('6 - Mostrar Pilha')
    print('7 - Filtrar Gênero')
    print('8 - Contar Status')
    print("9 - Remover da fila")
    print("10 - Remover do histórico de Concluídos")
    print("11 - Sair")

    opcao = input('Escolha uma opção da Biblioteca: ')

    if opcao == '1':
        cadastrar_livro()

    elif opcao == '2':
        listar_livros()

    elif opcao == '3':
        buscar_livro()

    elif opcao == '4':
        atualizar_status()

    elif opcao == '5':
        mostrar_fila()

    elif opcao == '6':
        mostrar_pilha()

    elif opcao == '7':
        filtrar_genero()

    elif opcao == '8':
        contar_status()
     
    elif opcao == '9':
        remover_da_fila()

    elif opcao == '10':
        remover_da_pilha()

    elif opcao == '11':
        print('Obrigado por acessar a biblioteca! O sistema será encerrado.')

    else:

        print('Opção Inválida. Por favor digite os números de 1 à 11.')
    
    input('\n Pressione ENTER para continuar.')
