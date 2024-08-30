valor_principal = 10000  
taxa_juros_anual = 5    
numero_parcelas = 24    


taxa_juros_mensal = taxa_juros_anual / 12 / 100


if taxa_juros_mensal > 0:
    parcela = (valor_principal * taxa_juros_mensal * (1 + taxa_juros_mensal) ** numero_parcelas) / ((1 + taxa_juros_mensal) ** numero_parcelas - 1)
else:
    parcela = valor_principal / numero_parcelas 


print(f"O valor da parcela mensal é: R${parcela:.2f}")
