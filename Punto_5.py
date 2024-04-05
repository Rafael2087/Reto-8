def Potencia (x : int , y : int):
    i : int = x
    for j in range(y-1):
        i = i * x
    return i    

if __name__ == "__main__" :
    i : int = int(input("Dijite un número natural: "))
    if i == 0 :
        print("El número 2 elevado a la 0 es igual a 1")
    elif i < 0 :
        print("Dijite un número positivo")
    else:
        print("El número 2 elevado a la " + str(i) + " es igual a " + str(Potencia(2,i)))
        
