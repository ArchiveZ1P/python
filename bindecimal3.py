decimal = 0.0
potencia = -1

num = ['1.100001010001001', '1.100001010001001', '1.101101100101001', '1.100100111111011', '1.000111110101010'] 
exp = [-1, 5, 8, 17, -14]

for cont in range(len(num)):
    partes = num[cont].split('.')
    inteira = int(partes[0], 2)

    for i in partes[1]: #Percorre por cada numero da parte decimal
        if i == '1': #Se o numero for 1, entao realiza a opreacao multiplicando pelo expoente e a cada repetição diminui o expoente
            decimal += 2 ** potencia
        potencia -= 1

    res = ((inteira + decimal) * 2 **exp[cont]) # da o resultado final e multiplica pelo expoente
    print("Convertido:", res)
    decimal = 0.0 #Reseta variaveis para proxima iteracao 
    potencia = -1
