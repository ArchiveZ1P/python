import numpy as np

ci = [1.0,2.0]
ci2 = [-2.0,3.0]
new1 = 1.5
new2 = -1.5
sec1 = ci[0]
sec2= ci[1]
secb1 = ci2[0]
secb2 = ci2[1]
max_it = 1000
prec_x = 1E-5
prec_f = 1E-7

#Resultado
def calc_res1(x):
    return (5 * np.log(x)) - 2 + (0.4 * x)

def calc_res2(x):
    return (x - (((x**5) - 26) / (5 * x**4)))

#Derivada
def calc_der1(x):
    return (5/x) + 0.4

def calc_der2(x):
    return ((4/5) - (104/(5*(x**5)))) 

#Bisseção a)
for i in range(max_it):
    bis = (ci[0] + ci[1])/2
    res1 = calc_res1(bis)
    if abs(ci[1]-ci[0]) < prec_x and abs(res1) < prec_f:
        break
    if res1 < 0:
        ci[0] = bis
    elif res1 >= 0:
        ci[1] = bis
print(f"Bisseção a), iteração {i+1}: {bis}\n")

#Bisseção b)
for i in range(max_it):
    bis = (ci2[0] + ci2[1])/2
    res1 = calc_res2(bis)
    if abs(ci2[1]-ci2[0]) < prec_x and abs(res1) < prec_f:
        break
    if res1 < 0:
        ci2[0] = bis
    elif res1 >= 0:
        ci2[1] = bis
print(f"Bisseção b), iteração {i+1}: {bis}\n")

#Newton a)
for i in range(max_it):
    fx1 = calc_res1(new1)
    fxl1 = calc_der1(new1)
    new1 -= fx1/fxl1
    if abs(fx1) < prec_f:
        break
print(f"Newton-Raphson a), iteração {i+1}: {new1}\n")

#Newton b)   
for i in range(max_it):
    fx2 = calc_res2(new2)
    fxl2 = calc_der2(new2)
    new2 -= fx2/fxl2
    if abs(fx2) < prec_f:
        break
print(f"Newton-Raphson b), iteração {i+1}: {new2}\n")

#Secante a)
for i in range(max_it):
    xk1 = calc_res1(sec1)
    xk2 = calc_res1(sec2)
    aux = sec2
    if xk2 != xk1:
        sec2 -= (xk2 * (sec2 - sec1)) / (xk2 - xk1)
        if abs(sec2-sec1) < prec_x and abs(xk2) < prec_f:
            break
    else: 
        print("xk2 - xk1 resultou em 0")
        break
    sec1 = aux
print(f"Secante a), iteração {i+1}: {sec2}\n")
    
#Secante b)
sec1 = 1
sec2= 2
for i in range(max_it):
    xk3 = calc_res2(sec1)
    xk4 = calc_res2(sec2)
    aux = sec2
    if xk4 != xk3:
        sec2 -= (xk4 * (sec2 - sec1)) / (xk4 - xk3)
        if abs(sec2-sec1) < prec_x and abs(xk4) < prec_f:
            break
    else: 
        print("xk4 - xk3 resultou em 0")
        break
    sec1 = aux
print(f"Secante b), iteração {i+1}: {sec2}\n")