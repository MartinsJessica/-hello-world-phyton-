pedacos_pizza = 8

quantidade_pessoas = int(input("Quantidade de pessoas(no máximo 8):\n"))

pedacos_por_pessoa = pedacos_pizza // quantidade_pessoas

pedacos_restantes = pedacos_pizza % quantidade_pessoas

print("Quantidade de pedaços por pessoa:", pedacos_por_pessoa)

print("Restará(ão): ", pedacos_restantes, " pedaços")
