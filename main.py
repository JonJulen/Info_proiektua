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

def esaldi_aukera(zail):
    print()
    libu = []
    libu1 = ["Kaixo"]
    libu2 = ["Egun on"]
    libu3 = ["Arratsalde on"]
    if zail == '1':
        libu = libu1
    elif zail == '2':
        libu = libu2
    elif zail == '3':
        libu = libu3
    esaldia = libu[0]
    print(esaldia)
    return esaldia

def nehurtu_erabilitako_denbora(hasiera):
  return time.perf_counter() - hasiera
        
def nota(esaldia, sarrera, hasiera):
    puntuazioa = puntuazioa + len(esaldia)
    puntuazioa_osoa = puntuazioa_osoa + len(esaldia)
    if sartua != esaldia:
        if len(sarrera) < len(esaldia):
            puntuazioa -= (len(esaldia)-len(sarrera))
        for i in range(len(sarrera)):
            if sarrera[i] != esaldia[i]:
                puntuazioa -= 1
    else:
        t = nehurtu_erabilitzako_denbora(hasiera)
    return puntuazioa, puntuazioa_osoa

#main
modua, zailtasuna = menu(0)
if modua == "1":
    hitz_kopurua = 5;
    for i in range(hitz_kopurua):
        esaldia = esaldia_aukeratu()
        print(f"Sartu hitza: {esaldia}")
        sarrera = input()
        hasierako_denbora = time.perf_counter()
        puntuazioa, puntuazioa_osoa = nota(esaldia, sarrera, hasierako_denbora)
        
    print(f"Zure nota: {puntuazioa}/{puntuazioa_osoa}")

