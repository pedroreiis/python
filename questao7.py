def calcular_tabela_dividas(divida):
    tabela_juros = {
        1: 0,
        3: 0.10,
        6: 0.15,
        9: 0.20,
        12: 0.25
    }
    print("| Dívida        | Juros | Quantidade de Parcelas | Valor da Parcela |")
    print("|---------------|-------|-----------------------|------------------|")
    for parcelas, taxa_juros in tabela_juros.items():
        valor_juros = divida * taxa_juros
        valor_total = divida + valor_juros
        valor_parcela = valor_total / parcelas
        print(f"| R$ {valor_total:.2f} | R$ {valor_juros:.2f} | {parcelas}                     | R$ {valor_parcela:.2f}      |")

valor_divida = 1000.00
calcular_tabela_dividas(valor_divida)
