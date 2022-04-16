from time import sleep
#Style
limpa = '\033[m'
red_bold = '\033[1;31m'
red_inv = '\033[7;31m'
bold = '\033[1m'
white_inv = '\033[7;30m'

print('{} {}LOJA SANTOS SILVA{} {}'.format('='*10, red_bold, limpa, '='*10))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 0 ] à vista dinheiro/cheque
[ 1 ] à vista cartão
[ 2 ] 2x no cartão
[ 3 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))

if opção == 0:
    print('{}10% de desconto para pagamento à vista dinheiro/cheque{}'.format(white_inv, limpa))
    print('{}CALCULANDO...{}'.format(bold, limpa))
    sleep(2)
    valor = preço * 90 / 100
    print('Essa compra de R${} sairá por um total de: {}R${:.2f}{}'.format(preço, bold, valor, limpa))
elif opção == 1:
    print('{}5% de desconto para pagamento à vista cartão{}'.format(white_inv, limpa))
    print('{}CALCULANDO...{}'.format(bold, limpa))
    sleep(2)
    valor = preço * 95 / 100
    print('Essa compra de R${} sairá por um total de: {}R${:.2f}{}'.format(preço, bold, valor, limpa))
elif opção == 2:
    print('{}parcelando em 2x no cartão não tem desconto!{}'.format(white_inv, limpa))
    print('{}CALCULANDO...{}'.format(bold, limpa))
    sleep(2)
    print('Seram duas parcelas de {}R${}{}'.format(bold, preço/2, limpa))
    print('Essa compra sairá por: {}R${}{}'.format(bold, preço, limpa))
elif opção == 3:
    parcelas = int( input('Dividirá em quantas parcelas? '))
    porc = parcelas - 2
    print('{}Juros de {}% para pagamentos em {}x no cartão{}'.format(white_inv, porc, parcelas, limpa))
    print('{}CALCULANDO...{}'.format(bold, limpa))
    sleep(2)
    valor = (preço * (100 + porc)) / 100
    print('Seram {} parcelas de {}R${:.2f}{} mensais.'.format(parcelas, bold, valor/parcelas, limpa))
    print('Essa compra de R${} sairá por um total de: {}R${:.2f}{}'.format(preço, bold, valor, limpa))
else:
    print('{}ESSA OPÇÃO NÃO É VÁLIDA!{}'.format(red_inv, limpa))