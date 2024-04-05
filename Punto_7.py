def Multiplicacion (x : int , y : int) :
    i : int = x * y
    return i

if __name__ == "__main__" :
    for i in range(1,10):
        print("La tabla del " + str(i))
        for j in range(1,10):
            print(str(i) + " x " + str(j) + " = " + str(Multiplicacion(i,j)))