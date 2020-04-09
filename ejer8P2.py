def esPrimo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print('Ingrese el string a analizar')
cadena = input()

dic = {}

cont = 0

for d in cadena:
    car = d
    cont = 0
    print(car)
    if (car in cadena):
        for s in cadena:
            if (car == s):
                cont = cont + 1
        if (car not in dic):
            if (esPrimo(cont)):
                dic[car] = "El caracter aparece: ", cont, " veces y es primo"
            else:
                dic[car] = "El caracter aparece: ", cont, " veces y no es primo"

print(dic)
