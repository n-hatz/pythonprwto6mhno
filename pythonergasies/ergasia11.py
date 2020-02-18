text = open("tetrades.txt", "r")
lista = text.read().splitlines()
newlista = []
for i in range(len(lista)):
    newlista += lista[i].split()
exada = input("Εισάγετε έναν εξαψήφιο αριθμό: ")
t1 = []
t2 = []
t3 = []
for i in range(4): #τα πρώτα 4 ψηφία της εξάδας τοποθετούνται σε πίνακα (πρώτη τετράδα)
    t1.append(exada[i]) #η τετράδα γίνεται μεταβλητή
tetrada1=''.join(t1)
for i in range(1,5): #τα ψηφία 2-5 της εξάδας τοποθετούνται σε πίνακα (δεύτερη τετράδα)
    t2.append(exada[i])
tetrada2=''.join(t2)
for i in range(2,6): #τα τελευταία 4 ψηφία της εξάδας τοποθετούνται σε πίνακα (τρίτη τετράδα)
    t3.append(exada[i])
tetrada3=''.join(t3)
for i in range(len(newlista)): #ελέγχει αν κάποια από τις τετράδες περιέχεται στο αρχείο (χρησιμοποιείται i+1 επειδή συνήθως τη μέτρηση την ξεκινάμε από το 1)
    if newlista[i] == tetrada1:
        print("Υπάρχει η τετράδα ", tetrada1, ",είναι η τετράδα ", i+1, " του αρχείου")
    elif newlista[i] == tetrada2:
        print("Υπάρχει η τετράδα ", tetrada2, ",είναι η τετράδα ", i+1, " του αρχείου")
    elif newlista[i] == tetrada3:
        print("Υπάρχει η τετράδα ", tetrada3, ",είναι η τετράδα ", i+1, " του αρχείου")
