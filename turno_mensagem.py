turno = input(
    "Em qual turno você estuda?\n - M ou m, para matutino;\n - V ou v, para vespertino;\n - N ou n, para noturno.")

if (turno.lower() == "m"):
    print("Bom dia!")
elif (turno.lower() == "v"):
    print("Boa Tarde!")
elif (turno.lower() == "n"):
    print("Boa Noite!")
else:
    print("Valor Inválido!")
