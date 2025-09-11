# ---------------------------------------------------------------------------
# Enunciado do Problema
# ---------------------------------------------------------------------------
#
# 1. Escrever um programa que calcule o seguinte somatório:
#
#    100
#     ∑     1
#    n=1   ---
#          n²
#
# 2. Calcular o somatório da série infinita 1/n! (aproximado até n=100),
#    que converge para o número de Euler 'e'.
#
# ---------------------------------------------------------------------------
import math

def somatorio_basileia(limite):
    """
    Calcula o somatório de 1/n^2 até um 'limite' superior.
    Este é um caso particular do Problema de Basileia, que converge para (pi^2)/6.
    """
    soma = 0.0
    for n in range(1, limite + 1):
        soma += 1 / (n ** 2)
    return soma

def somatorio_euler_otimizado(limite):
    """
    Calcula o somatório de 1/n! até um 'limite' superior.
    Este somatório converge para o número 'e' - 1.
    Otimizado para não recalcular o fatorial a cada iteração.
    """
    soma = 0.0
    fatorial = 1.0  # Começa com 1 para servir de base para o primeiro cálculo
    for n in range(1, limite + 1):
        fatorial *= n  # Atualiza o fatorial para n! (1!, 2!, 3!, ...)
        soma += 1 / fatorial
    return soma

# --- Execução e Análise ---
LIMITE_N = 100

# 1. Cálculo do primeiro somatório
resultado_soma_1 = somatorio_basileia(LIMITE_N)
valor_exato_basileia = (math.pi ** 2) / 6

print("-" * 50)
print(f"Cálculo do Somatório de 1/n² para n de 1 a {LIMITE_N}")
print("-" * 50)
print(f"Resultado do somatório: {resultado_soma_1:.12f}")
print(f"Valor teórico (π²/6)  : {valor_exato_basileia:.12f}")
print(f"Diferença              : {abs(resultado_soma_1 - valor_exato_basileia):.12e}\n")


# 2. Cálculo do segundo somatório
resultado_soma_2 = somatorio_euler_otimizado(LIMITE_N)
valor_exato_euler = math.e - 1 # O somatório começa de n=1, então converge para e-1

print("-" * 50)
print(f"Cálculo do Somatório de 1/n! para n de 1 a {LIMITE_N}")
print("-" * 50)
print(f"Resultado do somatório: {resultado_soma_2:.12f}")
print(f"Valor teórico (e - 1)   : {valor_exato_euler:.12f}")
print(f"Diferença              : {abs(resultado_soma_2 - valor_exato_euler):.12e}")