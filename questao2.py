numPares = 0 
numImpares = 0 
for i in range(10):
    número = int(input(f"Digite o {i+1}° número inteiro:"))
    if número % 2 == 0: 
        numPares+=1
        
    else:
        numImpares += 1

        print(f"Quantidade de números pares: {numPares}")
        print(f"Quantidade de números impares: {numImpares}")