preço = float(input("Qual é o preço do produto? R$"))
desconto = (preço * 5) / 100
preço_atual = preço - desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}' .format(preço, preço_atual))