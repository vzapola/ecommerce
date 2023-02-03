# cardápio:

print('''Especificação   Código  Preço
Hamburguer Vegano   100     R$ 1,20
Porção de Fritas    101     R$ 1,30
Porção de Mandioca  102     R$ 1,50
Suco Diversos       103     R$ 1,20
Torta de Chocolate  104     R$ 1,30
Bolo de Laranja     105     R$ 1,00''')

# aqui serão anotados os produtos

vendas = []

while True:
    produto = input('Registre aqui seu produto: ')
    if not produto:
        break
    qtde = int(input(f'Registre aqui a quantidade do produto {produto}: '))
    vendas.append([produto, qtde])
print(vendas)