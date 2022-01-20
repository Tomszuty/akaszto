def keres(feladvany, lista):
    eredmeny=[]
    for helyseg in lista:
        if len(feladvany) == len(helyseg) and helyseg[0] == feladvany[0] and helyseg[-1] == feladvany[-1]:
            eredmeny.append(helyseg)
    return eredmeny

def betutipp(feladvany:str, helyseg):
    index = feladvany.index('.')
    return helyseg[index]

def ellenor(eredeti, uj, betu):
    if len(eredeti) != len(uj):
        return False
    for i in range(len(eredeti)):
        if eredeti[i] != uj[i]:
            if eredeti[i] != '.':
                return False
            else:
                if uj[i] != betu:
                    return False  
    return True

def kizar(lista, betu):
    eredmeny=[]
    for helyseg in lista:         
        if not betu in helyseg[1:-1]:
            eredmeny.append(helyseg)
    return eredmeny

print("Most te gondolj!")
    kiirando=input("Írd be a feladványt:")
    lehetsegesek = keres(kiirando, helysegek)
    #print(lehetsegesek)
    # while ciklus inkább, amíg több mint 1 lehetséges van!
    if len(lehetsegesek) == 0:
        print("Nincs ilyen település.")
    elif len(lehetsegesek) == 1:
        print(lehetsegesek[0], "a gondolt város.")
    else:
        betu = betutipp(kiirando, lehetsegesek[0])
        valasz = input(f"Van benne '{betu}' betű? (i/n): ")
        if valasz == "i":
            kiirando2=input("Írd be a feladványt:")
            while not ellenor(kiirando, kiirando2, betu):
                kiirando2=input("Írd be a feladványt:")
            lehetsegesek = keres(kiirando, lehetsegesek)
        else:
            lehetsegesek = kizar(lehetsegesek, betu)
            