import json
import csv


def neo_izlusci_podatke(leto):
    leto = str(leto)

    crna_lista = {
        "2018": [
            "ReSET",
            "SPS",
            "ZDRUŽENA DESNICA",
            "NPS",
            "ZDRUŽENA LEVICA",
            "SSN",
        ],
        "2022": ["ZSi", "ZOS"],
        "2026": ["SLOGA", "REŠITEV"],
    }

    with open(f"data{leto}.json", "r", encoding="utf-8") as dat:
        podatki = json.load(dat)

    # legenda, kateri id pripada kateri stranki
    # Velik problem imamo, ker stranke na črnem seznamu ne kandidiraju v vseh volilnih enotah, zato dolžina slovarjev ni enaka za vse okraje. Ker so to ponavadi stranki, ki skupaj prejmejo manj kot 0.05% glasov,jih bomo izbrisali iz podatkov.

    legenda = {}

    # podatki za celo Slovenijo
    rezultati_cela_slovenija = {}

    for i in podatki["slovenija"]["rez"]["rez"]:
        if i["knaz"] not in crna_lista[leto]:
            stranka = i["knaz"]
            id_stranke = i["st"]
            procenti = i["prc"]

            legenda[stranka] = id_stranke
            rezultati_cela_slovenija[str(id_stranke)] = procenti

    return leto, podatki, legenda, rezultati_cela_slovenija


def neo_stevilka_okraja(leto, podatki, enota, okraj):
    if leto == "2026":
        stevilka_okraja = stevilka_okraja = podatki["slovenija"]["enote"][enota][
            "okraji"
        ][okraj]["rpeid"]
    if leto in ["2022", "2018"]:
        stevilka_okraja = (enota + 1) * 1000 + podatki["slovenija"]["enote"][enota][
            "okraji"
        ][okraj]["st"]
    return stevilka_okraja


def neo_pripravi_rez(leto, podatki):
    leto = str(leto)

    crna_lista_id = {
        "2018": {14, 19, 7, 11, 25, 22},
        "2022": {5, 21},
        "2026": {107803, 107801},
    }

    rez = {}

    for enota in range(8):
        for okraj in range(11):
            stevilka_okraja = neo_stevilka_okraja(leto, podatki, enota, okraj)

            seznam_rezultatov = podatki["slovenija"]["enote"][enota]["okraji"][okraj][
                "rez"
            ]["rez"]

            nov_seznam = [stevilka_okraja]

            for slovar in seznam_rezultatov:
                if slovar["st"] not in crna_lista_id[leto]:
                    nov_seznam.append(slovar)

            rez[f"podatki_{leto}_{stevilka_okraja}"] = nov_seznam

    return rez


def neo_zapis_podatkov(leto, legenda, rezultati_cela_slovenija, rez):
    leto = str(leto)

    with open(f"data_{leto}.py", "w", encoding="utf-8") as podatkovna_datoteka:
        podatkovna_datoteka.write(
            f"legenda = {legenda}\n\n"
            f"rezultati_cela_slovenija = {rezultati_cela_slovenija}\n\n"
            f"rez = {rez}"
        )


def neo_zapis_csv(leto, legenda, rez):
    leto = str(leto)

    with open(
        f"rezultati_{leto}_procenti.csv", "w", encoding="utf-8", newline=""
    ) as dat:
        tabela = csv.writer(dat)

        tabela.writerow(["OKRAJ"] + list(legenda.keys()))  # pomagal z AI

        for key in rez:
            tabela.writerow(
                [rez[key][0]] + [rez[key][i]["prc"] for i in range(1, len(rez[key]))]
            )
