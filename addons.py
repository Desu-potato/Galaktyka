import dill, math, random
from PIL import Image, ImageDraw, ImageFont


def r(tura):
    a = dill.load(open("zapisy/Galaktykaztury"+str(tura)+".pickle", "rb"))
    return a

def rG():
    a = dill.load(open("zapisy/Galaktyka.pickle", "rb"))
    return a

def Gal1(gal,tura):
    dill.dump(gal, file=open("zapisy/Galaktykaztury"+str(tura)+".pickle", "wb+"))
def Gal(gal):
    dill.dump(gal, file=open("zapisy/Galaktyka.pickle", "wb+"))

class eco:
    def __init__(self,nazwa, pos, sector):
        #Główne statystyki
        self.nazwa = str(nazwa)
        self.position = [sector,pos]
        self.pop = 50
        self.food = 1
        self.energy = 1.1
        self.GDP = 575.735
        self.stab = 0.8
        #Wskaźniki

        self.NGoP = 1.05
        self.NGoG = 1.05
        self.taxR = 5
        self.PoSP = 15
        self.points = 0
        self.zasp = 1
        # Wskaźniki
        self.pm = 0
        self.bm = 0
        self.turaB =0
        self.klucz = True
    def tura(self):
        self.points = self.points + ((self.GDP/10)*(self.zasp)*(self.stab)*(self.energy-1)*(self.pop))*(self.taxR/100)
        self.pm = (self.zasp * 0.5) * self.pop * self.energy-1
        self.bm = self.bm + (self.pm * (self.PoSP/100))
        self.pop = self.pop * self.NGoP * self.food
        self.GDP = self.GDP * self.NGoG
        self.turaB = self.turaB +1
        if(self.turaB >2 and self.klucz == True):
            self.NGoP = self.NGoP - 0.01
            self.NGoG = self.NGoG - 0.01
            if (self.turaB > 2 and self.NGoG < 1):
                self.stab = self.stab - 0.01
            self.turaB = 0

    def pustyszablon(self):
        # Główne statystyki
        self.pop = 0
        self.food = 0
        self.energy = 0
        self.GDP = 0
        self.stab = 0
        # Wskaźniki

        self.NGoP = 0
        self.NGoG = 0
        self.taxR = 0
        self.PoSP = 0
        self.points = 0
        self.zasp = 0
        # Wskaźniki
        self.pm = 0
        self.bm = 0
class imperium:
    def __init__(self, imperium):
        self.wlosci = []
        self.tech = []
        self.impname = str(imperium)
        self.sredStab = 0
        self.NumWlo = 0
        self.point = 0
        self.bud = 0
        self.pop = 0
        self.t = 0
        self.posW = False
    def generuj(self,nazwa,pos,sector):
        self.wlosci.append(eco(nazwa, pos , sector))
    def generujPusty(self,nazwa):
        a = eco(nazwa, [], [])
        a.pustyszablon()
        self.wlosci.append(a)
    def tura(self):
        self.t = self.t+1
        self.point = 0
        self.bud = 0
        self.pop = 0
        self.sredStab = 0
        self.NumWlo = len(self.wlosci)
        for a in self.wlosci:
            a.tura()
            self.point = self.point + a.points
            self.pop = self.pop + a.pop
            self.bud = self.bud + a.bm
            self.sredStab = self.sredStab + a.stab
        self.sredStab = self.sredStab/self.NumWlo
        self.techpodsumuj()

    def usun(self,a):
        self.wlosci.pop(a)

    def techpodsumuj(self):
        for i in self.tech:
            i.summary(0)
    def dodajtech(self,a,b):
        self.tech.append(tech(str(a),int(b)))
    def usuntech(self,a):
        self.tech.pop(a)

    def kluczchange(self,a):
        if(a == 0):
            self.posW = False
        if(a == 1):
            self.posW = True
class tech:
    def __init__(self, name, points):
        self.all = 0
        self.name = str(name);
        self.tier = ""
        self.Tpoints = 0.0
        self.plus = 0
        self.abac = 1.1
        self.ta = 0
        self.summary(int(points))
    def summary(self, points):
        self.ta = self.ta + 1
        self.all = self.all + points
        if self.all>3:
            B = round(math.log(self.all ^ 3) * (self.abac), 2)
            self.plus = round(math.log(self.all ^ 3) * 1.1)
        else:
            B = 0.5
        self.Tpoints = self.Tpoints + B
        if round(self.Tpoints) >= 10 and round(self.Tpoints) < 20:
            self.tier = ("Pierwszy lvl techa")

        elif round(self.Tpoints) >= 20 and round(self.Tpoints) < 40:
            self.tier =("Drugi lvl techa")

        elif round(self.Tpoints) >= 40 and round(self.Tpoints) < 80:
            self.tier =("Trzeci lvl techa")

        elif round(self.Tpoints) >= 80 and round(self.Tpoints) < 160:
            self.tier =("czwarty lvl techa")

        elif round(self.Tpoints) >= 160:
            self.tier =("Piąty lvl techa")
        else:
            self.tier = "Tech tylko koncepcyjny"
class sector:
    def __init__(self,pos):
        #---------------x-----------z----------y
        self.name = random.random()
        self.posNMS = pos
        self.posUWS = []
        self.uk = 0
        self.uszupelnij(7)

    def uszupelnij(self,szansa):
        bufor = 0
        for bloki in range(125):
            one = random.randint(1, szansa)
            two = 2
            if (one == two):
                bufor = bufor + 1
        self.uk = bufor
        i = 0
        for somtin in range(bufor):
            self.posUWS.append([])
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            z = random.randint(0, 4)
            if ([x, y, z] in self.posUWS):
                x = random.randint(0, 4)
                y = random.randint(0, 4)
                z = random.randint(0, 4)
            else:
                pass
            self.posUWS[i].append(x)
            self.posUWS[i].append(y)
            self.posUWS[i].append(z)
            i = i + 1
