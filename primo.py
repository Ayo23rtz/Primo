
n = input('Ingrese un numero: ')
while n.isdecimal() is False:
     n = input('El digito ingresado no es un numero, por favor ingrese un numero: ')

n = int(n)


def es_primo():
    if n < 2:
        return False
    else:
        for elemento in range(2, n):
            if n % elemento == 0:
                return False
        return True
        
print(es_primo())

