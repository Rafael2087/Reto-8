import math

def maclaurin_arctan(x, N):
    result = 0
    for n in range(N):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

if __name__ == "__main__":
    i : float = float(input(("Dijite el valor en el que va a evaluar la funcón arcotangente: ")))
    j : int = int(input("Dijite el número de polinomios: "))
    
    print("La aproximación de Maclaurin da: " + str(maclaurin_arctan(i,j)))
    print("El valor real es: " + str(math.atan(i)))

    if (math.atan(i) - maclaurin_arctan(i,j) )*100 > 0.1 :
        print("La aproximación de Maclaurin para " + str(j) + " terminos no es precisa")
    else:    
        print("La aproximación de Maclaurin para " + str(j) + " terminos es precisa")