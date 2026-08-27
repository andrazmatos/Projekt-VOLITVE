# Analiza volilne sturkture okrajev na državnozborskih volitev v Sloveniji od leta 2000 do 2026

## Opis projekta

Projekt obravnava rezultate državnozborskih volitev v Sloveniji. Iz uradnih podatkov izlušči rezultate po volilnih okrajih, jih uredi v primernejšo obliko in pripravi datoteke, ki jih je mogoče uporabiti za nadaljnjo analizo. V knjižnici pandas analizira zbrane podatke in pripelje do ugotovitev, kakšna je volilna sturkura (volatilnost, trdnost, visoka volilna podpora eni politični opciji, swing state ipd.) v 88 volilnih okrajih v Sloveniji. Zbrani podatki omogočajo nadaljnjo podrobnejšo matematično analizo volilnih trendov v SLoveniji po prelomu tisočletja, a te zahtevnejše analize presegajo obseg trenutne seminarske naloge.

## Podatki

Uporabljeni so podatki za državnozborske volitve v letih:

- 2000
- 2004
- 2008
- 2011
- 2014
- 2018
- 2022
- 2026

Podatki za starejša leta (2000—2014) so shranjeni v HTML datotekah, podatki za novejša leta pa so zaradi kompleksnosti spletnih strani po dogovoru s profesorjem naložena v JSON datotekah.

## Kaj program naredi

Program:
- iz spleta naloži HTML kodo za vse volitve pred letom 2018
- prebere izvorne HTML oziroma JSON datoteke,
- izlušči rezultate po volilnih okrajih,
- odstrani stranke, ki niso nastopile v vseh volilnih okrajih,
- pripravi urejene podatkovne datoteke, kjer v obliki slovarja slovarjev zapiše rezultate za vse stranke po volilnih okrajih v obliki procentualnega rezultata in števila glasov,
- ustvari CSV datoteke z deleži glasov po okrajih,
- v datoteki `analiza_volilnih_okrajev` izvede večplastno analizo volilnih okrajev

## Struktura datotek

- `main.py` zažene celoten program.
- `luscenje_podatkov.py` vsebuje funkcije za obdelavo podatkov iz starejših HTML datotek.
- `neo_luscenje_podatkov.py` vsebuje funkcije za obdelavo novejših JSON podatkov.
- Mape `2000`, `2004`, `2008`, `2011`, `2014` vsebujejo HTML datoteke iz tedanjih volitev z rezultati po volilnih enotah.
- Datoteke `data2018.json`, `data2022.json`, `data2026.json` vsebujejo podatke za novejša leta.
- Datoteke `rezultati{leto}_procenti.csv` so ustvarjene izhodne datoteke s procentualnimi rezultati.