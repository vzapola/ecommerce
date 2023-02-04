# Preço dos produtos

M100 = 1.20
M101 = 1.30
M102 = 1.50
M103 = 1.20
M104 = 1.30
M105 = 1.00

# cardápio:

print(f'''Especificação   Código  Preço
Hamburguer Vegano   100     R$ {M100:.2f}
Porção de Fritas    101     R$ {M101:.2f}
Porção de Mandioca  102     R$ {M102:.2f}
Suco Diversos       103     R$ {M103:.2f}
Torta de Chocolate  104     R$ {M104:.2f}
Bolo de Laranja     105     R$ {M105:.2f}''')

# aqui serão anotados os produtos

vendas = []

while True:
    produto = input('Registre aqui seu produto: ')
    if not produto:
        break
    qtde = int(input(f'Registre aqui a quantidade do produto {produto}: '))
    vendas.append([produto, qtde])
print(vendas)