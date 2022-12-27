#Infor proiektua: Mekanografia jokua

#mod:
import random
import time

#func
def menu(turno):
    if turno == 0:
        print("""
Ongi etorri mekanografia testera
Ondoren, jokatzeko modua eta esaldien zailtasuna hautatuko duzu
""")
    else:
        berriz=input("Jokatzeko modua zein zailtasuna aldatu nahi duzu? b/e")
        if berriz == 'b':
            modua = input("""
Moduak:
1| 5 esaldi
2| Hitz kopuru aukeratua
3| Denbora aukeratua
Aukeratu modua:
""")
            zail = int(input("""
Zailtasuna | 1 | 2 | 3 | :
"""))
    modua = input("""
Moduak:
1| 5 esaldi
2| Hitz kopuru aukeratua
3| Denbora aukeratua
Aukeratu modua:
""")
    zail = int(input("""
Zailtasuna | 1 | 2 | 3 | :
"""))
    return modua, zail

def esaldia_aukeratu(zail):
    libu = []
    libu1 = ["Egun on Euskal Herria","Zer moduz","Hik lan eta nik jai"]
    libu2 = ["Akerrak adarrak okerrak ditu","Aldapeko sagarraren adarraren puntan","Zozoak beleari ipurbeltz"]
    libu3 = ["Bederatziehun eta laurogeita hemeretzi mila bederatziehun eta laurogeita hemeretzi","Superkalifragilistikoespialidoso","Mikelezizanmaltzurralanhandiaegundugu"]
    if zail == 1:
        libu = libu1
    elif zail == 2:
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
        elif len(sarrera) > len(esaldia):
            puntuazioa -= (len(sarrera) - len(esaldia))
            sarrera = sarrera[0:len(esaldia)]
        for i in range(len(sarrera)):
            if sarrera[i] != esaldia[i]:
                puntuazioa -= 1
    else:
        print(f"Sekulakoa! Erabilitako denbora: {t}")
    return puntuazioa, t

def mezua(puntuazioa, puntuazioa_osoa, denbora):
    r = round((puntuazioa/5)/(denbora/60))
    if r < 24:
        print(f"Zure HM (hitzak minutuko) 24 baino baxuagoa da, zehazki {r}, gehio praktika beharko zenuke")
    elif 24 < r < 32:
        print(f"Zure HM (hitzak minutuko) 24 eta 32 bitartean dago, zehazki {r}, abiadura ertaina")
    elif 32 < r < 52:
        print(f"Zure HM (hitzak minutuko) 32 eta 52 bitartean dago, zehazki {r}, oso ona!!")
    elif 52 < r < 70:
        print(f"Zure HM (hitzak minutuko) 52 eta 70 bitartean dago, zehazki {r}, mekanografian jantzia")
    elif 70 < r < 80:
        print(f"Zure HM (hitzak minutuko) 70 eta 80 bitartean dago, zehazki {r}, paregabea, bikaina")
    elif 80 < r:
        print(f"Zure HM (hitzak minutuko) 80 baino altuagoa da, zehazki {r}, robota ote?")
#main
aukera = "b"
turno = 0
while aukera == "b":
    modua, zailtasuna = menu(turno)
    puntuazioa = 0
    puntuazio_osoa = 0
    denbora_totala = 0
    
    if modua == "1":
        hitz_kopurua = 5
        for i in range(hitz_kopurua):
            esaldia = esaldia_aukeratu(zailtasuna)
            hasierako_denbora = time.time()
            print(f"Sartu hitza: {esaldia}")
            sarrera = input()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            denbora_totala += denbora
            
    elif modua == "2":
        hitz_kopurua = int(input("Zenbat hitz sartu nahi dituzu?: "))
        for i in range(hitz_kopurua):
            esaldia = esaldia_aukeratu(zailtasuna)
            hasierako_denbora = time.time()
            print(f"Sartu hitza: {esaldia}")
            sarrera = input()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            denbora_totala += denbora
            
    elif modua == "3":
        geratzen_denbora = int(input("Sartu nahi duzun denbora segundutan: "))
        denbora_totala = geratzen_denbora
        while geratzen_denbora > 0:
            esaldia = esaldia_aukeratu(zailtasuna)
            hasierako_denbora = time.time()
            print(f"Sartu hitza: {esaldia}")
            sarrera = input()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            geratzen_denbora -= denbora
            print(f"Geratzen zaizun denbora: {round(geratzen_denbora, 2)}")
            
    print(f"Zure nota: {puntuazioa}/{puntuazio_osoa}")
    mezua(puntuazioa, puntuazio_osoa, denbora_totala)
    turno += 1
    aukera = input("Berriz jolastu?(b/e): ")
