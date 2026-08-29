import requests
import time

HEADERS = {"User-Agent": "Chrome/148.0.7778.97"}


def povleci_podatke_s_spleta(leto):
    leto = str(leto)
    link = {
        "2000": "https://www.dvk-rs.si/arhivi/dz2000/",
        "2004.5": "https://www.dvk-rs.si/arhivi/ep2004/",
        "2004": "https://www.dvk-rs.si/arhivi/dz2004/html/",
        "2008": "https://www.dvk-rs.si/arhivi/dz2008/rezultati/",
        "2009": "https://www.dvk-rs.si/arhivi/ep2009/",
        "2011": "https://www.dvk-rs.si/arhivi/dz2011/rezultati/",
        "2014": "https://www.dvk-rs.si/arhivi/dz2014/rezultati/",
        "2014.5": "https://www.dvk-rs.si/arhivi/ep2014/",
    }
    for i in range(1, 9):
        odgovor = requests.get(
            f"{link[str(leto)]}rez_vo{i}.html",
            headers=HEADERS,
        )
        vsebina = odgovor.text

        with open(f"{leto}\\VE_{i}.html", "w", encoding="UTF-8") as dat:
            dat.write(vsebina)
