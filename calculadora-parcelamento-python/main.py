print('Bem-vindos à loja do Lucas!')

# solicitar ao usuário valor do pedido e quantidade de parcelas
valorPedido = float(input('Digite o valor do pedido: '))
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))

# aplicar juros:
if quantidadeParcelas <= 0:
    print('Valor de parcelas inválido, tente novamente')
    exit()
# menos de 4 parcelas = 0%
elif quantidadeParcelas < 4:
    taxa = 0
# de 4 a 5 parcelas = 4%
elif quantidadeParcelas <= 5:
    taxa = 0.04
# de 6 a 8 parcelas = 8%
elif quantidadeParcelas <= 8:
    taxa = 0.08
# de 9 a 12 parcelas = 16%
elif quantidadeParcelas <= 12:
    taxa = 0.16
# 13 parcelas ou mais = 32%
else:
    taxa = 0.32

# calcular o valor total parcelado
totalParcelado = valorPedido * (1 + taxa)
# calcular o valor da parcela
valorParcela = totalParcelado / quantidadeParcelas

#exibir o valor de cada parcela
print(f'Valor da parcela: R${valorParcela:.2f}')
#exibir o valor total parcelado
print(f'Valor total parcelado: R${totalParcelado:.2f}')

# mensagem quando não houver juros
if quantidadeParcelas < 4:
    print('Não houve juros aplicados')

