# aqui serão anotados os pedidos

pedido = input('Registre aqui o seu pedido. Registre quantos produtos quiser e, para finalizar o pedido, basta apertar enter com a caixa vazia:')
pedidos = []

while pedido != '':
    pedidos.append(pedido)
    pedido = input('Registre aqui o seu pedido. Registre quantos produtos quiser e, para finalizar o pedido, basta apertar enter com a caixa vazia:')
        
print(f'Resumo do pedido: Os itens foram {pedidos}')