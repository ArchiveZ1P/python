import numpy as np

#Funções
f1 = lambda x: 3 + 4*x - 3*x**2 + 5*x**3 - x**4 + 4*x**5
f2 = lambda x: np.sqrt(x)

#Limites de integração
a1, b1 = 0, 2
a2, b2 = 0, 20

# Integrais analíticas
I1_analitico = 2**6 - 2**5/2 + 5*2**4/4 - 2**5/5 + 4*2**6/6 - 3
I2_analitico = 2/3 * 20**(3/2)

# Pontos
pontostrape1 = [2, 5, 13]
pontosSimp1 = [3, 5, 13]
pontosGauss1 = [1, 2, 3]
pontostrape2 = [2, 5, 99]
pontosSimp2 = [3, 5, 99]

#Fórmulas
def trapezio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2::2]) + y[-1])

def quadratura(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5 * (x + 1) * (b - a) + a
    return np.dot(w, f(t)) * 0.5 * (b - a)

# Calculando as integrais usando os métodos implementados
print(f'Função 1 integral (Trapézio) para os pontos {pontostrape1}')
for n in pontostrape1:
    I1_trapz = trapezio(f1, a1, b1, n)
    E1_trapz = abs(I1_analitico - I1_trapz)
    print(f'Resultado: {I1_trapz}')
    print(f'Erro absoluto {E1_trapz}\n')
    
print(f'Função 1 integral (Simpson) para os pontos {pontosSimp1}')
for n in pontosSimp1:
    I1_simpson = simpson(f1, a1, b1, n)
    E1_simpson = abs(I1_analitico - I1_simpson)
    print(f'Resultado: {I1_simpson}')
    print(f'Erro absoluto {E1_simpson}\n')
    
print(f'Função 1 integral (Quadratura) para os pontos {pontosGauss1}')
for n in pontosGauss1:
    I1_gauss = quadratura(f1, a1, b1, n)
    E1_gauss = abs(I1_analitico - I1_gauss)
    print(f'Resultado: {I1_gauss}')
    print(f'Erro absoluto {E1_gauss}\n')
    
print(f'Função 2 integral (Trapézio) para os pontos {pontostrape2}')
for n in pontostrape2:
    I2_trapz = trapezio(f2, a2, b2, n)
    E2_trapz = abs(I2_analitico - I2_trapz)
    print(f'Resultado: {I2_trapz}')
    print(f'Erro absoluto {E2_trapz}\n')
    
print(f'Função 2 integral (Simpson) para os pontos {pontosSimp2}')
for n in pontosSimp2:
    I2_simpson = simpson(f2, a2, b2, n)
    E2_simpson = abs(I2_analitico - I2_simpson)
    print(f'Resultado: {I2_simpson}')
    print(f'Erro absoluto {E2_simpson}\n')
    
#Gaussiana com subdivisão do intervalo
def gaussian_quadrature_subdiv(f, a, b, n, m):
    subintervalos = np.linspace(a, b, m+1)
    result = 0
    for i in range(m):
        result += quadratura(f, subintervalos[i], subintervalos[i+1], n)
    return result

I2_gauss_subdiv = gaussian_quadrature_subdiv(f2, a2, b2, 5, 4)
E2_gauss_subdiv = abs(I2_analitico - I2_gauss_subdiv)

print(f'Função 2 integral (Quadratura com subdivisão) para 5 pontos em cada subintervalo:')
print(f'Resultado: {I2_gauss_subdiv}')
print(f'Erro absoluto {E2_gauss_subdiv}\n')