# Tópico 2: Séries Numéricas (Somatórios)

## Conceitos Teóricos

Um somatório, representado pelo símbolo sigma ($ \sum $), é a adição de uma sequência de termos. Em métodos numéricos, somatórios são usados para aproximar valores de séries, calcular médias, entre outras aplicações.

### Séries Implementadas

1.  **Série de Basileia (Aproximação)**: O cálculo do somatório:
    $$ S_1 = \sum_{n=1}^{100} \frac{1}{n^2} $$
    Esta é uma aproximação finita da famosa série infinita resolvida por Euler, que converge para $ \frac{\pi^2}{6} $.

2.  **Série de Taylor para $e^x$ em x=1 (Aproximação)**: O cálculo do somatório:
    $$ S_2 = \sum_{n=1}^{100} \frac{1}{n!} $$
    A série infinita $ \sum_{n=0}^{\infty} \frac{1}{n!} $ converge para o número de Euler, $e$. Como nosso somatório começa em $n=1$ (excluindo o termo $1/0! = 1$), ele converge para $e - 1$.

---

##  Conteúdo do Script `main.py`

O script `main.py` está estruturado da seguinte forma:

1.  **Define a função `somatorio_basileia`** para calcular o somatório de $1/n^2$.
2.  **Define a função `somatorio_euler_otimizado`**, que calcula o somatório de $1/n!$ de forma eficiente, sem recalcular o fatorial a cada iteração.
3.  **Executa os cálculos** para ambas as séries com um limite de $N=100$.
4.  **Imprime os resultados** e os compara com os valores teóricos conhecidos (`(pi^2)/6` e `e - 1`), mostrando a diferença.

---

## Resultados Esperados

Ao executar `python main.py`, a saída no terminal será:

```
--------------------------------------------------
Cálculo do Somatório de 1/n² para n de 1 a 100
--------------------------------------------------
Resultado do somatório: 1.634983900185
Valor teórico (π²/6)  : 1.644934066848
Diferença              : 9.9501666632e-03

--------------------------------------------------
Cálculo do Somatório de 1/n! para n de 1 a 100
--------------------------------------------------
Resultado do somatório: 1.718281828459
Valor teórico (e - 1)   : 1.718281828459
Diferença              : 0.000000000000e+00
```
