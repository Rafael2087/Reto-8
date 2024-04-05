if __name__ == "__main__" :
    i : int = int(input("DIjite un número: "))
    if i % 2 != 0 :
        i = i - 1
    if i < 2 :
        print("Dijite un número mayor que 2")
    else:
        for j in range (i,1,-2):
            print(j)