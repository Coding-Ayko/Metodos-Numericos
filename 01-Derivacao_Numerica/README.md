# Tópico 1: Derivação Numérica

## Conceitos Teóricos

A derivada de uma função $f(x)$ em um ponto $x$ representa a taxa de variação instantânea da função nesse ponto. Analiticamente, a derivada de $f(x) = \sin(x)$ é $f'(x) = \cos(x)$.

Quando não podemos calcular a derivada analítica, usamos aproximações numéricas.

### Métodos Implementados

1.  **Diferença Finita Progressiva**: Utiliza o valor da função no ponto atual e em um ponto um pouco à frente. A fórmula tem uma precisão de primeira ordem ($O(h)$).
    $$ f'(x) \approx \frac{f(x+h) - f(x)}{h} $$

2.  **Diferença Finita Central**: Utiliza valores da função simetricamente em torno do ponto de interesse. Geralmente produz um resultado mais preciso, com precisão de segunda ordem ($O(h^2)$).
    $$ f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} $$

Onde $h$ é um valor pequeno, chamado de "passo".

---

## Conteúdo do Script 

O script `main.py` está estruturado da seguinte forma:

1.  **Define a função** a ser analisada: `f(x) = sin(x)`.
2.  **Define a derivada analítica** `f'(x) = cos(x)` para obter o valor exato.
3.  **Implementa as funções** `diferenca_progressiva` e `diferenca_central`.
4.  **Executa os cálculos** para $x=1$ com os passos $h=0.1$ e $h=0.01$.
5.  **Imprime os resultados** de cada método e o erro absoluto associado, comparando-os com o valor analítico.

---

## Resultados Esperados

Ao executar `python main.py`, a saída no terminal será:

```
--------------------------------------------------
Cálculo da Derivada de f(x) = sen(x) em x = 1.0
--------------------------------------------------
Valor Analítico (Exato) cos(1.0) = 0.540302305868

Para h = 0.1:
  - Diferença Progressiva: 0.497363753361 | Erro Absoluto = 4.293855250726e-02
  - Diferença Central    : 0.539402252321 | Erro Absoluto = 9.0005354712e-04

Para h = 0.01:
  - Diferença Progressiva: 0.536086098975 | Erro Absoluto = 4.2162068932e-03
  - Diferença Central    : 0.540293305891 | Erro Absoluto = 9.0000000000e-06

Observação: Note como o erro na diferença central é significativamente menor que na progressiva.
```