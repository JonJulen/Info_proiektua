#Infor proiektua: Mekanografia jokua || Patxi Bueno eta Jon Julen Weyndling

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
        berriz=input("Jokatzeko modua zein zailtasuna aldatu nahi duzu?(b/e): ")
        marra_lerroa()
        if berriz != 'b':
            modua = azkeneko_modua
            zail = azkeneko_zailtasuna
            return modua, zail
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
    print()
    return modua, zail
    
def liburutegia_aukeratu(zail):
    libu = []
    auxlibu = []
    libu1 = ["Egun on Euskal Herria","Gezurrak buztana labur","Hik lan eta nik jai", "Hoi dek sasoia", "Non gogoa han zangoa", "Goiz gorri arrats euri", "Geroa alferraren leloa", "Su gaberik ez da kerik","Ezinak ez du legerik","Zer ikusi, hura ikas"]
    libu2 = ["Akerrak adarrak okerrak ditu", "Aldapeko sagarraren adarraren puntan", "Zozoak beleari ipurbeltz", "Azaroa bero, negua gero", "Eguzkia nora zapiak hara", "Bururik ez eta txapela nahi","Haurrak hazi nekeak bizi","Umearen zentzuna, etxean entzuna","Ogi gogorrari hagin zorrotz","A ze parea karakola eta barea"]
    libu3 = ["Urrutiko intxaurrak hamalau, bertara joan eta lau","Superkalifragilistikoespialidoso","Mikel ez izan maltzurra lan handia egun dugu", "Afaldu nahi ez duenaren afaria beti prest", "Abenduko eguna, argitu orduko iluna","Elur-melur ez naiz zure beldur, badut etxean arto eta egur","Txapelik handienak ez du buru hutsik betetzen","Bururik nekatzen ez duenak, hankak nekatu behar","Txapelik handienak ez du buru hutsik betetzen"]
    if zail == 1:
        libu = libu1.copy()
        auxlibu = libu1.copy()
    elif zail == 2:
        libu = libu2.copy()
        auxlibu = libu2.copy()
    elif zail == 3:
        libu = libu3.copy()
        auxlibu = libu3.copy()
    return libu, auxlibu

def esaldia_aukeratu(libu, auxlibu):
    if len(libu) == 0:
        libu = auxlibu.copy()
    esaldia = random.choice(libu)
    libu.remove(esaldia)
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

def mezua(puntuazioa, denbora):
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
        
def marra_lerroa():
    print("-"*40)
    
#main
aukera = "b"
turno = 0
azkeneko_modua = 0
azkeneko_zailtasuna = 0
while aukera == "b":
    modua, zailtasuna = menu(turno)
    liburutegia, aux_liburutegia = liburutegia_aukeratu(zailtasuna)
    azkeneko_modua = modua
    azkeneko_zailtasuna = zailtasuna
    puntuazioa = 0
    puntuazio_osoa = 0
    denbora_totala = 0
    sartutako_hitzak = 0
    
    if modua == "1":
        hitz_kopurua = 5
        for i in range(hitz_kopurua):
            esaldia = esaldia_aukeratu(liburutegia, aux_liburutegia)
            hasierako_denbora = time.time()
            marra_lerroa()
            print(f"Sartu hitza: {esaldia}")
            marra_lerroa()
            sarrera = input()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            denbora_totala += denbora
            
    elif modua == "2":
        hitz_kopurua = int(input("Zenbat hitz sartu nahi dituzu?: "))
        for i in range(hitz_kopurua):
            esaldia = esaldia_aukeratu(liburutegia, aux_liburutegia)
            hasierako_denbora = time.time()
            marra_lerroa()
            print(f"Sartu hitza: {esaldia}")
            marra_lerroa()
            sarrera = input()
            print()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            denbora_totala += denbora
            
    elif modua == "3":
        geratzen_denbora = int(input("Sartu nahi duzun denbora segundutan: "))
        denbora_totala = geratzen_denbora
        while geratzen_denbora > 0:
            esaldia = esaldia_aukeratu(liburutegia, aux_liburutegia)
            hasierako_denbora = time.time()
            marra_lerroa()
            print(f"Sartu hitza: {esaldia}")
            marra_lerroa()
            sarrera = input()
            sartutako_hitzak += 1
            print()
            puntuazio_osoa = puntuazio_osoa + len(esaldia)
            puntuazioa, denbora = nota(esaldia, puntuazioa, sarrera, hasierako_denbora)
            geratzen_denbora -= denbora
            print(f"Geratzen zaizun denbora: {round(geratzen_denbora, 2)}")
            print(f"Orain arte sarturiko hitzak: {sartutako_hitzak}")
            
    print(f"Zehaztasuna: {puntuazioa}/{puntuazio_osoa}")
    mezua(puntuazioa, denbora_totala)
    turno += 1
    marra_lerroa()
    aukera = input("Berriz jolastu?(b/e): ")
    marra_lerroa()
    azkeneko_modua = modua
    azkeneko_zailtasuna = zailtasuna 
