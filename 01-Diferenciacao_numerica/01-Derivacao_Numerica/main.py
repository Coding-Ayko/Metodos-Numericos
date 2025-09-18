import math

# ---------------------------------------------------------------------------
# Enunciado do Problema
# ---------------------------------------------------------------------------
#
# Calcular a derivada da função f(x) = sen(x) no ponto x=1, utilizando:
# 1. O método analítico (valor exato).
# 2. O método numérico de diferença progressiva.
# 3. O método numérico de diferença central.
#
# Os cálculos numéricos devem ser feitos para h = 0.1 e h = 0.01.
# Ao final, calcular o erro absoluto de cada aproximação.
#
# ---------------------------------------------------------------------------

# Definição da função a ser derivada
def f(x):
    """Retorna o seno de x."""
    return math.sin(x)

# Definição da derivada analítica (exata) para fins de comparação
def derivada_analitica(x):
    """Retorna o cosseno de x, que é a derivada de sen(x)."""
    return math.cos(x)

# Implementação dos métodos numéricos

def diferenca_progressiva(f, x, h):
    """
    Calcula a derivada aproximada usando a fórmula da diferença finita progressiva.
    f'(x) ≈ (f(x+h) - f(x)) / h
    """
    return (f(x + h) - f(x)) / h

def diferenca_central(f, x, h):
    """
    Calcula a derivada aproximada usando a fórmula da diferença finita central.
    f'(x) ≈ (f(x+h) - f(x-h)) / (2*h)
    """
    return (f(x + h) - f(x - h)) / (2 * h)


# --- Execução e Análise ---

# Parâmetros
ponto_x = 1.0
passos_h = [0.1, 0.01]

# 1. Cálculo do valor analítico (exato)
valor_exato = derivada_analitica(ponto_x)
print("-" * 50)
print(f"Cálculo da Derivada de f(x) = sen(x) em x = {ponto_x}")
print("-" * 50)
print(f"Valor Analítico (Exato) cos({ponto_x}) = {valor_exato:.12f}\n")

# 2. Cálculo pelos métodos numéricos para cada passo h
for h in passos_h:
    # Diferença Progressiva
    valor_progressivo = diferenca_progressiva(f, ponto_x, h)
    erro_progressivo = abs(valor_progressivo - valor_exato)

    # Diferença Central
    valor_central = diferenca_central(f, ponto_x, h)
    erro_central = abs(valor_central - valor_exato)

    print(f"Para h = {h}:")
    print(f"  - Diferença Progressiva: {valor_progressivo:.12f} | Erro Absoluto = {erro_progressivo:.12e}")
    print(f"  - Diferença Central    : {valor_central:.12f} | Erro Absoluto = {erro_central:.12e}\n")

print("Observação: Note como o erro na diferença central é significativamente menor que na progressiva.")