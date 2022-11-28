#Infor proiektua
import random
def menu(turno):
    if turno == 0:
        print("Ongi etorri...")
    else:
        print("Jokatzen...")
    modua = input(""" """)
    zail = input(""" """)
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
    h = libu[r]
    print(h)
    return h
    
#     if zail == 1:
#         r = random.randint(0, len(libu1))
#         h = libu1[r]
#     elif zail == 2:
#         r = random.randint(0, len(libu2))
#         h = libu2[r]
#     else:
#         r = random.randint(0, len(libu3))
#         h = libu3[r]
    

def sarrera(h):
    for i in range(len(h)):
        print("_",end="")
    print("\r")
    for i in range(len(h)):
        input()
        
modua, zailtasuna = menu(0)
h = esaldi_aukera(zailtasuna)
sarrera(h)
