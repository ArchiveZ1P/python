import numpy as np

def gaussSeidel(A, b, inicial, max_ite, tol, lamb):
    ite = 0
    while ite < max_ite:
        inicial_aux = np.copy(inicial)
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * inicial[j]
            x /= A[i][i]
            inicial[i] = (1 - lamb) * inicial_aux[i] + lamb * x
        ite += 1
        if np.all(np.abs(inicial - inicial_aux) < tol):
            break
    return inicial, ite

A = np.array([[4, -3, 1], [2, 4, -2], [4, 3, 3]], dtype=float)
b = np.array([29, -18, 3], dtype=float)

inicial = np.zeros(len(b))
max_ite = 1000
tol = 1e-9

res, ite = gaussSeidel(A, b, inicial, max_ite, tol, 1)
print(f"Sem relaxação:")
print(res)
print("Número de iterações:", ite)
print("\n")

v_lambda = [0.2, 0.5, 1.5]
print(f"Com relaxação:")
for i in v_lambda:
    inicial = np.zeros(len(b))
    res, ite = gaussSeidel(A, b, inicial, max_ite, tol, i)
    print(f"Lambda = {i}:")
    print(res)
    print("Número de iterações:", ite)
    print("\n")