# Biblioteca Pessoal

Projeto simples de biblioteca pessoal em Python, usando apenas quatro arquivos.

## Arquivos

- `main.py`
  - Menu principal e fluxo de execução.
- `tarefas.py`
  - Todas as funções que implementam as operações do menu.
- `dados.py`
  - Lista de livros e funções de consulta de status.
- `utils.py`
  - Função para limpar a tela do terminal.

## Funcionalidades

O sistema permite:

1. Cadastrar livro
2. Listar livros cadastrados
3. Buscar livro por título ou autor
4. Atualizar status de um livro
5. Mostrar fila de leitura (`Para ler`)
6. Mostrar pilha de livros concluídos (`Concluído`)
7. Filtrar livros por gênero
8. Contar livros por status
9. Remover o primeiro livro da fila e marcar como `Lendo`
10. Remover o último livro do histórico de concluídos e colocá-lo de volta na fila de leitura

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Exemplo de uso

Após iniciar o programa, o menu será exibido:

```text
======= Biblioteca Pessoal =======
      1 - Cadastrar Livro
      2 - Listar Livros
      3 - Buscar Livro
      4 - Atualizar Status
      5 - Mostrar Fila
      6 - Mostrar Pilha
      7 - Filtrar Gênero
      8 - Contar Status
      9 - Remover da fila
      10 - Remover do histórico de Concluídos
      11 - Sair
```

Passos comuns:

1. Escolha `1` para cadastrar um livro.
2. Informe título, autor, ano, gênero e status.
3. Use `2` para listar todos os livros.
4. Use `7` para filtrar por gênero ou `3` para buscar por título/autor.

## Observações

- O projeto usa apenas Python padrão, sem dependências extras.
- Os livros são mantidos em memória durante a execução do programa.
- Fechar o programa faz com que os dados sejam perdidos, pois não há persistência em arquivo.
- Para clicar em `S` ou `N` nas perguntas de confirmação, use apenas essas letras.
