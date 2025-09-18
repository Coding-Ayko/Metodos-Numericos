# Tópico 3: Integração Numérica


##  Conceitos Teóricos

### Método da Soma de Retângulos (Regra do Ponto à Esquerda)

Este é um dos métodos mais simples para aproximar uma integral. A ideia é dividir a área sob a curva em $n$ retângulos de larguras iguais e somar suas áreas.

1.  **Largura do Retângulo ($h$)**: O intervalo total $[a, b]$ é dividido em $n$ partes iguais. A largura de cada retângulo é:
    $$ h = \frac{b - a}{n} $$

2.  **Altura do Retângulo**: Para a regra do ponto à esquerda, a altura de cada retângulo é determinada pelo valor da função no início do seu subintervalo, ou seja, $f(x_i)$.

3.  **Área Total**: A integral é aproximada pela soma das áreas desses $n$ retângulos.
    $$ \int_{a}^{b} f(x) \,dx \approx \sum_{i=0}^{n-1} h \cdot f(x_i) $$

---

## Conteúdo do Script `main.py`

O script `main.py` está estruturado da seguinte forma:

1.  **Define a função** a ser integrada: $f(x) = 10x^4$.
2.  **Implementa a função `integral_retangulos_esquerda`**, que recebe a função, os limites de integração (`a`, `b`) e o número de divisões (`n`).
3.  **Executa o cálculo numérico** para o intervalo $[2, 6]$ com $n=4$ subdivisões.
4.  **Calcula o valor analítico exato** da integral para fins de comparação. A integral de $10x^4$ é $2x^5$.
5.  **Imprime o resultado numérico**, o resultado exato e o erro absoluto da aproximação.

---

## Resultados Esperados

Ao executar `python main.py`, a saída no terminal será:

```
------------------------------------------------------------
Cálculo da Integral de f(x) = 10x⁴ de 2.0 a 6.0 com n = 4
------------------------------------------------------------
Resultado Numérico (Soma de Retângulos): 7440.0000
Resultado Analítico (Exato)            : 15488.0000
Erro Absoluto                          : 8048.0000
```

