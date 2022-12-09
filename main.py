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
    d_has = time.time()
    return esaldia, d_has

def erlojua(hasiera):
    denbosoa = round((time.time() - hasiera), 2)
    time.sleep(1)
    return denbosoa
        
def nota(esaldia, sartua):
    puntuazioa = len(esaldia)
    if sartua != esaldia:
        if len(sartua) < len(esaldia):
            puntuazioa -= (len(esaldia)-len(sartua))
        for i in range(len(sartua)):
            if sartua[i] != esaldia[i]:
                puntuazioa -= 1
    return puntuazioa

#main
modua, zailtasuna = menu(0)
i = 0
e, d = esaldi_aukera(zailtasuna)
sarrera = input()
t = erlojua(d)
p = nota(e, sarrera)

print("Zure nota {} tik: {}".format(len(e),p))
print("Denbora: ", t)
