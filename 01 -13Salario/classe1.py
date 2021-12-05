print("Calculadora do Adiantamento do 13° Salario!")
print("Sempre usar ponto(.) ao invés de virugla(,) para números decimais!")

print("Qual é o valor em conta capital?")
capital:float = float(input())

print("Qual é o valor do salario?")
salario:float = float(input())

print("Qual é o valor dos beneficios?")
beneficios:float = float(input())

TSalario:float = salario + beneficios

print("Quanto é o desconto do inss?")
inss:float = float(input())

print("Quanto é o desconto do Imposto de renda?")
ir:float = float(input())

TDescontos:float = ir + inss

ts2 = TSalario / 2.0 - TDescontos
td2 = ts2 * 0.7

tcapital = capital * 0.7

if td2 > tcapital:
	print("O 13° salario deve ser: R$", round(td2, 2)," baseado no salário.")
else:
	print("O 13° salario deve ser: R$", tcapital," baseado no capital.")
