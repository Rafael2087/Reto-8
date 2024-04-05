import math

e : float = math.e

def Maclaurin_e (x : float , y : int):
    result = 0
    for n in range(y + 1):
        result += (x ** n) / math.factorial(n)
    return result


if __name__ == "__main__":
    i : float = float(input("Dijite el exponente: "))
    j : int =int(input("Dijite la cantidad de terminos: "))

    print("La aproximación de Maclaurin da: " + str(Maclaurin_e(i,j)))
    print("El valor real es: " + str(e**i))

    if (e**i - Maclaurin_e(i,j) )*100 > 0.1 :
        print("La aproximación de Maclaurin para " + str(j) + " terminos no es precisa")
    else:    
        print("La aproximación de Maclaurin para " + str(j) + " es precisa")
    