
populacao_A = 80000
populacao_B = 200000
taxa_crescimento_A = 0.03  # 3%
taxa_crescimento_B = 0.015  # 1.5%
anos = 0
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
