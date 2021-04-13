totalpares = 0
totalimpares = 0

n = int(input("Numero (0 para terminar): "))

while n != 0:
    pares = 0
    impares = 0

    while n != 0:
        ultimoDigito = n % 10
        if ultimoDigito % 2 == 0:
            pares += 1
            totalpares += 1
        else:
            impares += 1
            totalimpares += 1
        n = n // 10

    print("pares ", pares, " impares", impares)
    n = int(input("Numero (-1 para continuar): "))
print("total pares ", totalpares)
print("total impares ", totalimpares)