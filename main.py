from net_scraping import povleci_podatke_s_spleta
from neo_luscenje_podatkov import (
    neo_izlusci_podatke,
    neo_pripravi_rez,
    neo_zapis_podatkov,
    neo_zapis_csv,
)
from luscenje_podatkov import luscenje_podatkov, podatki_v_csv

# pridobivanje podatkov s spleta za leta 2000, 2004, 2008, 2011, 2014
for leto in [2014.5]:  # [2000, 2004, 2004.5, 2008, 2009, 2011, 2014, 2014.5]:
    povleci_podatke_s_spleta(leto)

# podatke iz datotek za zgoraj našteta leta bomo najprej izluščili, nato pa še zapisali v obliko CSV
for oblika in ["gl", "prc"]:
    for leto in [2014.5]:  # [2000, 2004, 2004.5, 2008, 2009, 2011, 2014.5]:
        luscenje_podatkov(leto)
        podatki_v_csv(leto, oblika)

# priprava dokumentacije za leta 2018, 2022, 2026
# for oblika in ["gl", "prc"]:
#     for leto in [2018, 2022, 2026]:
#         leto, podatki, legenda, rezultati_cela_slovenija = neo_izlusci_podatke(
#             leto, oblika
#         )

#         rez = neo_pripravi_rez(leto, podatki)

#         neo_zapis_podatkov(leto, legenda, rezultati_cela_slovenija, rez)

#         neo_zapis_csv(leto, legenda, rez, oblika)
