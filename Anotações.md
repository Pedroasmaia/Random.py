# Python

---

# 01 | Dados:

### Dicionários:

```python
#Definindo Dicionario
dicionario = {"Chave" : "Valor","1": "um","2": "dois"}
#Buscando valor
descobrindo = dicionario["Chave"]
print(descobrindo)
#Adicionando novo valor
dicionario["Nova_chave"] = "Novo_valor"
print(dicionario)
#Descobrir todas as chaves:, define todas as chaves na nova variavel (chaves):
for chaves in dicionario:
    print(chaves)
#outra forma:
print(dicionario.keys())
#Se eu quiser pegar todos os valores:
for chaves in dicionario:
    valores = dicionario[chaves]
    print(valores)
#outra forma
print(dicionario.values)
#Retirando uma chave:
dicionario.pop("Chave")
print(dicionario)
#Verificar se uma Chave existe:
if "1" in dicionario:
     print('Existe')
else:
    print('Não existe')	
```

---