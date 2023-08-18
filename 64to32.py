import numpy as np
   
valores = [5.21, 35.0, 47.5]
exp = [0, -95, 112]
for i in range(len(valores)):
    x = np.float64(valores[i]*(10**exp[i]))
    y = np.float32(x)
    dif = x-y
    print(f'64: {x}\n32: {y}\nDiferença: {dif}\n\n')
