# Tópico 1: Derivação Numérica

Este script demonstra como calcular a derivada de uma função em um ponto específico utilizando métodos de diferenças finitas.

## Conceitos

A derivada de uma função $f(x)$ em um ponto $x$ representa a taxa de variação instantânea da função nesse ponto. Analiticamente, a derivada de $f(x) = \sin(x)$ é $f'(x) = \cos(x)$.

Quando não podemos calcular a derivada analítica, usamos aproximações numéricas.

### Métodos Implementados

1.  **Diferença Finita Progressiva**: Utiliza o valor da função no ponto atual e em um ponto um pouco à frente.
    $$ f'(x) \approx \frac{f(x+h) - f(x)}{h} $$

2.  **Diferença Finita Central**: Utiliza valores da função simetricamente em torno do ponto de interesse, o que geralmente produz um resultado mais preciso.
    $$ f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} $$

Onde $h$ é um valor pequeno, chamado de "passo".

## Execução

O script `main.py` calcula a derivada de $f(x) = \sin(x)$ em $x=1$ para dois valores de $h$ (0.1 e 0.01) e compara os resultados com o valor analítico exato, calculando também o erro absoluto de cada método.

# Tópico 2: Séries Numéricas (Somatórios)

Este script implementa o cálculo de somatórios finitos que aproximam o valor de séries infinitas conhecidas.

## Conceitos

Um somatório, representado pelo símbolo sigma ($ \sum $), é a adição de uma sequência de termos. Em métodos numéricos, somatórios são usados para aproximar valores de séries, calcular médias, entre outras aplicações.

### Séries Implementadas

1.  **Série de Basileia (Aproximação)**: O cálculo do somatório:
    $$ S_1 = \sum_{n=1}^{100} \frac{1}{n^2} $$
    Esta é uma aproximação finita da famosa série infinita que converge para $ \frac{\pi^2}{6} $.

2.  **Série de Taylor para $e^x$ (Aproximação)**: O cálculo do somatório:
    $$ S_2 = \sum_{n=1}^{100} \frac{1}{n!} $$
    A série infinita $ \sum_{n=0}^{\infty} \frac{1}{n!} $ converge para o número de Euler, $e$. Como nosso somatório começa em $n=1$, ele converge para $e - 1$. O script implementa uma versão otimizada que evita o recálculo completo do fatorial a cada passo.

## Execução

O script `main.py` calcula os dois somatórios até o limite de $N=100$ e compara os resultados com seus respectivos valores teóricos conhecidos.

# Tópico 3: Integração Numérica

Este script introduz o conceito de integração numérica, que consiste em encontrar um valor aproximado para uma integral definida. A integral definida de uma função $f(x)$ em um intervalo $[a, b]$ representa a área sob a curva da função nesse intervalo.

## Conceitos

### Método da Soma de Retângulos (Regra do Ponto à Esquerda)

Este é um dos métodos mais simples para aproximar uma integral. A ideia é dividir a área sob a curva em $n$ retângulos de larguras iguais e somar suas áreas.

1.  **Largura do Retângulo ($h$)**: O intervalo total $[a, b]$ é dividido em $n$ partes iguais. A largura de cada retângulo é:
    $$ h = \frac{b - a}{n} $$

2.  **Altura do Retângulo**: Para a regra do ponto à esquerda, a altura de cada retângulo é determinada pelo valor da função no início do seu subintervalo, ou seja, $f(x_i)$.

3.  **Área Total**: A integral é aproximada pela soma das áreas desses $n$ retângulos.
    $$ \int_{a}^{b} f(x) \,dx \approx \sum_{i=0}^{n-1} h \cdot f(x_i) $$

## Execução

O script `main.py` calcula a integral de $f(x) = 10x^4$ no intervalo $[2, 6]$, usando $n=4$ divisões. Ele também calcula o valor exato da integral (via cálculo analítico) para determinar o erro da aproximação numérica.