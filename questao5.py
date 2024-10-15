preco_unitario = 1.99
quantidade_maxima = 50
print("Lojas Quase Dois - Tabela de preços")
for quantidade in range(1, quantidade_maxima + 1):
    total = quantidade * preco_unitario
    print(f"{quantidade} - R$ {total:.2f}")