class map:
    def __init__(self):
        self.fckmap = []
        self.generujwszechswiat()
    def generujwszechswiat(self):
        i = 0
        for y in range(9):
            for x in range(19):
                for z in range(9):
                    self.fckmap.append([])
                    self.fckmap[i].append(x)
                    self.fckmap[i].append(y)
                    self.fckmap[i].append(z)
                    self.fckmap[i].append(sector([x, y, z]))
                    i = i + 1
    def find(self,pos):
        for b in self.fckmap:
            if(b[0] == pos[0] and b[1] == pos[1]and b[2] == pos[2]):
                return self.fckmap.index(b)
class mapasektora:
        def __init__(self, dane):
            self.mapP = None
            self.mapG = None
            self.dane = dane
            self.wyb = 0
            self.stworz()

        def stworz(self):
            x = 1000
            z = 1000
            self.mapP = Image.new('RGB', (x, z), (0, 0, 0),)
            self.mapG = ImageDraw.Draw(self.mapP)

        def wybierz(self, wyb):
            self.wyb = wyb

        def ret(self):
            dane = self.dane
            font = ImageFont.truetype('font.ttf', 48)
            for rzad in range(5):
                x = 600 + 50 * rzad
                for b in range(5):
                    for a in range(5):
                        if (rzad == self.wyb):
                            wait = False
                            for uklad in dane:
                                if (uklad[0] == rzad and uklad[1] == a and uklad[2] == b):
                                    wait = True
                                    break
                            if (wait == True):
                                self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                             (0, 255, 0))
                            else:
                                self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                             (255, 255, 255))
                        elif (rzad > self.wyb):
                            pass
                        else:
                            self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                         (0, 12, 27))
                '''
                if (rzad == 4):
                    y = 900
                    x = 600

                    self.mapG.text((
                        (x, y)
                    ), "x/y/z", font=font)
                '''
            self.mapG.text((100, 100), "Warstwa: " + str(self.wyb), font=font)
            self.mapP.save("test.png")
        def generuj(self, pos, przes, color):
            # [x,y]

            przesunx = przes[0]
            przesuny = przes[1]
            x = pos[0]
            y = pos[1]

            self.mapG.polygon(
                (((x / 2) + przesunx, przesuny),
                 (przesunx, (y * 1 / 4) + przesuny),
                 (przesunx, (y * 3 / 4) + przesuny),
                 ((x / 2) + przesunx, y + przesuny),
                 (x + przesunx, (y * 3 / 4) + przesuny),
                 (x + przesunx, (y * 1 / 4) + przesuny)
                 ),
                fill=(color),
                outline=(0, 0, 0))

        # [x,z,y]
class mapagalaktyki:
    def __init__(self, dane):
        self.mapP = None
        self.mapG = None
        self.dane = dane
        self.wyb = 0
        self.stworz()

    def stworz(self):
        x = 1700
        z = 1500
        self.mapP = Image.new('RGB', (x, z), (0, 0, 0), )
        self.mapG = ImageDraw.Draw(self.mapP)

    def wybierz(self, wyb):
        self.wyb = wyb

    def ret(self):
        dane = self.dane
        font = ImageFont.truetype('font.ttf', 48)
        for rzad in range(19):
            x = 600 + 50 * rzad
            for b in range(9):
                for a in range(9):
                    if (rzad == self.wyb):
                        wait = False
                        for uklad in dane:
                            if (uklad[2] == a and uklad[1] == rzad and uklad[0] == b):
                                wait = True
                                break
                        if (wait == True):
                            self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                         (0, 255, 0))
                        else:
                            self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                         (255, 255, 255))
                    elif (rzad > self.wyb):
                        pass
                    else:
                        self.generuj([100, 100], [x - (50 * a), (x - (50 * b) + (25 * a) - 25 * rzad)],
                                     (0, 12, 27))



        self.mapG.text((100, 100), "Warstwa: " + str(self.wyb), font=font)
        self.mapP.save("test.png")

    def generuj(self, pos, przes, color):
        # [x,y]

        przesunx = przes[0]
        przesuny = przes[1]
        x = pos[0]
        y = pos[1]

        self.mapG.polygon(
            (((x / 2) + przesunx, przesuny),
             (przesunx, (y * 1 / 4) + przesuny),
             (przesunx, (y * 3 / 4) + przesuny),
             ((x / 2) + przesunx, y + przesuny),
             (x + przesunx, (y * 3 / 4) + przesuny),
             (x + przesunx, (y * 1 / 4) + przesuny)
             ),
            fill=(color),
            outline=(0, 0, 0))

    # [x,z,y]
class galaktyka:
    def __init__(self):
        self.imp = []
        self.Mapa = None
        self.inicjuj_galaktyke()
        self.T = 0
    def dodaj_imperium(self, name):
        self.imp.append(imperium(name))

    def usun_imperium(self, num):
        self.imp.pop(num)

    def inicjuj_galaktyke(self):
            main = map()
            self.Mapa = main

    def wylosuj_uklad(self):
            bufor = []
            for uklad in self.Mapa.fckmap:
                if(uklad[3].uk>0):
                    bufor.append(uklad)
            a= len(bufor)-1
            wynik = random.randint(0, a)
            a = self.Mapa.fckmap[wynik]

            wynik = random.randint(0, len(a[3].posUWS)-1)

            b = a[3].posUWS[wynik]
            print(b)
            print(a[3].posNMS)
            return [a[3].posNMS,b]

