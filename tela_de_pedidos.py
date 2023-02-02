# aqui serão anotados os produtos

vendas = []

while True:
    produto = input('Registre aqui seu produto: ')
    if not produto:
        break
    qtde = int(input(f'Registre aqui a quantidade do produto {produto}: '))
    vendas.append([produto, qtde])
print(vendas)