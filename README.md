# Métodos Numéricos - Estudos e Implementações

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-green" alt="Status do Projeto: Em Desenvolvimento">
  <img src="https://img.shields.io/github/languages/top/Coding-Ayko/Metodos-Numericos" alt="Linguagem Principal">
  <img src="https://img.shields.io/github/license/Coding-Ayko/Metodos-Numericos" alt="Licença">
  <img src="https://img.shields.io/github/last-commit/Coding-Ayko/Metodos-Numericos" alt="Último Commit">
</p>

---

## Sobre o Projeto

Este repositório serve como um registro dos meus estudos na disciplina de Métodos Numéricos. O objetivo é aplicar os conceitos teóricos em algoritmos práticos, solidificando o aprendizado e construindo um portfólio de projetos acadêmicos.

Cada pasta representa um tópico de estudo, contendo o código-fonte da implementação e um `README.md` com a explicação matemática do método abordado.

---

## Tópicos Abordados

Atualmente, o projeto contém implementações para os seguintes métodos:

* **[01 - Derivação Numérica](./01-Derivacao_Numerica/)**: Métodos para calcular a derivada de uma função em um ponto, utilizando as fórmulas de diferenças finitas (progressiva e central) e análise de erro.

* **[02 - Séries Numéricas](./02-Series_Numericas/)**: Algoritmos para o cálculo de somatórios, com exemplos que se aproximam de constantes matemáticas famosas como π (Problema de Basileia) e o número de Euler.

* **[03 - Integração Numérica](./03-Integracao_Numerica/)**: Introdução ao cálculo de integrais definidas de forma numérica, utilizando o método da soma de retângulos (regra do ponto à esquerda).

---

## Tecnologias Utilizadas

* **Linguagem:** [Python 3](https://www.python.org/)
* **Bibliotecas:**
    * `math` (Funções matemáticas padrão)
    * `numpy` (Para manipulação numérica precisa em alguns scripts)

---

## Como Rodar o Projeto

Para executar os exemplos, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Coding-Ayko/Metodos-Numericos.git](https://github.com/Coding-Ayko/Metodos-Numericos.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Metodos-Numericos
    ```

3.  **Escolha um tópico e execute o script:**
    ```bash
    # Exemplo para o tópico de Derivação Numérica
    cd 01-Derivacao_Numerica
    python main.py
    ```

---

## Próximos Passos

A ideia é continuar adicionando novos métodos numéricos, como:

- [ ] Métodos para encontrar raízes de funções (Bissecção, Newton-Raphson).
- [ ] Interpolação (Polinômios de Lagrange, Newton).
- [ ] Solução de sistemas de equações lineares (Gauss-Seidel).
- [ ] Métodos de integração mais precisos (Regra dos Trapézios, Simpson).

---

