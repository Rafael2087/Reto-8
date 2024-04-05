def Cuadrado (x : int):
    i = x**2
    return i

if __name__ == "__main__" :
    for i in range (1,101):
        print("El número es " + str(i) + " y su cuadrado es " + str(Cuadrado(i)))