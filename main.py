#Infor proiektua: Mekanografia jokua

#Func:
import random
def menu(turno):
    if turno == 0:
        print("Ongi etorri...")
    else:
        print("Jokatzen...")
    modua = input(""" Modua: """)
    zail = input(""" Zailtasuna: """)
    return modua, zail

def esaldi_aukera(zail):
    print(zail)
    libu = []
    libu1 = ["Kaixo"]
    libu2 = ["Egun on"]
    libu3 = ["Arratsalde on"]
    if zail == 1:
        libu = libu1
    elif zail == 2:
        libu = libu2
    elif zail == 3:
        libu = libu3
    r = random.randint(0, len(libu)-1)
    esaldia = libu[r]
    print(esaldia)
    return esaldia
    
#     if zail == 1:
#         r = random.randint(0, len(libu1))
#         h = libu1[r]
#     elif zail == 2:
#         r = random.randint(0, len(libu2))
#         h = libu2[r]
#     else:
#         r = random.randint(0, len(libu3))
#         h = libu3[r]
    

def sarrera(esaldia):
    for i in range(len(esaldia)):
        print("_",end="")
    print("\r")
    for i in range(len(esaldia)):
        input()
        
modua, zailtasuna = menu(0)
h = esaldi_aukera(zailtasuna)
sarrera(h)
