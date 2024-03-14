import numpy as np
import matplotlib.pyplot as plt

# Função para calcular os coeficientes do polinômio interpolador de Newton
def coef_newton(X, Y):
    n = len(X)
    coef = np.zeros([n, n]) # matriz de coeficientes
    coef[:,0] = Y # primeira coluna é Y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (X[i+j] - X[i])

    return coef[0, :] # retorna a primeira linha

# Função para calcular o valor do polinômio interpolador de Newton em um ponto
def eval_newton(coef, X, x):
    n = len(X) - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x - X[n-k])*p
    return p

# Dados
conjuntos = [
    {"X": np.array([0, 2, 4, 6, 8, 10]), "Y": np.array([0.9, 2, 2.8, 3.1, 5.9, 6])},
    {"X": np.array([0, 2, 4, 6, 8]), "Y": np.array([1, 9.389, 58.598, 409.429, 2988.958])},
    {"X": np.array([0, 2, 4, 6, 8, 10, 12, 14, 16]), "Y": np.array([1, 7, 21, 22, 34, 34.5, 35, 64.5, 65])}
]

for i, conjunto in enumerate(conjuntos):
    X = conjunto["X"]
    Y = conjunto["Y"]

    # Polinômio interpolador de Lagrange
    P_Lagrange = np.poly1d(np.polyfit(X,Y,len(X)-1))

    # Valor da função f(X) para X=5.2
    f_5_2_Lagrange = P_Lagrange(5.2)

    # Coeficientes do polinômio interpolador na forma canônica
    coef_Lagrange = P_Lagrange.coefficients

    print(f"Conjunto {i+1} - Método de Lagrange:")
    print(f"f(5.2) = {f_5_2_Lagrange}")
    print(f"Coeficientes: {coef_Lagrange}")

    # Polinômio interpolador de Newton
    coef_Newton = coef_newton(X,Y)

    # Valor da função f(X) para X=5.2
    f_5_2_Newton = eval_newton(coef_Newton,X,5.2)

    print(f"\nConjunto {i+1} - Método de Newton:")
    print(f"f(5.2) = {f_5_2_Newton}")
    print(f"Coeficientes: {coef_Newton}\n")

    # Plot do gráfico
    plt.figure()
    
    plt.plot(X,Y,'ro') # pontos originais em destaque
    
    X_plot = np.linspace(np.min(X),np.max(X),500)
    
    Y_plot_Lagrange = P_Lagrange(X_plot)
    
    plt.plot(X_plot,Y_plot_Lagrange,'b-', label='Lagrange') # função polinomial de Lagrange
    
    Y_plot_Newton = [eval_newton(coef_Newton,X,x) for x in X_plot]
    
    plt.plot(X_plot,Y_plot_Newton,'g-', label='Newton') # função polinomial de Newton
    
    plt.title(f"Conjunto {i+1} - Métodos de Lagrange e Newton")
    
    plt.legend()
    
    plt.show()
