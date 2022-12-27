#Infor proiektua: Mekanografia jokua

#mod:
import random
import time

#func
def menu(turno):
    if turno == 0:
        print("Ongi etorri...")
    else:
        print("Jokatzen...")
    modua = input(""" Modua: """)
    zail = input(""" Zailtasuna | 1 | 2 | 3 | : """)
    return modua, zail

def esaldia_aukeratu(zail):
    libu = []
    libu1 = ["Kaixo","Agur","ETA"]
    libu2 = ["Egun on"]
    libu3 = ["Arratsalde on"]
    if zail == '1':
        libu = libu1
    elif zail == '2':
        libu = libu2
    elif zail == '3':
        libu = libu3
    esaldia = random.choice(libu)
    #print(esaldia)
    return esaldia

def neurtu_erabilitako_denbora(hasiera):
  return round(time.time() - hasiera, 2)
        
def nota(esaldia, puntuazioa, sarrera, hasiera):
    puntuazioa = puntuazioa + len(esaldia)
    t = neurtu_erabilitako_denbora(hasiera)
    if sarrera != esaldia:
        print(f"Zerbait ez dago ongi! Erabilitako denbora: {t}")
        if len(sarrera) < len(esaldia):
            puntuazioa -= (len(esaldia)-len(sarrera))
        for i in range(len(sarrera)):
            if sarrera[i] != esaldia[i]:
                puntuazioa -= 1
    else:
        print(f"Sekulakoa! Erabilitako denbora: {t}")
    return puntuazioa, t

#main
modua, zailtasuna = menu(0)
puntuazioa = 0
puntuazio_osoa = 0

if modua == "1":
    hitz_kopurua = 5
elif modua == "2":
    hitz_kopurua = input()
for i in range(hitz_kopurua):
    esaldia = esaldia_aukeratu(zailtasuna)
    hasierako_denbora = time.time()
    print(f"Sartu hitza: {esaldia}")
    sarrera = input()
    puntuazio_osoa = puntuazio_osoa + len(esaldia)
    puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
    
print(f"Zure nota: {puntuazioa}/{puntuazio_osoa}")

