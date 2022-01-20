import random
def beolvas(filenev):
    # ide jön a kód
    lista = []
    forrasfile = open(filenev,mode='r',encoding='UTF-8')
    for sor in forrasfile:
        lista.append(sor.strip())
    forrasfile.close()
    return lista

def feladvany(szo):
    return szo[0] + "." * (len(szo) - 2) + szo[-1]

def cserel(feladvany, szo, betu):
    eredmeny = szo[0]
    for i in range(1, len(szo)-1):
        if szo[i] == betu:
            eredmeny += betu
        else:
            eredmeny += feladvany[i]
    eredmeny += szo[-1]
    return eredmeny 

def gep_gondol(helysegek):
    feladat = random.choice(helysegek)
    kiirando = feladvany(feladat)
    print(kiirando)
    proba = 6
    while "." in kiirando and proba > 0:
        betu = input("adj meg egy betut: ")
        if len(betu) > 1:
            if betu.lower() != feladat.lower():            
                proba = 0
            break

        if betu in feladat[1: -1]:
            kiirando = cserel(kiirando, feladat, betu)
        else:
            proba -= 1
            print("a hianyzo betu kozott nem talalhato", proba, "tipped van meg")            
        print(kiirando)

    if proba > 0:
        print("grat")
    else:
        print("jo bena vagy a gondolt szo: ", feladat)

def main():
    helysegek = beolvas("helyek.txt")
    gep_gondol(helysegek)

    
      


main()