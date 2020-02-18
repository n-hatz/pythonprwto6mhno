text = open("keimeno.txt", "r")
lista = text.read().splitlines()
newlista = []
for i in range(len(lista)):
    newlista += lista[i].split()
for i in range(len(newlista)):
    if len(newlista[i]) > 3:
        print("Η λέξη πριν από την επεξεργασία: ", newlista[i])
        x = newlista[i][0]
        newlista[i]=newlista[i].replace(newlista[i][0],"")
        l = []
        l.append(newlista[i])
        l.append(x)
        l.append("ay")
        newlista[i]=''.join(l)
        print("Η λέξη μετά την επεξεργασία: ", newlista[i])
    
