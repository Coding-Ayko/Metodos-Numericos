#Enunciado

#Escreva um programa que encontre a raiz da função f(x)= sen(x) - ln(x)
#ultilizando o método da bissecção a partir do intervalo [1;5]. 
# Ultilize |f(m)| < 0.001 como condição de parada

#explicação
#O método da bissecção, ele repetidamente "corta o intervalo ao meio" para cercar a raiz da função.

#inicio da logica 
#
import math

def define_funcao(x):
  """Retorna o valor de sen(x) - ln(x)"""
  return math.sin(x) - math.log(x)

# --- Parâmetros Iniciais ---
f = define_funcao
a, b = 1.0, 5.0
cond_parada = 0.001
iteracao = 0

# --- Laço da Bissecção ---
while True:
  iteracao += 1
  m = (a + b) / 2
  f_m = f(m)
  
  # Impressão simples dos valores da iteração atual
  print(f"Iteracao={iteracao}, a={a}, b={b}, m={m}, f(m)={f_m}")
  
  # Condição de parada (a mesma de antes)
  if abs(f_m) < cond_parada:
    break 

  # Lógica para reduzir o intervalo
  if f(a) * f_m < 0:
    b = m
  else:
    a = m

# --- Resultado Final ---
print("\n--- Loop Encerrado ---")
print(f"A raiz aproximada encontrada foi: {m}")
print(f"Valor de f(m) na raiz: {f_m}")
print(f"Número de iterações: {iteracao}")