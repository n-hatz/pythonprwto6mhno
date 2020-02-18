text = open("keimeno.txt", "r")
lista = text.read().splitlines() #χωριζουμε το κειμενο που διαβαζουμε απο το αρχειο σε γραμμες
length = len(lista)
newlista = []
for i in range(length):
    newlista += lista[i].split() #χωριζουμε τις γραμμες σε λεξεις και τις βαζουμε σε νεο πινακα
newlista.sort(key=len) #σορταρουμε τον πινακα αναλογα με το μέγεθος
biglista = newlista[::-1] #ο νεος πινακας ισουται με τον σορταρισμένο πινακα αλλα αναποδογυρισμενο
print("Οι 5 μεγαλύτερες λέξεις χωρίς τροποποιήσεις:")
for i in range(5):
    print (biglista[i]) #τυπωνουμε τις 5 μεγαλυτερες λεξεις χωρις αλλαγες
edit = biglista[0:5] #νεος πινακας που αφορα μονο τις 5 μεγαλυτερες λεξεις
for g in range(5):
    edit[g]=edit[g][::-1]
    for x in edit[g]:
        if x in "aioue!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
           edit[g]=edit[g].replace(x,"") #αφαιρουμε τα κενα και τους ειδικους χαρακτηρες
print(" ")
print("η λίστα μετά τις τροποποιήσεις:")
for i in range(5):
    print (edit[i]) #τυπωνουμε τις τροποποιημενες λεξεις
text.close()
