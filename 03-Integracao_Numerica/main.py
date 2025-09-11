# ---------------------------------------------------------------------------
# Enunciado do Problema
# ---------------------------------------------------------------------------
#
# Calcular a integral definida da função f(x) = 10 * x^4 no intervalo [2, 6].
# Utilizar o método da soma de retângulos (regra do ponto à esquerda)
# com 4 subdivisões.
#
# ---------------------------------------------------------------------------
import numpy as np

# Definição da função a ser integrada
def f(x):
    """Retorna o valor da função 10 * x^4."""
    return 10 * x**4

def integral_retangulos_esquerda(f, a, b, n):
    """
    Calcula a integral definida de f(x) de 'a' até 'b' usando 'n' retângulos.
    A altura de cada retângulo é determinada pelo valor da função no início do intervalo (ponto à esquerda).

    Args:
        f (function): A função a ser integrada.
        a (float): O limite inferior de integração.
        b (float): O limite superior de integração.
        n (int): O número de subdivisões (retângulos).

    Returns:
        float: O valor aproximado da integral.
    """
    h = (b - a) / n      # Largura de cada subintervalo
    soma_areas = 0.0     # Inicializa o valor acumulado da área

    # Itera sobre cada subintervalo
    # np.arange é usado para garantir a precisão com pontos flutuantes
    for x in np.arange(a, b, h):
        altura = f(x)      # Altura do retângulo é f(x) no ponto inicial
        area = h * altura  # Área do retângulo
        soma_areas += area # Acumula a área

    return soma_areas

# --- Execução e Análise ---

# Parâmetros do problema
limite_inferior = 2.0
limite_superior = 6.0
num_divisoes = 4

# 1. Cálculo da integral numérica
resultado_numerico = integral_retangulos_esquerda(f, limite_inferior, limite_superior, num_divisoes)

# 2. Cálculo da integral analítica (exata) para comparação
# A integral de 10x^4 é 2x^5.
# Avaliada de 2 a 6: (2 * 6^5) - (2 * 2^5) = 15552 - 64 = 15488
valor_exato = 2 * (limite_superior**5) - 2 * (limite_inferior**5)

# 3. Cálculo do erro
erro_absoluto = abs(resultado_numerico - valor_exato)

print("-" * 60)
print(f"Cálculo da Integral de f(x) = 10x⁴ de {limite_inferior} a {limite_superior} com n = {num_divisoes}")
print("-" * 60)
print(f"Resultado Numérico (Soma de Retângulos): {resultado_numerico:.4f}")
print(f"Resultado Analítico (Exato)            : {valor_exato:.4f}")
print(f"Erro Absoluto                          : {erro_absoluto:.4f}")