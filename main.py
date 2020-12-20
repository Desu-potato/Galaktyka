import discord, addons, asyncio
from discord.ext import commands

master = commands.Bot(command_prefix='/Gal.')

main = addons.galaktyka()


@master.event
async def on_ready():
    print('Żyje')
@master.event
async def on_command_error(ctx, error):
        await ctx.send("Błąd komendy")
        print(error)
        await asyncio.sleep(5)
        await clear(ctx, 2)
@master.command(name="PS")
@commands.has_role("GM")
async def PanelSterowania(ctx):
    a = '''**Panel Sterowania**```Małe zasady:
!- Komendy specialne, należy na nie uważać.
Dane po przecinku należy wprowadzać z kropką
Komend nie powinnno się używać poza panelami sterowania.
Czas na wpisanie informacji, po wywołaniu komendy to około 30 sekund
Pomocnicze:
    -/Gal.PS - Zwykły Panel Sterowania
    -/Gal.Imperia - Wyświetla wszystkie aktualne imperia
    -/Gal.clear (arg liczbowy) - Komenda do czyszczenia chatów
    -/Gal.ImperiumMajątek - Komenda do wyświetleniaogólnie
     wskaźników do danej planety. (Szybkie)
    -/Gal.pokazsektorGM- Komenda do wyświetlenia zawartości sektora bez tajemnicy
    -/Gal.pokazsektor (Warstwa)- generuje mapę sektora z zaznaczoną pozycją
    -/Gal.pokazwszechswiat - generuje mapę wszechświata z zanaczonym punktem
Komendy Główne:
    -/Gal.Tech - Główna komenda do edycji techów i ich dodawnaia
    -/Gal.Majątekedytuj - Główna komenda do edycji zawartości imperiów
Komendy do tury:
    -/Gal.StwórzturęImperium - Generuje wszystkie informacje
     o danym imperium dla gracza
    -/Gal.TuraWrzechświata - Globalna tura
    -/Gal.DodajImperium (arg) - Komenda do dodawania imperium
    -/Gal.TuraImperium! - Przeskoczenie tury u danego imperium
    -/Gal.UsunImperium (arg liczbowy) - Komenda do usuwania imperiów
    -/Gal.Wylosujuklad - Losuje losowy sektor, i miejsce w nim
     w którym znajduje się układ
    -/Gal.Zmiananazwy - Zmiana nazwy imperium
    -/Gal.Dodajwłość - Dodaj zabudowany glob, z standardową ekonomią
    -/Gal.Dodajpustąwłość - template kolonialny/stacji
Komendy bazowe:
    -/Gal.Zapis! - Zapis zmian w danej turze.
    *Komenda zapisuje aktualne zmiany w obiekcie galaktyki.
     Uważać jak cholera, bo będę musiał przywracać archiwum
    -/Gal.Wczytaj! - Wczytanie bazy na wypadek gdyby bot się zresetował
Komendy programisty(Niedostępne dla GM, to archiwum):
    -/Gal.Wczytaj!G (Ture)
    -/Gal.Zapis!G - Zapis turowego obiektu
    ```'''
    await ctx.send(a)



@master.command(name="Imperia")
@commands.has_role("GM")
async def PokazImperia(ctx):
    i = 0

    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    mess = "Z kosmosu wydobywają się dźwięki:``` "
    try:
        for a in main.imp:
            i = i + 1
            mess = mess + str(a.impname) + " : " + str(i) + "\n"
        mess = mess + "```"
    except discord.Forbidden:
        mess = "Galaktyka jest pusta"
    await ctx.send(mess)
    await ctx.send("-Wyślij cokolwiek by kontynuować")
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 3)
    else:
        await clear(ctx, 3)


@master.command(name="DodajImperium")
@commands.has_role("GM")
async def DodajImperium(ctx, x):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    main.dodaj_imperium(x)
    await ctx.send("Dodano: " + x + " -Wyślij cokolwiek by kontynuować")
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)


@master.command(name="UsunImperium")
@commands.has_role("GM")
async def usun(ctx, x):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    main.usun_imperium(x)
    await ctx.send("Usunięto: " + x + " -Wyślij cokolwiek by kontynuować")
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)


@master.command()
@commands.has_role("GM")
async def clear(etx, amount):
    await etx.channel.purge(limit=int(amount))


