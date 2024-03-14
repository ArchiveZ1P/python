import numpy as np

def LU(A, B):
    n = len(A)
    U = np.copy(A)
    L = np.eye(n)
    P = np.eye(n)

    for k in range(n - 1):
        lp = np.argmax(np.abs(U[k:, k])) + k
        if lp != k:
            U[[k, lp]] = U[[lp, k]]
            P[[k, lp]] = P[[lp, k]]
            if k > 0:
                L[[k, lp], :k] = L[[lp, k], :k]

        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, k:] -= m * U[k, k:]

    # Triangular inferior, encontra Y
    Pb = np.dot(P, B)
    Y = np.zeros(n)
    for i in range(n):
        Y[i] = Pb[i] - np.sum(L[i, :i] * Y[:i])

    # Triangular superior, encontra X
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (Y[i] - np.sum(U[i, i+1:] * X[i+1:])) / U[i, i]

    return X

# Primeira matriz

A = np.array([[3, -4, 1],[1, 2, 2],[4, 0, -3]], dtype='double')
B = np.array([9, 3, -2], dtype='double')
X = LU(A, B)
Ax = np.dot(A, X)
dif = B - Ax

print(f'Resultado da primeira matriz: {X}\nDiferença: {dif}\n')

# Segunda matriz

A2 = np.array([[0.1, -3, 4, 7, 4, 14],[-2, 4, 2, 5, -5, 21],[1, 200, 3, -3, 3, -4],[-1, 5, 4, 22, 7, -8],[4, 8, 7, 10, -9, 1],[-55, -1, 35, 1, 11, 0.2]], dtype='double')
B2 = np.array([14, 26, 19, -5, 7, -4], dtype='double')
X2 = LU(A2, B2)
Ax2 = np.dot(A2, X2)
dif2 = B2 - Ax2

print(f'Resultado da segunda matriz: {X2}\nDiferença: {dif2}\n')