ano_inicial = 1995
ano_final = 2025
salario_inicial = 1000.0
percentual_aumento = 0.015 
salario = salario_inicial
for ano in range(ano_inicial + 1, ano_final + 1):
    salario += salario * percentual_aumento  
    percentual_aumento *= 2 
print(f"O salário do funcionário em {ano_final} será de R$ {salario:.2f}")
