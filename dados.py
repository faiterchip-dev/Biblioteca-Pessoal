lista_de_livros_cadastrados = []  #Lista global para armazenar os livros cadastrados
status_opcoes = ['Para ler', 'Lendo', 'Concluído'] #Opções de status para os livros, usadas para validação e contagem

try:
    def obter_livros_por_status(status):  #Função para obter livros filtrados por status
        return [livro for livro in lista_de_livros_cadastrados if livro['Status'] == status]


    def obter_fila():
        return obter_livros_por_status('Para ler')


    def obter_pilha():
        return obter_livros_por_status('Concluído')
except Exception as error:
    print(f'Ocorreu um erro ao acessar os dados: {error}')

