# Preço dos produtos

M100 = 1.10
M101 = 2.20
M102 = 3.30
M103 = 4.40
M104 = 5.50
M105 = 6.60

# cardápio:

print(f'''Especificação   Código  Preço
Hamburguer Vegano   M100     R$ {M100:.2f}
Porção de Fritas    M101     R$ {M101:.2f}
Porção de Mandioca  M102     R$ {M102:.2f}
Suco Diversos       M103     R$ {M103:.2f}
Torta de Chocolate  M104     R$ {M104:.2f}
Bolo de Laranja     M105     R$ {M105:.2f}''')

## aqui serão anotados os produtos

                # vendas = []

                # while True:
                #     produto = input('Registre aqui seu produto e para encerrar o pedido, digite "encerrar": ')
                #     if not produto:
                #         break
                #     qtde = int(input(f'Registre aqui a quantidade do produto {produto}: '))
                #     if not qtde:
                #         break
                #     vendas.append([produto, qtde])
                # print(vendas)

## calculo do valor a ser pago

total = 0
produto = input('\nRegistre aqui seu produto e para encerrar o pedido, digite "encerrar": ')
while produto != 'encerrar':
    qtde = int(input('Informe a quantidade: '))
    if produto == 'M100':
        total += M100 * qtde
    elif produto == 'M101':
        total += M101 * qtde
    elif produto == 'M102':
        total += M102 * qtde
    elif produto == 'M103':
        total += M103 * qtde
    elif produto == 'M104':
        total += M104 * qtde
    elif produto == 'M105':
        total += M105 * qtde
    if not produto:
        break        
    produto = input('Registre aqui seu produto e para encerrar o pedido, digite "encerrar": ')

print(f'O total a ser pago é: R$ {total:.2} \n O pagamento poderá ser feito através do QR Code que foi gerado.')

import qrcode
imagemqrcode = qrcode.make(total)
imagemqrcode.save('valortotal_qrcode.png')