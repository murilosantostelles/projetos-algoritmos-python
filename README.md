# projetos-algoritmos-python
Projetos em Python para aplicar os conceitos da disciplina de Algoritmos, estudados em 2025/1.

# 🎲 Coleção de Jogos Clássicos em Python

Este repositório contém uma coleção de jogos de texto simples desenvolvidos em Python.

## 📝 Contexto do Projeto

Este projeto foi desenvolvido como parte dos requisitos da disciplina de Algortimos, presente no primeiro período do curso de Engenharia de Software na UniAcademia. O objetivo era aplicar conceitos fundamentais de lógica de programação, estruturas de dados e interação com o usuário para criar jogos funcionais no terminal, evitando o uso de funções prontas.

## ✨ Jogos Incluídos

Atualmente, a coleção inclui os seguintes jogos (em ordem cronológica):

- **Pedra, Papel e Tesoura**
- **Jogo da Forca**
- **Jogo da Velha**

## 🚀 Como Executar e Jogar

Para jogar, você precisa ter o Python 3.11 (ou superior) instalado.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```

3.  **Escolha e execute um dos jogos:**


    * **Para jogar Pedra, Papel e Tesoura:**
        ```bash
        python3 pedra_papel_tesoura/main.py
        ```
        *Instruções:* Jogue contra o computador escolhendo entre pedra, papel ou tesoura e veja quem vence a rodada.

      
    * **Para jogar o Jogo da Forca:**
        ```bash
        python3 jogo_da_forca/main.py
        ```
        *Instruções:* Tente adivinhar a palavra secreta letra por letra. Você tem um número limitado de tentativas antes que o boneco seja enforcado.



    * **Para jogar o Jogo da Velha:**
        ```bash
        python3 jogo_da_velha/main.py
        ```
        *Instruções:* Dois jogadores alternam turnos para marcar 'X' ou 'O' em um tabuleiro 3x3. O primeiro a conseguir uma linha, coluna ou diagonal completa, vence.
         Para escolher a posição da jogada, utiliza-se números de 0 a 2 para representar as linhas, e números também de 0 a 2, para representar as colunas. Então, se desejar jogar
         na posição do meio, por exemplo, devera digitar "1" para a linha e "1" para a coluna!

## 📁 Estrutura do Repositório

O código está organizado em diretórios separados para cada jogo, facilitando a manutenção e a compreensão:

```
.
├── jogo_da_forca/
│   └── main.py
├── jogo_da_velha/
│   └── main.py
└── pedra_papel_tesoura/
    └── main.py
```

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
