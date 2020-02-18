n = eval(input("Εισάγετε έναν αριθμό: "))
k = 0
while len(str(n)) > 1:
    k = 3*int(n) + 1
    n = str(k)
    print("Ο αριθμός επί τρία συν ένα: ", n)
    k = 0
    for i in range(len(n)):
        k += int(n[i])
    print("Το άθροισμα των ψηφίων: ", k)
    n = str(k)
    k = 0