@master.command(name="ImperiumMajątek")
@commands.has_role("GM")
async def cheak1(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content)
        await clear(ctx, 20)
        i = 0
        mess = "``` "
        for a in main.imp[int(x - 1)].wlosci:
            i = i + 1
            mess = mess + str(a.nazwa) + " : " + str(i) + "\n"
        mess = mess + "```"
        await ctx.send("Wybierz włość: " + mess)
        msg = await master.wait_for('message', check=check, timeout=30)
        if ((msg.content).isnumeric()):
            b = int(msg.content)
            await clear(ctx, 20)
            a = vars(main.imp[int(x - 1)].wlosci[b - 1])
            mess = "``` "
            for b, c in a.items():
                mess = mess + str(b) + " : " + str(c) + " \n"
            mess = mess + "```"
            await ctx.send("Ekonomia:" + mess)
            msg = await master.wait_for('message', check=check, timeout=30)
            if msg == True:
                await clear(ctx, 20)
            else:
                await clear(ctx, 20)


@master.command(name="Majątekedytuj")
@commands.has_role("GM")
async def somting(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    def gotu(a):
        bufor = []
        for x in a:
            if (x.isnumeric() or x == "," or x == " "):
                bufor.append(x)
            else:
                pass
        bufor2 = ''
        for x in bufor:
            if x.isnumeric():
                bufor2 = bufor2 + x
            else:
                bufor2 = bufor2 + " "
        bufor = []
        for x in bufor2.split():
            bufor.append(int(x))
        return bufor

    def sum(x, planeta):
        wlosc = main.imp[int(x - 1)].wlosci[planeta]
        mess = ">        **Nazwa: **" + str(wlosc.nazwa) + "\n"
        mess = mess + "Klucz degeneracji: " + str(wlosc.klucz) + "\n"
        mess = mess + "Wskaźniki: " + "\n"
        mess = mess + "```-GDP: " + str(round(wlosc.GDP)) + " Tysiace milionów" + "\n"
        mess = mess + "-Budulec pozyskany w tej turze: " + str(round(wlosc.pm * (wlosc.PoSP/100)))
        mess = mess + "-Produkcja budulca całoprzemysłowo:" + str(round(wlosc.pm)) + "Mt/t" + "\n"
        mess = mess + "-Naturalny wzrost gospodarki: " + str(round((wlosc.NGoG - 1) * 100)) + "%" + "\n"
        mess = mess + "-Naturalny wzrost populacji: " + str(round((wlosc.NGoP - 1) * 100)) + "%" + "\n"
        mess = mess + "-Stabilność: " + str(wlosc.stab * 100) + "%" + "\n"
        mess = mess + "-Podatki: " + str(wlosc.taxR) + "%" + "\n"
        mess = mess + "-Rezerwa narodowa materiałowa: " + str(wlosc.PoSP) + "%" + "\n"
        mess = mess + "```\n"
        mess = mess + "Zasoby:\n"
        mess = mess + "```"
        mess = mess + "Punkty: " + str(round(wlosc.points)) + "\n"
        mess = mess + "Pop: " + str(round(wlosc.pop)) + "Milionów" + "\n"
        mess = mess + "Magazyn-Budulca:" + str(round(wlosc.bm)) + "Mt" + "\n"
        mess = mess + "Żywność: " + str(wlosc.food * 100) + "% zaspokojonia" + "\n"
        mess = mess + "Zasoby planety: " + str(wlosc.zasp) + "\n"
        mess = mess + "Produkcja energii:" + str(wlosc.energy) + "0 SPE" + "\n"
        mess = mess + "```\n"
        mess = mess + "Współrzędne:\n"
        mess = mess + "```"
        mess = mess + "Sektor: " + str(wlosc.position[0]) + "\n"
        mess = mess + " Pozycja w sektorze: " + str(wlosc.position[1]) + "\n"
        mess = mess + "```\n"
        return mess
    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content)
        await clear(ctx, 20)
        i = 0
        mess = "``` "
        for a in main.imp[int(x - 1)].wlosci:
            i = i + 1
            mess = mess + str(a.nazwa) + " : " + str(i) + "\n"
        mess = mess + "```"
        await ctx.send("Wybierz włość: numer " + mess)
        msg = await master.wait_for('message', check=check, timeout=30)
        planeta = int(msg.content) - 1
        if ((msg.content).isnumeric() and int(msg.content) <= len(main.imp[int(x - 1)].wlosci)):
            await ctx.send(sum(x,planeta))
            await ctx.send("Komenda? Zasoby, Wskaźniki, Współrzędne, Podstawowe")
            buf = await master.wait_for('message', check=check, timeout=30)
            komenda = buf.content
            if komenda.lower() == "zasoby":
                await clear(ctx, 2)

                buf = ""
                await ctx.send("Punkty: "+ str(round(main.imp[int(x - 1)].wlosci[planeta].points))+"\n"+"Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].points = float(komenda)

                buf = ""
                await ctx.send("Populacja: " + str(round(main.imp[int(x - 1)].wlosci[planeta].pop))+ "\nPominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                        await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].pop = float(komenda)


                buf = ""
                await ctx.send("Budulec Magazyn: " + str(round(main.imp[int(x - 1)].wlosci[planeta].bm)) + " MT\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].bm = float(komenda)

                buf = ""
                await ctx.send("Pożywienie: " + str((main.imp[int(x - 1)].wlosci[planeta].food)) + " \n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].food = float(komenda)
                buf = ""
                await ctx.send("Zasoby planety: " + str(round(main.imp[int(x - 1)].wlosci[planeta].zasp,2)) + " \n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].zasp = float(komenda)
                buf = ""
                await ctx.send("Energia Globu: " + str(round(main.imp[int(x - 1)].wlosci[planeta].energy,2)) + " SPE(rly)\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].energy = float(komenda)

                await ctx.send("Pomyślnie zakończono komende")
                await asyncio.sleep(5)
                await clear(ctx, 20)
                #praca
            elif komenda.lower() == "wskaźniki" or komenda.lower() == "wskazniki":

                await clear(ctx, 2)
                await ctx.send("GDP: " + str((main.imp[int(x - 1)].wlosci[planeta].GDP)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].GDP = float(komenda)

                await ctx.send("Naturalny wzrost gospodarki: " + str((main.imp[int(x - 1)].wlosci[planeta].NGoG)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].NGoG = float(komenda)

                await ctx.send("Naturalny wzrost populacji: " + str((main.imp[int(x - 1)].wlosci[planeta].NGoP)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].NGoP = float(komenda)

                await ctx.send("Stab: " + str((main.imp[int(x - 1)].wlosci[planeta].stab)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].stab = float(komenda)

                await ctx.send("Tax: " + str((main.imp[int(x - 1)].wlosci[planeta].taxR)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].taxR = float(komenda)

                await ctx.send("Rezerwa: " + str((main.imp[int(x - 1)].wlosci[planeta].PoSP)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    main.imp[int(x - 1)].wlosci[planeta].PoSP = float(komenda)
                await ctx.send("Pomyślnie zakończono komende")
                await asyncio.sleep(5)
                await clear(ctx, 20)
            elif komenda.lower() == "współrzędne" or komenda.lower() == "wspolrzedne":
                await clear(ctx, 2)
                await ctx.send("Sektor: " + str((main.imp[int(x - 1)].wlosci[planeta].position[0])) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    buf = gotu(buf.content)
                    main.imp[int(x - 1)].wlosci[planeta].position[0] = buf
                await ctx.send("Sektor: " + str((main.imp[int(x - 1)].wlosci[planeta].position[1])) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    await clear(ctx, 1)
                else:
                    buf = gotu(buf.content)
                    main.imp[int(x - 1)].wlosci[planeta].position[1] = buf
                await ctx.send("Pomyślnie zakończono komende")
                await asyncio.sleep(5)
                await clear(ctx, 10)
            elif komenda.lower() == "podstawowe":
                await clear(ctx, 2)
                await ctx.send("Nazwa: " + str((main.imp[int(x - 1)].wlosci[planeta].nazwa)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    pass
                else:
                    main.imp[int(x - 1)].wlosci[planeta].nazwa = str(komenda)
                await ctx.send("Klucz degeneracji: " + str((main.imp[int(x - 1)].wlosci[planeta].klucz)) + "\n" + "Pominąć? Pomiń/Pomin/pom - zamiast wartości (1-Włączony, 0- wyłączony)")
                buf = await master.wait_for('message', check=check, timeout=30)
                komenda = buf.content
                if komenda.lower() == "pom" or komenda.lower() == "pomin" or komenda.lower() == "pomiń":
                    pass
                else:
                    if komenda.isnumeric() and int(komenda) == 1:
                        main.imp[int(x - 1)].wlosci[planeta].klucz = True
                    elif komenda.isnumeric() and int(komenda) == 0:
                        main.imp[int(x - 1)].wlosci[planeta].klucz = False
                    else:
                        await ctx.send("Nic nie zmieniono")


                await ctx.send("Pomyślnie zakończono komende")
                await asyncio.sleep(5)
            else:
                await clear(ctx, 20)
                await ctx.send("Pominięto wszystko")
                await asyncio.sleep(5)
                await clear(ctx, 2)
        else:
            await ctx.send("Złe dane, komenda kończy działanie.")


@master.command(name="TuraWrzechświata")
@commands.has_role("GM")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    for a in main.imp:
        a.tura()
    main.T = main.T + 1
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)


@master.command(name="Zapis!G")
@commands.has_role("Programiści")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a
    addons.Gal1(main, int(main.T))

    await ctx.send("Dodano")
    await asyncio.sleep(5)
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)

@master.command(name="Zapis!")
@commands.has_role("GM")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a
    addons.Gal(main)
    await ctx.send("Dodano")
    await asyncio.sleep(5)
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)

@master.command(name="Wczytaj!")
@commands.has_role("GM")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    global main
    main = addons.rG()
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)

@master.command(name="Wczytaj!G")
@commands.has_role("Programiści")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    global main
    await ctx.send("Która tura?")
    msg = await master.wait_for('message', check=check, timeout=30)
    buf = msg.content
    if buf.isnumeric() :
        main = addons.r(int(buf))
        await ctx.send("Wczytano")
    msg = await master.wait_for('message', check=check, timeout=30)
    if msg == True:
        await clear(ctx, 20)
    else:
        await clear(ctx, 20)


@master.command(name="StwórzturęImperium")
@commands.has_role("GM")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "Które imperium?``` "
    try:
        for a in main.imp:
            i = i + 1
            mess = mess + str(a.impname) + " : " + str(i) + "\n"
        mess = mess + "```"
    except discord.Forbidden:
        mess = "Galaktyka jest pusta"
    await ctx.send(mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    await clear(ctx, 20)
    x = int(msg.content) - 1
    if (((msg.content).isnumeric())):
        a = int(msg.content) - 1
        for tech in main.imp[a].tech:
            mess = "```"
            mess = mess + str(tech.name) + " : Nazwa badania" + "\n"
            mess = mess + tech.tier + " : Poziom zawansowania badań" + "\n"
            mess = mess + str(tech.all) + " : Ilość przeznaczonych środków ogólnie" + "\n"
            mess = mess + str(round(tech.Tpoints, 2)) + " : pkt Aktualny progres badań" + "\n"
            mess = mess + str(tech.plus) + " : dodatek do rzutu na powiązane z techem" + "\n"
            mess = mess + "```"
            await ctx.send(mess)
        mess = "```"
        b = main.imp[a]
        mess = mess + "Tura: " + str(b.t) + "\n"
        mess = mess + "Nazwa imperium: " + str(b.impname) + "\n"
        mess = mess + "Liczba planet i księżyców lub stacji pod nadzorem: " + str(b.NumWlo) + "\n"
        mess = mess + "Średnia stabilność imperium: " + str(round(b.sredStab, 1)) + "\n"
        mess = mess + "Dochód skarbu państwa: " + str(round(b.point)) + "\n"
        mess = mess + "Populacja imperium: " + str(round(b.pop)) + "m" + "\n"
        mess = mess + "Produkcja rezerwy państwowej " + str(round(b.bud)) + "\n"
        mess = mess + "```"
        await ctx.send(mess)
        for wlosc in main.imp[x].wlosci:
            mess = "```"
            if(main.imp[x].posW):
                mess = mess + "Sektor: " + str(wlosc.position[0]) + "\n"
            else:
                mess = mess + "Sektor: " + "[?,?,?]"
            mess = mess + " Pozycja w sektorze: " + str(wlosc.position[1]) + "\n"
            mess = mess + "Nazwa: " + str(wlosc.nazwa) + "\n"
            mess = mess + "GDP: " + str(round(wlosc.GDP)) + " Tysiace milionów" + "\n"
            mess = mess + "Żywność: " + str(round(wlosc.food * 100)) + "% zaspokojonia" + "\n"
            mess = mess + "Zasoby planety: " + str(wlosc.zasp) + "\n"
            mess = mess + "Produkcja energii:" + str(wlosc.energy) + "00 SPE" + "\n"
            mess = mess + "Produkcja budulca całoprzemysłowo:" + str(round(wlosc.pm)) + "Mt/t" + "\n"
            mess = mess + "Budulec pozyskany:" + str(round(wlosc.bm)) + "Mt" + "\n"
            mess = mess + "Pop: " + str(round(wlosc.pop)) + " Milionów" + "\n"
            mess = mess + "Naturalny wzrost gospodarki: " + str(round((wlosc.NGoG - 1) * 100)) + "%" + "\n"
            mess = mess + "Naturalny wzrost populacji: " + str(round((wlosc.NGoP - 1) * 100)) + "%" + "\n"
            mess = mess + "Punkty: " + str(round(wlosc.points)) + "\n"
            mess = mess + "Stabilność: " + str(wlosc.stab * 100) + "%" + "\n"
            mess = mess + "Podatki: " + str(wlosc.taxR) + "%" + "\n"
            mess = mess + "Rezerwa narodowa materiałowa: " + str(wlosc.PoSP) + "%" + "\n"
            mess = mess + "```"
            await ctx.send(mess)


@master.command(name="Tech")
@commands.has_role("GM")
async def cheak21(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "Które imperium?``` "
    try:
        for a in main.imp:
            i = i + 1
            mess = mess + str(a.impname) + " : " + str(i) + "\n"
        mess = mess + "```"
    except discord.Forbidden:
        mess = "Galaktyka jest pusta"
    await ctx.send(mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    wybor = int(msg.content) - 1
    await clear(ctx, 20)
    await ctx.send("Komendy: Dodaj,edytuj,usuń")
    msg = await master.wait_for('message', check=check, timeout=30)
    abc = msg.content
    await clear(ctx, 20)
    b = main.imp[wybor]
    if (abc.lower() == "dodaj"):
        await ctx.send("Nazwa techa")
        test = await master.wait_for('message', check=check, timeout=30)
        await ctx.send("Fundusze")
        test1 = await master.wait_for('message', check=check, timeout=30)
        b.dodajtech(test.content, test1.content)
        await clear(ctx, 20)
    if (abc.lower() == "edytuj"):
        mess = "Który tech: ```"
        i = 0
        for a in b.tech:
            i = i + 1
            mess = mess + a.name + str(i) + "\n"
        mess = mess + "```"
        await ctx.send(mess)
        tech = await master.wait_for('message', check=check, timeout=30)

        if (tech.content.isnumeric()):
            a = int(tech.content) - 1
            await ctx.send("Nazwa: " + b.tech[a].name)
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].name = str(msg.content)
            await clear(ctx, 20)

            await ctx.send("Środki przeznaczone, wersja zamieniania: " + str(b.tech[a].all))
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].all = int(msg.content)
            await clear(ctx, 20)

            await ctx.send("Środki przeznaczone, wersja dodawalna: " + str(b.tech[a].all))
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].all = b.tech[a].all + int(msg.content)
            await clear(ctx, 20)

            await ctx.send("Progres, wersja zamienna: " + str(b.tech[a].Tpoints))
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].Tpoints = float(msg.content)
            await clear(ctx, 20)

            await ctx.send("Progres, wersja dodawalna: " + str(b.tech[a].Tpoints))
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].Tpoints = b.tech[a].Tpoints + float(msg.content)
            await clear(ctx, 20)

            await ctx.send("Mnożnik progresu: " + str(b.tech[a].abac))
            await ctx.send("Jeśli pominąć, zamiast wartości: Tak")
            msg = await master.wait_for('message', check=check, timeout=30)
            if ((msg.content).lower() == 'tak'):
                pass
            else:
                b.tech[a].abac = float(msg.content)
            await clear(ctx, 20)
    if (abc.lower() == "usuń"):
        mess = "Który tech: ```"
        i = 0
        for a in b.tech:
            i = i + 1
            mess = mess + a.name + str(i) + "\n"
        mess = mess + "```"
        await ctx.send(mess)
        test = await master.wait_for('message', check=check, timeout=30)
        b.usuntech(int(test.content))
        await ctx.send("Usunięto")
        await clear(ctx, 20)


@master.command(name="Dodajpustąwłość")
@commands.has_role("GM")
async def somting(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a
    def gotu(a):
        bufor = []
        for x in a:
            if (x.isnumeric() or x == "," or x == " "):
                bufor.append(x)
            else:
                pass
        bufor2 = ''
        for x in bufor:
            if x.isnumeric():
                bufor2 = bufor2 + x
            else:
                bufor2 = bufor2 + " "
        bufor = []
        for x in bufor2.split():
            bufor.append(int(x))
        return bufor
    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content)-1
        await clear(ctx, 20)
        await ctx.send("Nazwa włości")
        msg = await master.wait_for('message', check=check, timeout=30)
        main.imp[x].generujPusty(str(msg.content))
        await clear(ctx, 20)
        await ctx.send("Dodano")
        await asyncio.sleep(5)
        await clear(ctx, 20)


@master.command(name="Dodajwłość")
@commands.has_role("GM")
async def somting(ctx):

    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a
    def gotu(a):
        bufor = []
        for x in a:
            if (x.isnumeric() or x == "," or x == " "):
                bufor.append(x)
            else:
                pass
        bufor2 = ''
        for x in bufor:
            if x.isnumeric():
                bufor2 = bufor2 + x
            else:
                bufor2 = bufor2 + " "
        bufor = []
        for x in bufor2.split():
            bufor.append(int(x))
        return bufor

    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content) - 1
        await clear(ctx, 20)
        await ctx.send("Nazwa włości")
        nazwa = await master.wait_for('message', check=check, timeout=30)
        await ctx.send("Sektor")
        msg = await master.wait_for('message', check=check, timeout=30)
        sektor = gotu(msg.content)
        await ctx.send("Pozycja w sektorz")
        msg = await master.wait_for('message', check=check, timeout=30)
        sektorP = gotu(msg.content)
        main.imp[x].generuj(str(nazwa.content), sektorP,sektor)
        await ctx.send("Dodano")
        await asyncio.sleep(5)
        await clear(ctx, 20)

@master.command(name="TuraImperium!")
@commands.has_role("GM")
async def somting(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content) - 1
        main.imp[x].tura()
        await asyncio.sleep(5)
        await clear(ctx, 20)

@master.command(name="Turawlosci!")
@commands.has_role("GM")
async def somting(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content) - 1
        main.imp[x].tura()
        await asyncio.sleep(5)
        await clear(ctx, 20)





@master.command(name="Zmiananazwy")
@commands.has_role("GM")
async def somting(ctx):
    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    i = 0
    mess = "``` "
    for a in main.imp:
        i = i + 1
        mess = mess + str(a.impname) + " : " + str(i) + "\n"
    mess = mess + "```"
    await ctx.send("Wybierz Imperium " + mess)
    msg = await master.wait_for('message', check=check, timeout=30)
    if ((msg.content).isnumeric()):
        x = int(msg.content) - 1
        await ctx.send("Nazwa: " + str(main.imp[x].impname))
        msg = await master.wait_for('message', check=check, timeout=30)
        main.imp[x].impname = str(msg.content)
        await asyncio.sleep(5)
        await clear(ctx, 20)

@master.command(name="Wylosujuklad")
@commands.has_role("GM")
async def somting(ctx):
        await clear(ctx, 20)
        dane = main.wylosuj_uklad()
        await ctx.send("Sektor x,y,z | PodSektor: x, y, z\n"+str(dane))

@master.command(name="pokazsektorGM")
@commands.has_role("GM")
async def somting(ctx):
        def gotu(a):
            bufor = []
            for x in a:
                if (x.isnumeric() or x == "," or x == " "):
                    bufor.append(x)
                else:
                    pass
            bufor2 = ''
            for x in bufor:
                if x.isnumeric():
                    bufor2 = bufor2 + x
                else:
                    bufor2 = bufor2 + " "
            bufor = []
            for x in bufor2.split():
                bufor.append(int(x))
            return bufor

        def check(m):
            a = m.author == ctx.author and m.channel == ctx.channel
            return a
        await ctx.send("Sektor:")
        msg = await master.wait_for('message', check=check, timeout=30)
        c = gotu(msg.content)
        x = c[0]
        y = c[1]
        z = c[2]
        bufor = [int(x),int(y),int(z)]
        b = main.Mapa.find(bufor)

        uklad = main.Mapa.fckmap[b][3].posUWS
        print(uklad)
        await clear(ctx, 20)
        for b in range(5):
            a = addons.mapasektora(uklad)
            a.wybierz(int(b))
            a.ret()
            await ctx.send(file=discord.File("test.png"))


@master.command(name="pokazsektor")
@commands.has_role("GM")
async def somting(ctx, b):
    def gotu(a):
        bufor = []
        for x in a:
            if (x.isnumeric() or x == "," or x == " "):
                bufor.append(x)
            else:
                pass
        bufor2 = ''
        for x in bufor:
            if x.isnumeric():
                bufor2 = bufor2 + x
            else:
                bufor2 = bufor2 + " "
        bufor = []
        for x in bufor2.split():
            bufor.append(int(x))
        return bufor

    def check(m):
        a = m.author == ctx.author and m.channel == ctx.channel
        return a

    await ctx.send("Pozycja")
    msg = await master.wait_for('message', check=check, timeout=30)
    c = gotu(msg.content)
    x = c[0]
    y = c[1]
    z = c[2]
    bufor = [int(x), int(y), int(z)]

    await clear(ctx, 20)
    a = addons.mapasektora([bufor])
    a.wybierz(int(b))
    a.ret()
    await ctx.send(file=discord.File("test.png"))

@master.command(name="pokazwszechswiat")
@commands.has_role("GM")
async def somting(ctx, change):
        def gotu(a):
            bufor = []
            for x in a:
                if (x.isnumeric() or x == "," or x == " "):
                    bufor.append(x)
                else:
                    pass
            bufor2 = ''
            for x in bufor:
                if x.isnumeric():
                    bufor2 = bufor2 + x
                else:
                    bufor2 = bufor2 + " "
            bufor = []
            for x in bufor2.split():
                bufor.append(int(x))
            return bufor
        def check(m):
            a = m.author == ctx.author and m.channel == ctx.channel
            return a
        nazwa = await master.wait_for('message', check=check, timeout=30)
        b = gotu(nazwa.content)
        await clear(ctx, 2)
        bufor = [b[1],b[0],b[2]]
        a = addons.mapagalaktyki([bufor])
        a.wybierz(int(change))
        a.ret()
        await ctx.send(file=discord.File("test.png"))

@master.command(name="usunwlosc")
@commands.has_role("GM")
async def somting(ctx):
        def gotu(a):
            bufor = []
            for x in a:
                if (x.isnumeric() or x == "," or x == " "):
                    bufor.append(x)
                else:
                    pass
            bufor2 = ''
            for x in bufor:
                if x.isnumeric():
                    bufor2 = bufor2 + x
                else:
                    bufor2 = bufor2 + " "
            bufor = []
            for x in bufor2.split():
                bufor.append(int(x))
            return bufor

        def check(m):
            a = m.author == ctx.author and m.channel == ctx.channel
            return a

        i = 0
        mess = "``` "
        for a in main.imp:
            i = i + 1
            mess = mess + str(a.impname) + " : " + str(i) + "\n"
        mess = mess + "```"
        await ctx.send("Wybierz Imperium " + mess)
        msg = await master.wait_for('message', check=check, timeout=30)
        if ((msg.content).isnumeric()):
            x = int(msg.content)
            await clear(ctx, 20)
            i = 0
            mess = "``` "
            for a in main.imp[int(x - 1)].wlosci:
                i = i + 1
                mess = mess + str(a.nazwa) + " : " + str(i) + "\n"
            mess = mess + "```"
            await ctx.send("Wybierz włość do usuniecia: numer " + mess)
            msg = await master.wait_for('message', check=check, timeout=30)
            planeta = int(msg.content) - 1
            main.imp[x-1].usun(planeta)
            await ctx.send("Usunieto")
master.run('Nzg0NTkxODEwMDcyMTUwMDQ2.X8riEA.a2OlmW26JABJ3_N3GkaN-gSSGHo')

