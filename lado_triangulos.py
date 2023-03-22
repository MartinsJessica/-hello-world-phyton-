lado_a = int(input("Digite o valor do lado A:"))
lado_b = int(input("Digite o valor do lado B:"))
lado_c = int(input("Digite o valor do lado C:"))

if (lado_a > lado_b + lado_c or lado_b > lado_a + lado_c or lado_c > lado_a + lado_b):
    print("Não é possível formar um triangulo!")
else:
    if (lado_a == lado_b == lado_c):
        print("Triângulo Equilátero")
    elif (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
        print("Triangulo Isósceles")
    else:
        print("Triângulo Escaleno")
