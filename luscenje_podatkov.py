import re
import csv


def naredi_okraje():
    okraji = []
    for enota in range(1, 9):
        for zap_st in range(1, 12):
            if zap_st < 10:
                okraji.append(f"{enota}00{zap_st}")
            else:
                okraji.append(f"{enota}0{zap_st}")
    return okraji


# splača se nam odstraniti vso odvečno solato, ki nam jo html pusti: značke, oznako &nbsp. To bom najlažje naredil z operatorjem replace
def ocisti_html(niz):
    niz = re.sub(r"<br\s*/?>", "\n", niz)
    niz = re.sub(r"<.*?>", "", niz)
    niz = niz.replace("&nbsp;", " ")
    return niz.strip()


def luscenje_podatkov(leto):
    okraji_index = {
        "2000": 4,
        "2004.5": 6,
        "2004": 8,
        "2008": 0,
        "2009": 0,
        "2011": 0,
        "2014": 0,
        "2014.5": 0,
    }
    vrstice_index = {
        "2000": 7,
        "2004.5": 9,
        "2004": 11,
        "2008": 3,
        "2011": 3,
        "2009": 3,
        "2014": 3,
        "2014.5": 3,
    }
    podatki = {}
    okraji = naredi_okraje()
    if leto not in [2000, 2004, 2004.5, 2008, 2009, 2011, 2014, 2014.5]:
        return "Neveljavno leto. Državnozborske volitve so potekale leta 2000, 2004, 2008, 2011 in 2014."

    for enota in range(1, 9):
        with open(f"{leto}\\VE_{enota}.html", encoding="UTF-8") as dat:
            table = dat.read()
        okraji_enote = okraji[(enota - 1) * 11 : enota * 11]

        # iz tabele izluščim vrstice, rad pa bi jih vse dal skupaj, ne pa obravnaval vsake posebej, zato bom uporabil re.findall, pri čemer obravnavam samo vsak teks znotraj značk <tr> in </tr>

        vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)

        okraji_neocisceni = re.findall(
            r"<t[dh][^>]*>(.*?)</t[dh]>",
            vrstice[okraji_index[f"{leto}"]],
            flags=re.DOTALL,
        )

        for vrstica in vrstice[vrstice_index[f"{leto}"] :]:
            strankarski_rezultati = re.findall(
                r"<t[dh][^>]*>(.*?)</t[dh]>", vrstica, flags=re.DOTALL
            )
            if len(strankarski_rezultati) < 13:
                continue
            stranka = ocisti_html(strankarski_rezultati[0])
            if stranka not in podatki:
                podatki[stranka] = {}

            # rezultati po okrajih, kjer se sprehajamo skupaj po okraju in rezultatih v obliki <td>...</td>, številka 2 je tam, ker se sprehajamo od tretjega stolpca naprej, saj sta prva ime stranka, drugi pa število vseh glasov
            for okraj, okraj_rezultat in zip(okraji_enote, strankarski_rezultati[2:]):
                vrednosti = (
                    ocisti_html(okraj_rezultat)
                    .replace(".", "")
                    .replace(" %", "")
                    .replace(",", ".")
                    .replace("-", "0\n0")
                    .split("\n")
                )

                glasovi = int(vrednosti[0])
                procent = float(vrednosti[1])
                podatki[stranka][okraj] = {"gl": glasovi, "prc": procent}

    podatki_koncni = {}

    for stranka in podatki.keys():
        if len(podatki[stranka]) == 88:
            podatki_koncni[stranka] = podatki[stranka]

    # pri letih 2004 in 2000 moj rezalnik ujame še nekaj ključev v slovar, ki niso stranke (npr.: 'Dodatne informacije na rvk@gov.si': 0), zato se bom sprehodil po ključih slovarja in če njegova vrednost ni slovar, izbrisal vnos

    # for stranka in podatki_koncni.keys():
    #     if type(podatki_koncni[stranka]) != dict:
    #         podatki_koncni.pop(stranka)
    return podatki_koncni


# sprememba v CSV


def podatki_v_csv(leto, oblika):

    okraji = naredi_okraje()
    podatki_koncni = luscenje_podatkov(leto)
    stranke = list(podatki_koncni.keys())

    with open(
        f"rezultati_{leto}_{oblika}.csv", "w", encoding="utf-8", newline=""
    ) as dat:
        pisec = csv.writer(dat)
        pisec.writerow(["OKRAJ"] + stranke)

        for okraj in okraji:
            vrstica = [okraj]

            for stranka in stranke:
                podatki_sortirani_po_obliki = podatki_koncni[stranka][okraj][oblika]
                if oblika in "prc":
                    delez = podatki_sortirani_po_obliki / 100
                    vrstica.append(round(delez, 4))
                else:
                    vrstica.append(podatki_sortirani_po_obliki)

            pisec.writerow(vrstica)

    return f"Preveri datoteko 'rezultati{leto}_{oblika}.csv'"
