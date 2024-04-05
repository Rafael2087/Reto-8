def Factorial ( x : int ):
    Factorial_Numero : int = 1
    for i in range (1, x + 1):
        Factorial_Numero = Factorial_Numero * i
    return Factorial_Numero

if __name__ == "__main__" :
    i : int = int(input("Dijite un número natural: "))
    if i < 1 :
        if i == 0:
            print("El factorial de 0 es 1")
        else:
            print("Dijite un número positivo")
    else:
        for j in range (1,i+1):
            print("El factorial de " + str(j) + " es " + str(Factorial(j)))
    
    
