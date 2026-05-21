# Biblioteca Pessoal

Projeto simples de biblioteca pessoal desenvolvido em Python utilizando programação modular e conceitos básicos de estruturas de dados.

O sistema funciona diretamente pelo terminal e permite organizar livros por status de leitura, gênero e histórico.

---

# Objetivo do Projeto

O objetivo deste projeto é aplicar conceitos aprendidos em sala de aula utilizando Python, incluindo:

- Modularização
- Funções
- Estruturas condicionais
- Estruturas de repetição
- Listas e dicionários
- Tratamento de exceções
- Estruturas de dados (Fila e Pilha)

---

# Estrutura do Projeto

O projeto foi dividido em quatro arquivos principais:

## Arquivos

### `main.py`
Responsável pelo:
- Menu principal
- Fluxo do programa
- Controle das opções escolhidas pelo usuário

---

### `tarefas.py`
Contém:
- Todas as funcionalidades do sistema
- Cadastro
- Busca
- Atualização
- Filtros
- Manipulação da fila e pilha

---

### `dados.py`
Responsável por:
- Armazenar os livros cadastrados
- Gerenciar os status dos livros
- Funções auxiliares de consulta

---

### `utils.py`
Arquivo utilitário contendo:
- Função de limpeza de tela do terminal

---

# Funcionalidades

O sistema permite:

## Gerenciamento de Livros
1. Cadastrar livro
2. Listar livros cadastrados
3. Buscar livro por título ou autor
4. Atualizar status de um livro

---

## Organização de Leitura
5. Mostrar fila de leitura (`Para ler`)
6. Mostrar pilha de livros concluídos (`Concluído`)

---

## Filtros e Estatísticas
7. Filtrar livros por gênero
8. Contar livros por status

---

## Manipulação da Fila e Pilha
9. Remover o primeiro livro da fila e marcar como `Lendo`
10. Remover o último livro do histórico de concluídos e colocá-lo novamente na fila de leitura

---

# Estruturas de Dados Utilizadas

## Fila (FIFO)

Os livros marcados como "Para ler" funcionam como uma fila.

Conceito:
- Primeiro livro adicionado
- Primeiro livro a ser lido

FIFO:
```text
First In, First Out
```

---

## Pilha (LIFO)

Os livros marcados como "Concluído" funcionam como uma pilha.

Conceito:
- Último livro concluído
- Primeiro livro exibido

LIFO:
```text
Last In, First Out
```

---

# Tratamento de Erros

O sistema utiliza `try/except` para evitar falhas durante a execução.

Exemplos:
- Entrada inválida
- Letras no lugar de números
- Erros inesperados do sistema

Exemplo utilizado no projeto:

```python
try:
    opcao = input("Digite uma opção: ")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
```

---

# Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

---

# Exemplo de Uso

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

---

# Fluxo Básico de Utilização

1. Escolha `1` para cadastrar um livro
2. Informe:
   - Título
   - Autor
   - Ano
   - Gênero
   - Status
3. Utilize `2` para visualizar os livros
4. Utilize `3` para buscar livros
5. Utilize `4` para atualizar o status
6. Utilize `5` e `6` para visualizar fila e pilha

---

# Tecnologias Utilizadas

- Python 3
- VS Code
- Terminal/Console

---

# Requisitos

Para executar o projeto é necessário:

- Python 3 instalado
- Terminal ou Prompt de Comando

---

# Observações

- O projeto utiliza apenas Python padrão
- Não existem dependências externas
- Os livros são armazenados apenas em memória
- Ao fechar o programa os dados são perdidos
- O sistema foi desenvolvido para fins acadêmicos

---

# Melhorias Futuras

Possíveis melhorias para versões futuras:

- Salvamento em arquivo `.json`
- Interface gráfica
- Banco de dados
- Sistema de login
- Ordenação de livros
- Favoritos
- Avaliação de livros

---

# Integrantes

- ______________________
- ______________________
- ______________________

---

# Professor(a)

______________________

---

# Instituição

______________________

---

# Ano

2026

---

# Licença

Projeto desenvolvido exclusivamente para fins educacionais e acadêmicos.
