import random
def menua1():
    print("Ongi etorri Mekanografia testera, orain, aukeratu zein modutan jokatu nahi duzun")
    print()
    print("1- Hiru Esaldi")
    print("2- Modu librea")
    print("3- Atera")
    print()
    aukera=int(input("Aukeratu: "))
    return aukera

def menua2():
    print("Jokatzen segitu nahi duzu?")
    print()
    print("1- Hiru Esaldi")
    print("2- Modu librea")
    print("3- Atera")
    print()
    aukera=int(input("Aukeratu: "))
    return aukera


aukera=menua1()

while aukera!=3:

    Esaldi_zerrenda=["Maza rata callejera", "Informatika oso ikasgai baliagarria da", "Jai alai zestapunta", "Afaldu denbora galdu", "Mikel Goñi askatu","Orain farrak gero negarrak", "Ongi pasa pasatu gabe", "Borroka da bide bakarra", "Chivite mongola Navarra es una sola", "Jo ta ke irabazi arte", "Ford Focus ecobus", "Carrero Blanco campeón de salto", "Espiritu mendekatsua edo txabizak esaten duen bezala, le cum", "Lehenengo aldagaia gero balioa"]
    luzera_zerrenda= len(Esaldi_zerrenda)
    r=random.randint(0,luzera_zerrenda-1)
    hitza=(Esaldi_zerrenda[r])
    luzera_hitza=len(hitza)
    kontagailua=0
    esaldia=0
    asmatu=0

    if aukera==1:
        
        while esaldia<3:
            asmatu=0
            kontagailua=0
            r=random.randint(0,luzera_zerrenda-1)
            hitza=(Esaldi_zerrenda[r])
            luzera_hitza=len(hitza)
            print(hitza)
            idatzitakoa=input("Idatzi goiko esaldia: ")
            luzera_idatzitakoa= len(idatzitakoa)
            while kontagailua<min(luzera_idatzitakoa,luzera_hitza):
                hitza=(Esaldi_zerrenda[r])
                if idatzitakoa[kontagailua]==hitza[kontagailua]:
                    asmatu=asmatu+1
                kontagailua=kontagailua+1
            print(asmatu*100/max(luzera_idatzitakoa,luzera_hitza), "%")
            esaldia=esaldia+1

    if aukera==2:
        ronda=int(input("Zenbat esaldi egin nahi dituzu: ")) 
        while esaldia<ronda:
            asmatu=0
            kontagailua=0
            r=random.randint(0,luzera_zerrenda-1)
            hitza=(Esaldi_zerrenda[r])
            luzera_hitza=len(hitza)
            print(hitza)
            idatzitakoa=input("Idatzi goiko esaldia: ")
            luzera_idatzitakoa= len(idatzitakoa)
            while kontagailua<min(luzera_idatzitakoa,luzera_hitza):
                hitza=(Esaldi_zerrenda[r])
                if idatzitakoa[kontagailua]==hitza[kontagailua]:
                    asmatu=asmatu+1
                kontagailua=kontagailua+1
            esaldia=esaldia+1
            print(asmatu*100/max(luzera_idatzitakoa,luzera_hitza), "%")

    aukera=menua2()
