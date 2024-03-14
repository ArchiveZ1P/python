import numpy as np
import math

# Função da EDO
def f(t, y):
    return y + math.exp(2*t) + math.sin(t) + math.cos(t)

# Função exata
def y_exacta(t):
    return math.exp(2*t) - math.cos(t)

# Método de Euler
def euler(h, t0, y0, t):
    while t0 < t:
        y0 = y0 + h*f(t0, y0)
        t0 = t0 + h
    return y0

# Método de Euler melhorado
def euler_melhorado(h, t0, y0, t):
    while t0 < t:
        k1 = h*f(t0, y0)
        k2 = h*f(t0 + h, y0 + k1)
        y0 = y0 + 0.5*(k1 + k2)
        t0 = t0 + h
    return y0

# Método de Runge-Kutta de 4ª ordem
def runge_kutta(h, t0, y0, t):
    while t0 < t:
        k1 = h*f(t0, y0)
        k2 = h*f(t0 + 0.5*h, y0 + 0.5*k1)
        k3 = h*f(t0 + 0.5*h, y0 + 0.5*k2)
        k4 = h*f(t0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6
        t0 = t0 + h
    return y0

# Parâmetros iniciais
t0 = 0
y0 = 0
t = 2

# Passos para cada método
h_euler = (t - t0) / 16
h_euler_melhorado = (t - t0) / 8
h_runge_kutta = (t - t0) / 4

# Calculando os valores
y_euler = euler(h_euler, t0, y0, t)
y_euler_melhorado = euler_melhorado(h_euler_melhorado, t0, y0, t)
y_runge_kutta = runge_kutta(h_runge_kutta, t0, y0, t)
y_exato = y_exacta(t)

# Calculando os erros
e_euler = y_exato - y_euler
e_euler_melhorado = y_exato - y_euler_melhorado
e_runge_kutta = y_exato - y_runge_kutta

# Imprimindo os resultados
print('Método de Euler:', y_euler, ', Erro:', e_euler)
print("Método de Euler Melhorado: ", y_euler_melhorado, ', Erro:', e_euler_melhorado)
print("Método de Runge-Kutta: ", y_runge_kutta, ', Erro:', e_runge_kutta)
print("Valor exato: ", y_exato)