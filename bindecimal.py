binario = input("Digite o número binário (no formato x.y): ")
expoente = int(input("Digite o expoente: "))

partes = binario.split('.')
parte_inteira = int(partes[0], 2)
parte_fracionaria = sum(int(bit) * 2**(-i-1) for i, bit in enumerate(partes[1]))

numero_decimal = (parte_inteira + parte_fracionaria) * 2 ** expoente

print(numero_decimal)