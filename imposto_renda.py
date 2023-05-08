nro_horas = float(input("Quantas horas você trabalha por mês? "))
valor_h = float(input("Valor por hora trabalhada? "))
nro_filhos = int(input("Digite quantos filhos você tem: "))
salario_bruto = valor_h * nro_horas
salario_liquido = salario_bruto - (189.95 * nro_filhos)

print(salario_bruto, salario_liquido)

if salario_liquido < 1903.98:
    desconto_ir = 0.0
elif salario_liquido <= 2826.66:
    desconto_ir = 7.5
elif salario_liquido <= 3751.06:
    desconto_ir = 15
elif salario_liquidi <= 4664.68:
    desconto_ir = 22.5
else:
    desconto_ir = 27.5
    
imposto_renda = salario_liquido * (desconto_ir/100.0)

imposto_renda_formatado = "{:.2f}".format(imposto_renda)

print(imposto_renda_formatado)
