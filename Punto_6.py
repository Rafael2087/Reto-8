def Potencia (x : float , y : int):
    i : float = x
    for j in range(y-1):
        i = i * x
    return i 

if __name__ == "__main__" :
    j : float = float(input("Dijite un número: "))    
    i : int = int(input("Dijite un número natural: "))
    if i == 0 :
        print("El número " + str(j) + " elevado a la 0 es igual a 1")
    elif i < 0 :
        print("Dijite un número positivo")
    else:
        print("El número " + str(j) + " elevado a la " + str(i) + " es igual a " + str(Potencia(j,i)))
        
