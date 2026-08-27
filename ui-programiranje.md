# Extract district party percentages

> from this table, i want to extract the parties and thei₹procentages in each of the 1+11 districts (all together + 11 unique), using regex in python (as this is the instruction for school). How should i approach it and how should i store this data in the most usable way to later convert it to CSV. I'm familiar with basic enough python for this challenge, but everything above FMF Uvod v programiranje curriculum is out of scope.
>
> table:
> <tr><td width="13%"class="kaoth">&nbsp;</td><td width="6%"class="kaoth" ><b><font   color="#FFFFFF">Skupaj</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">JESENICE</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">RADOVLJICA I</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">RADOVLJICA II</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">KRANJ I</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">KRANJ II</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">KRANJ III</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">TRŽIČ</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">ŠKOFJA LOKA I</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">ŠKOFJA LOKA II</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">KAMNIK</font></b></td><td width="7%"class="kaoth" ><b><font   color="#FFFFFF">IDRIJA</font></b></td></tr><tr><td width="13%" ><font  >Št. preštetih glasovnic</font></td><td width="6%" align="right" ><font  >143.010<br>99,82&nbsp;%</font></td><td width="7%" align="right" ><font  >17.206<br>100,00&nbsp;%</font></td><td width="7%" align="right" ><font  >10.028<br>100,00&nbsp;%</font></td><td width="7%" align="right" ><font  >10.952<br>100,00&nbsp;%</font></td><td width="7%" align="right" ><font  >14.168<br>99,98&nbsp;%</font></td><td width="7%" align="right" ><font  >13.868<br>99,83&nbsp;%</font></td><td width="7%" align="right" ><font  >16.003<br>99,91&nbsp;%</font></td><td width="7%" align="right" ><font  >9.164<br>97,66&nbsp;%</font></td><td width="7%" align="right" ><font  >11.474<br>100,00&nbsp;%</font></td><td width="7%" align="right" ><font  >12.505<br>100,00&nbsp;%</font></td><td width="7%" align="right" ><font  >17.674<br>99,99&nbsp;%</font></td><td width="7%" align="right" ><font  >9.968<br>99,98&nbsp;%</font></td></tr><tr><td width="13%" ><font  >Št. neveljavnih glasovnic</font></td><td width="6%" align="right" ><font  >5.382<br>3,76&nbsp;%</font></td><td width="7%" align="right" ><font  >884<br>5,14&nbsp;%</font></td><td width="7%" align="right" ><font  >343<br>3,42&nbsp;%</font></td><td width="7%" align="right" ><font  >491<br>4,48&nbsp;%</font></td><td width="7%" align="right" ><font  >425<br>3,00&nbsp;%</font></td><td width="7%" align="right" ><font  >447<br>3,22&nbsp;%</font></td><td width="7%" align="right" ><font  >607<br>3,79&nbsp;%</font></td><td width="7%" align="right" ><font  >326<br>3,56&nbsp;%</font></td><td width="7%" align="right" ><font  >385<br>3,36&nbsp;%</font></td><td width="7%" align="right" ><font  >421<br>3,37&nbsp;%</font></td><td width="7%" align="right" ><font  >585<br>3,31&nbsp;%</font></td><td width="7%" align="right" ><font  >468<br>4,70&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >DeSUS</font></td><td width="6%" align="right" ><font  >4.656<br><b>3,38&nbsp;%</b></font></td><td width="7%" align="right"><font  >557<br>3,41&nbsp;%</font></td><td width="7%" align="right"><font  >375<br>3,87&nbsp;%</font></td><td width="7%" align="right"><font  >403<br>3,85&nbsp;%</font></td><td width="7%" align="right"><font  ><b>564<br>4,10&nbsp;%</b></font></td><td width="7%" align="right"><font  >496<br>3,70&nbsp;%</font></td><td width="7%" align="right"><font  >418<br>2,71&nbsp;%</font></td><td width="7%" align="right"><font  >342<br>3,87&nbsp;%</font></td><td width="7%" align="right"><font  >394<br>3,55&nbsp;%</font></td><td width="7%" align="right"><font  >436<br>3,61&nbsp;%</font></td><td width="7%" align="right"><font  >459<br>2,69&nbsp;%</font></td><td width="7%" align="right"><font  >212<br>2,23&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >DS</font></td><td width="6%" align="right" ><font  >1.009<br><b>0,73&nbsp;%</b></font></td><td width="7%" align="right"><font  >123<br>0,75&nbsp;%</font></td><td width="7%" align="right"><font  ><b>131<br>1,35&nbsp;%</b></font></td><td width="7%" align="right"><font  >101<br>0,97&nbsp;%</font></td><td width="7%" align="right"><font  >65<br>0,47&nbsp;%</font></td><td width="7%" align="right"><font  >90<br>0,67&nbsp;%</font></td><td width="7%" align="right"><font  >123<br>0,80&nbsp;%</font></td><td width="7%" align="right"><font  >16<br>0,18&nbsp;%</font></td><td width="7%" align="right"><font  >60<br>0,54&nbsp;%</font></td><td width="7%" align="right"><font  >101<br>0,84&nbsp;%</font></td><td width="7%" align="right"><font  >148<br>0,87&nbsp;%</font></td><td width="7%" align="right"><font  >51<br>0,54&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >GŽS</font></td><td width="6%" align="right" ><font  >1.758<br><b>1,28&nbsp;%</b></font></td><td width="7%" align="right"><font  ><b>264<br>1,62&nbsp;%</b></font></td><td width="7%" align="right"><font  >154<br>1,59&nbsp;%</font></td><td width="7%" align="right"><font  >142<br>1,36&nbsp;%</font></td><td width="7%" align="right"><font  >184<br>1,34&nbsp;%</font></td><td width="7%" align="right"><font  >181<br>1,35&nbsp;%</font></td><td width="7%" align="right"><font  >165<br>1,07&nbsp;%</font></td><td width="7%" align="right"><font  >91<br>1,03&nbsp;%</font></td><td width="7%" align="right"><font  >150<br>1,35&nbsp;%</font></td><td width="7%" align="right"><font  >114<br>0,94&nbsp;%</font></td><td width="7%" align="right"><font  >209<br>1,22&nbsp;%</font></td><td width="7%" align="right"><font  >104<br>1,09&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >GČP</font></td><td width="6%" align="right" ><font  >572<br><b>0,42&nbsp;%</b></font></td><td width="7%" align="right"><font  >91<br>0,56&nbsp;%</font></td><td width="7%" align="right"><font  >35<br>0,36&nbsp;%</font></td><td width="7%" align="right"><font  >57<br>0,54&nbsp;%</font></td><td width="7%" align="right"><font  >51<br>0,37&nbsp;%</font></td><td width="7%" align="right"><font  >53<br>0,39&nbsp;%</font></td><td width="7%" align="right"><font  >60<br>0,39&nbsp;%</font></td><td width="7%" align="right"><font  ><b>56<br>0,63&nbsp;%</b></font></td><td width="7%" align="right"><font  >34<br>0,31&nbsp;%</font></td><td width="7%" align="right"><font  >35<br>0,29&nbsp;%</font></td><td width="7%" align="right"><font  >63<br>0,37&nbsp;%</font></td><td width="7%" align="right"><font  >37<br>0,39&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >LDS</font></td><td width="6%" align="right" ><font  >43.892<br><b>31,89&nbsp;%</b></font></td><td width="7%" align="right"><font  >5.327<br>32,64&nbsp;%</font></td><td width="7%" align="right"><font  >3.493<br>36,07&nbsp;%</font></td><td width="7%" align="right"><font  >3.181<br>30,41&nbsp;%</font></td><td width="7%" align="right"><font  >5.140<br>37,40&nbsp;%</font></td><td width="7%" align="right"><font  ><b>5.140<br>38,30&nbsp;%</b></font></td><td width="7%" align="right"><font  >4.192<br>27,23&nbsp;%</font></td><td width="7%" align="right"><font  >2.719<br>30,76&nbsp;%</font></td><td width="7%" align="right"><font  >3.765<br>33,95&nbsp;%</font></td><td width="7%" align="right"><font  >2.771<br>22,93&nbsp;%</font></td><td width="7%" align="right"><font  >5.918<br>34,63&nbsp;%</font></td><td width="7%" align="right"><font  >2.246<br>23,64&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >NPS</font></td><td width="6%" align="right" ><font  >370<br><b>0,27&nbsp;%</b></font></td><td width="7%" align="right"><font  >54<br>0,33&nbsp;%</font></td><td width="7%" align="right"><font  >12<br>0,12&nbsp;%</font></td><td width="7%" align="right"><font  ><b>37<br>0,35&nbsp;%</b></font></td><td width="7%" align="right"><font  >31<br>0,23&nbsp;%</font></td><td width="7%" align="right"><font  >40<br>0,30&nbsp;%</font></td><td width="7%" align="right"><font  >35<br>0,23&nbsp;%</font></td><td width="7%" align="right"><font  >14<br>0,16&nbsp;%</font></td><td width="7%" align="right"><font  >29<br>0,26&nbsp;%</font></td><td width="7%" align="right"><font  >38<br>0,31&nbsp;%</font></td><td width="7%" align="right"><font  >57<br>0,33&nbsp;%</font></td><td width="7%" align="right"><font  >23<br>0,24&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >NOVA</font></td><td width="6%" align="right" ><font  >536<br><b>0,39&nbsp;%</b></font></td><td width="7%" align="right"><font  >66<br>0,40&nbsp;%</font></td><td width="7%" align="right"><font  >24<br>0,25&nbsp;%</font></td><td width="7%" align="right"><font  >26<br>0,25&nbsp;%</font></td><td width="7%" align="right"><font  >49<br>0,36&nbsp;%</font></td><td width="7%" align="right"><font  >55<br>0,41&nbsp;%</font></td><td width="7%" align="right"><font  ><b>85<br>0,55&nbsp;%</b></font></td><td width="7%" align="right"><font  >16<br>0,18&nbsp;%</font></td><td width="7%" align="right"><font  >40<br>0,36&nbsp;%</font></td><td width="7%" align="right"><font  >64<br>0,53&nbsp;%</font></td><td width="7%" align="right"><font  >70<br>0,41&nbsp;%</font></td><td width="7%" align="right"><font  >41<br>0,43&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >NSi</font></td><td width="6%" align="right" ><font  >15.805<br><b>11,48&nbsp;%</b></font></td><td width="7%" align="right"><font  >1.500<br>9,19&nbsp;%</font></td><td width="7%" align="right"><font  >1.132<br>11,69&nbsp;%</font></td><td width="7%" align="right"><font  >1.354<br>12,94&nbsp;%</font></td><td width="7%" align="right"><font  >1.234<br>8,98&nbsp;%</font></td><td width="7%" align="right"><font  >1.198<br>8,93&nbsp;%</font></td><td width="7%" align="right"><font  >1.876<br>12,18&nbsp;%</font></td><td width="7%" align="right"><font  >554<br>6,27&nbsp;%</font></td><td width="7%" align="right"><font  >1.470<br>13,26&nbsp;%</font></td><td width="7%" align="right"><font  ><b>2.734<br>22,62&nbsp;%</b></font></td><td width="7%" align="right"><font  >2.118<br>12,39&nbsp;%</font></td><td width="7%" align="right"><font  >635<br>6,68&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >SNS</font></td><td width="6%" align="right" ><font  >4.242<br><b>3,08&nbsp;%</b></font></td><td width="7%" align="right"><font  >525<br>3,22&nbsp;%</font></td><td width="7%" align="right"><font  >291<br>3,00&nbsp;%</font></td><td width="7%" align="right"><font  >360<br>3,44&nbsp;%</font></td><td width="7%" align="right"><font  ><b>569<br>4,14&nbsp;%</b></font></td><td width="7%" align="right"><font  >546<br>4,07&nbsp;%</font></td><td width="7%" align="right"><font  >416<br>2,70&nbsp;%</font></td><td width="7%" align="right"><font  >266<br>3,01&nbsp;%</font></td><td width="7%" align="right"><font  >328<br>2,96&nbsp;%</font></td><td width="7%" align="right"><font  >217<br>1,80&nbsp;%</font></td><td width="7%" align="right"><font  >480<br>2,81&nbsp;%</font></td><td width="7%" align="right"><font  >244<br>2,57&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >SLS+SKD</font></td><td width="6%" align="right" ><font  >12.307<br><b>8,94&nbsp;%</b></font></td><td width="7%" align="right"><font  >550<br>3,37&nbsp;%</font></td><td width="7%" align="right"><font  >746<br>7,70&nbsp;%</font></td><td width="7%" align="right"><font  >349<br>3,34&nbsp;%</font></td><td width="7%" align="right"><font  >673<br>4,90&nbsp;%</font></td><td width="7%" align="right"><font  >688<br>5,13&nbsp;%</font></td><td width="7%" align="right"><font  >1.468<br>9,53&nbsp;%</font></td><td width="7%" align="right"><font  >521<br>5,89&nbsp;%</font></td><td width="7%" align="right"><font  >1.315<br>11,86&nbsp;%</font></td><td width="7%" align="right"><font  >1.788<br>14,80&nbsp;%</font></td><td width="7%" align="right"><font  >2.173<br>12,72&nbsp;%</font></td><td width="7%" align="right"><font  ><b>2.036<br>21,43&nbsp;%</b></font></td></tr><tr><td width="13%" align="left"><font  >SMS</font></td><td width="6%" align="right" ><font  >7.204<br><b>5,23&nbsp;%</b></font></td><td width="7%" align="right"><font  >949<br>5,81&nbsp;%</font></td><td width="7%" align="right"><font  >567<br>5,85&nbsp;%</font></td><td width="7%" align="right"><font  >623<br>5,96&nbsp;%</font></td><td width="7%" align="right"><font  ><b>836<br>6,08&nbsp;%</b></font></td><td width="7%" align="right"><font  >754<br>5,62&nbsp;%</font></td><td width="7%" align="right"><font  >852<br>5,53&nbsp;%</font></td><td width="7%" align="right"><font  >343<br>3,88&nbsp;%</font></td><td width="7%" align="right"><font  >526<br>4,74&nbsp;%</font></td><td width="7%" align="right"><font  >422<br>3,49&nbsp;%</font></td><td width="7%" align="right"><font  >903<br>5,28&nbsp;%</font></td><td width="7%" align="right"><font  >429<br>4,52&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >SDS</font></td><td width="6%" align="right" ><font  >25.503<br><b>18,53&nbsp;%</b></font></td><td width="7%" align="right"><font  >2.337<br>14,32&nbsp;%</font></td><td width="7%" align="right"><font  >1.359<br>14,03&nbsp;%</font></td><td width="7%" align="right"><font  >1.617<br>15,46&nbsp;%</font></td><td width="7%" align="right"><font  >2.277<br>16,57&nbsp;%</font></td><td width="7%" align="right"><font  >2.424<br>18,06&nbsp;%</font></td><td width="7%" align="right"><font  >4.468<br>29,02&nbsp;%</font></td><td width="7%" align="right"><font  ><b>2.714<br>30,71&nbsp;%</b></font></td><td width="7%" align="right"><font  >1.908<br>17,21&nbsp;%</font></td><td width="7%" align="right"><font  >2.297<br>19,01&nbsp;%</font></td><td width="7%" align="right"><font  >2.852<br>16,69&nbsp;%</font></td><td width="7%" align="right"><font  >1.250<br>13,16&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >SDAS</font></td><td width="6%" align="right" ><font  >1.003<br><b>0,73&nbsp;%</b></font></td><td width="7%" align="right"><font  ><b>454<br>2,78&nbsp;%</b></font></td><td width="7%" align="right"><font  >28<br>0,29&nbsp;%</font></td><td width="7%" align="right"><font  >71<br>0,68&nbsp;%</font></td><td width="7%" align="right"><font  >103<br>0,75&nbsp;%</font></td><td width="7%" align="right"><font  >112<br>0,83&nbsp;%</font></td><td width="7%" align="right"><font  >40<br>0,26&nbsp;%</font></td><td width="7%" align="right"><font  >44<br>0,50&nbsp;%</font></td><td width="7%" align="right"><font  >37<br>0,33&nbsp;%</font></td><td width="7%" align="right"><font  >17<br>0,14&nbsp;%</font></td><td width="7%" align="right"><font  >78<br>0,46&nbsp;%</font></td><td width="7%" align="right"><font  >19<br>0,20&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >ZDRUŽENI ZELENI</font></td><td width="6%" align="right" ><font  >1.332<br><b>0,97&nbsp;%</b></font></td><td width="7%" align="right"><font  >161<br>0,99&nbsp;%</font></td><td width="7%" align="right"><font  >96<br>0,99&nbsp;%</font></td><td width="7%" align="right"><font  >110<br>1,05&nbsp;%</font></td><td width="7%" align="right"><font  >173<br>1,26&nbsp;%</font></td><td width="7%" align="right"><font  >138<br>1,03&nbsp;%</font></td><td width="7%" align="right"><font  >93<br>0,60&nbsp;%</font></td><td width="7%" align="right"><font  >116<br>1,31&nbsp;%</font></td><td width="7%" align="right"><font  >87<br>0,78&nbsp;%</font></td><td width="7%" align="right"><font  >48<br>0,40&nbsp;%</font></td><td width="7%" align="right"><font  ><b>253<br>1,48&nbsp;%</b></font></td><td width="7%" align="right"><font  >57<br>0,60&nbsp;%</font></td></tr><tr><td width="13%" align="left"><font  >ZLSD</font></td><td width="6%" align="right" ><font  >17.439<br><b>12,67&nbsp;%</b></font></td><td width="7%" align="right"><font  >3.364<br>20,61&nbsp;%</font></td><td width="7%" align="right"><font  >1.242<br>12,82&nbsp;%</font></td><td width="7%" align="right"><font  >2.030<br>19,41&nbsp;%</font></td><td width="7%" align="right"><font  >1.794<br>13,05&nbsp;%</font></td><td width="7%" align="right"><font  >1.506<br>11,22&nbsp;%</font></td><td width="7%" align="right"><font  >1.105<br>7,18&nbsp;%</font></td><td width="7%" align="right"><font  >1.026<br>11,61&nbsp;%</font></td><td width="7%" align="right"><font  >946<br>8,53&nbsp;%</font></td><td width="7%" align="right"><font  >1.002<br>8,29&nbsp;%</font></td><td width="7%" align="right"><font  >1.308<br>7,65&nbsp;%</font></td><td width="7%" align="right"><font  ><b>2.116<br>22,27&nbsp;%</b></font></td></tr>

Since school requires regex, I would do it in layers:

1. Extract table rows: `<tr>...</tr>`
2. Extract cells from each row: `<td ...>...</td>`
3. Remove HTML tags like `<font>`, `<b>`, `<br>`
4. Use first row as district names
5. Use party rows for data
6. Store data as a list of dictionaries, because that converts very cleanly to CSV later

The most usable CSV shape is probably “long format”:

```csv
party,district,votes,percentage
DeSUS,Skupaj,4656,3.38
DeSUS,JESENICE,557,3.41
...
```

That is easier to filter, sort, graph, and process than one huge row per party.

Example approach:

```python
import re
import csv

table = """PASTE YOUR TABLE STRING HERE"""

def clean_html(text):
    text = text.replace("<br>", "\n")
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("&nbsp;", " ")
    return text.strip()

def parse_number(text):
    # "4.656" -> 4656
    return int(text.replace(".", ""))

def parse_percent(text):
    # "3,38 %" -> 3.38
    text = text.replace("%", "").strip()
    return float(text.replace(",", "."))

# 1. Extract rows
rows = re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)

# 2. Extract districts from header row
header_cells = re.findall(r"<td[^>]*>(.*?)</td>", rows[0], flags=re.DOTALL)
districts = []

for cell in header_cells[1:]:   # skip first empty cell
    districts.append(clean_html(cell))

# 3. Extract party data
data = []

for row in rows[3:]:   # skip header + 2 statistic rows
    cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.DOTALL)

    party = clean_html(cells[0])

    for district, cell in zip(districts, cells[1:]):
        text = clean_html(cell)
        parts = text.split()

        votes = parse_number(parts[0])
        percentage = parse_percent(parts[1])

        data.append({
            "party": party,
            "district": district,
            "votes": votes,
            "percentage": percentage
        })

# 4. Write CSV
with open("results.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["party", "district", "votes", "percentage"])
    writer.writeheader()
    writer.writerows(data)
```

The key idea: do not try to extract “party + all percentages” with one giant regex. Use small regexes repeatedly. First rows, then cells, then clean each cell. Much easier to debug and totally enough for this assignment.

> razloži tole

Seveda. Ideja je: HTML tabela je navaden niz znakov, zato jo z regexi razbijemo na manjše dele.

Najprej imamo:

```python
rows = re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)
```

To poišče vse vrstice tabele. Vsaka vrstica je med `<tr>` in `</tr>`.
`.*?` pomeni “vzemi čim manj znakov, dokler ne prideš do `</tr>`”.
`re.DOTALL` je zato, da pika `.` ujame tudi prehode v novo vrstico.

Potem iz prve vrstice dobimo imena okrajev:

```python
header_cells = re.findall(r"<td[^>]*>(.*?)</td>", rows[0], flags=re.DOTALL)
```

To poišče vse celice `<td ...>...</td>`.
Del `[^>]*` pomeni “karkoli znotraj začetnega taga”, recimo:

```html
<td width="7%" class="kaoth">
```

Nas zanima samo vsebina med `>` in `</td>`.

Ker je prva celica prazna, jo preskočimo:

```python
for cell in header_cells[1:]:
    districts.append(clean_html(cell))
```

Funkcija `clean_html` odstrani HTML oznake:

```python
def clean_html(text):
    text = text.replace("<br>", "\n")
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("&nbsp;", " ")
    return text.strip()
```

Na primer tole:

```html
<font><b>3,38&nbsp;%</b></font>
```

postane:

```text
3,38 %
```

Glavni del je potem:

```python
for row in rows[3:]:
```

Zakaj `rows[3:]`? Ker preskočimo:

1. naslovno vrstico z okraji,
2. vrstico “Št. preštetih glasovnic”,
3. vrstico “Št. neveljavnih glasovnic”.

Od četrte vrstice naprej so politične stranke.

Za vsako vrstico naredimo:

```python
cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.DOTALL)
party = clean_html(cells[0])
```

Prva celica vsebuje ime stranke, recimo `DeSUS`.

Ostale celice vsebujejo glasove in procent:

```python
for district, cell in zip(districts, cells[1:]):
```

`zip` tukaj poveže vsak okraj z ustrezno celico. Recimo:

```python
Skupaj        -> 4.656 / 3,38 %
JESENICE      -> 557 / 3,41 %
RADOVLJICA I  -> 375 / 3,87 %
```

Potem celico očistimo:

```python
text = clean_html(cell)
parts = text.split()
```

Če imamo:

```text
4.656
3,38 %
```

`split()` naredi približno:

```python
["4.656", "3,38", "%"]
```

Zato vzamemo:

```python
votes = parse_number(parts[0])
percentage = parse_percent(parts[1])
```

`parse_number` spremeni slovensko zapisano število v `int`:

```python
"4.656" -> 4656
```

`parse_percent` spremeni decimalno vejico v decimalno piko:

```python
"3,38" -> 3.38
```

Na koncu vsak podatek shranimo kot slovar:

```python
data.append({
    "party": party,
    "district": district,
    "votes": votes,
    "percentage": percentage
})
```

En element v seznamu `data` bo izgledal tako:

```python
{
    "party": "DeSUS",
    "district": "Skupaj",
    "votes": 4656,
    "percentage": 3.38
}
```

To je zelo uporabna oblika, ker jo lahko direktno zapišeš v CSV:

```python
party,district,votes,percentage
DeSUS,Skupaj,4656,3.38
DeSUS,JESENICE,557,3.41
DeSUS,RADOVLJICA I,375,3.87
```

Glavna poanta: ne poskušaš z enim ogromnim regexom rešiti cele tabele. Najprej razbiješ na vrstice, potem na celice, potem iz vsake celice pobereš besedilo. To je veliko bolj pregledno in primerno za nivo Uvoda v programiranje.

> def clean_html(text):
>     text = text.replace("<br>", "\n")
>     text = re.sub(r"<.*?>", "", text)
>     text = text.replace("&nbsp;", " ")
>     return text.strip()

Ta funkcija vzame kos HTML-ja in ga spremeni v navadno besedilo.

```python
def clean_html(text):
```

Definiraš funkcijo z imenom `clean_html`, ki sprejme en niz `text`.

```python
text = text.replace("<br>", "\n")
```

Zamenja HTML prelom vrstice `<br>` z navadnim Python prelomom vrstice `\n`.

Primer:

```python
"4.656<br>3,38&nbsp;%"
```

postane:

```python
"4.656\n3,38&nbsp;%"
```

Potem:

```python
text = re.sub(r"<.*?>", "", text)
```

To odstrani vse HTML oznake, na primer `<font>`, `<b>`, `</b>`, `</font>`.

Regex:

```python
r"<.*?>"
```

pomeni:

- `<` začetek HTML oznake
- `.*?` poljubni znaki, ampak čim manj
- `>` konec HTML oznake

Primer:

```python
"<font><b>3,38&nbsp;%</b></font>"
```

postane:

```python
"3,38&nbsp;%"
```

Potem:

```python
text = text.replace("&nbsp;", " ")
```

HTML znak `&nbsp;` pomeni “non-breaking space”, torej poseben presledek. Zamenjamo ga z navadnim presledkom.

Primer:

```python
"3,38&nbsp;%"
```

postane:

```python
"3,38 %"
```

Na koncu:

```python
return text.strip()
```

`strip()` odstrani odvečne presledke in nove vrstice na začetku in koncu niza.

Primer celotne funkcije:

```python
clean_html("<font><b>4.656<br>3,38&nbsp;%</b></font>")
```

vrne:

```python
"4.656\n3,38 %"
```

Torej funkcija naredi to:

```html
<font><b>4.656<br>3,38&nbsp;%</b></font>
```

v to:

```text
4.656
3,38 %
```

> ampak če izbrišem vse značke HTMLja, potem izbrišem tudi <tr> in </tr>, torej ne bom mogel iskati po vrsticah

Točno, dobra opazka. Zato `clean_html` uporabiš **šele potem**, ko si tabelo že razbil na vrstice in celice.

Vrstni red je pomemben:

```python
# 1. Najprej poiščeš vrstice, dokler <tr> še obstaja
rows = re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)

# 2. Potem v vsaki vrstici poiščeš celice, dokler <td> še obstaja
cells = re.findall(r"<td[^>]*>(.*?)</td>", rows[0], flags=re.DOTALL)

# 3. Šele na koncu očistiš vsebino posamezne celice
clean_cell = clean_html(cells[0])
```

Ne narediš tega:

```python
table = clean_html(table)   # tega ne narediš na začetku
```

Ker potem res izgubiš `<tr>`, `<td>` in ostalo strukturo.

Pravilna logika je:

```python
rows = re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)

for row in rows:
    cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.DOTALL)

    for cell in cells:
        text = clean_html(cell)
        print(text)
```

Torej:

- cela tabela še ima `<tr>` in `<td>`
- posamezna vrstica še ima `<td>`
- posamezna celica se šele potem očisti HTML značk

Primer:

```python
row = '<tr><td><font>DeSUS</font></td><td><font>4.656<br><b>3,38&nbsp;%</b></font></td></tr>'

cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.DOTALL)

print(cells)
```

Dobiš približno:

```python
['<font>DeSUS</font>', '<font>4.656<br><b>3,38&nbsp;%</b></font>']
```

Zdaj lahko vsako celico posebej očistiš:

```python
for cell in cells:
    print(clean_html(cell))
```

Rezultat:

```text
DeSUS
4.656
3,38 %
```

Tvoja intuicija je pravilna: če bi HTML očistil prehitro, bi si odstranil “orientacijske oznake”, po katerih sploh veš, kje so vrstice in stolpci.

> kako dobri programerji uporabljajo main.py za definicijo ključnih funkcij in kako to vpeljejo potem v ostale datoteke v repozitoriju

Dobri programerji praviloma **ne uporabljajo `main.py` kot skladišče ključnih funkcij**. Bolj tipičen vzorec je:

- `main.py` je **vstopna točka programa**
- ključne funkcije so v ločenih datotekah/modulih
- `main.py` jih samo uvozi, poveže skupaj in zažene

Torej `main.py` naj bo bolj “dirigent”, ne pa cela orkestrska dvorana.

Recimo za tvoj primer s tabelo bi imel strukturo:

```text
projekt/
├── main.py
├── parser.py
├── export.py
└── data/
    └── tabela.html
```

V `parser.py` daš funkcije za obdelavo HTML-ja:

```python
# parser.py

import re

def clean_html(text):
    text = text.replace("<br>", "\n")
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("&nbsp;", " ")
    return text.strip()

def parse_number(text):
    return int(text.replace(".", ""))

def parse_percent(text):
    text = text.replace("%", "").strip()
    return float(text.replace(",", "."))

def extract_rows(table):
    return re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)

def extract_cells(row):
    return re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.DOTALL)
```

V `export.py` daš funkcijo za CSV:

```python
# export.py

import csv

def write_csv(filename, data):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["party", "district", "votes", "percentage"]
        )
        writer.writeheader()
        writer.writerows(data)
```

Potem je `main.py` samo kraj, kjer vse skupaj uporabiš:

```python
# main.py

from parser import clean_html, extract_rows, extract_cells, parse_number, parse_percent
from export import write_csv

def parse_table(table):
    rows = extract_rows(table)

    header_cells = extract_cells(rows[0])
    districts = []

    for cell in header_cells[1:]:
        districts.append(clean_html(cell))

    data = []

    for row in rows[3:]:
        cells = extract_cells(row)

        party = clean_html(cells[0])

        for district, cell in zip(districts, cells[1:]):
            text = clean_html(cell)
            parts = text.split()

            votes = parse_number(parts[0])
            percentage = parse_percent(parts[1])

            data.append({
                "party": party,
                "district": district,
                "votes": votes,
                "percentage": percentage
            })

    return data

def main():
    with open("data/tabela.html", encoding="utf-8") as f:
        table = f.read()

    data = parse_table(table)
    write_csv("results.csv", data)

if __name__ == "__main__":
    main()
```

Ta zadnji del:

```python
if __name__ == "__main__":
    main()
```

pomeni: “Zaženi `main()` samo, če sem to datoteko pognal direktno.”

Če narediš:

```bash
python main.py
```

se program zažene.

Če pa nekje drugje napišeš:

```python
import main
```

se `main()` ne zažene avtomatsko. To je koristno, ker lahko funkcije iz `main.py` uvoziš drugam brez nezaželenega zagona programa.

Ampak še boljši vzorec je, da iz drugih datotek **ne uvažaš iz `main.py`**, razen redko. Namesto tega skupne funkcije prestaviš v module, kot so:

```text
parser.py
export.py
utils.py
```

Potem jih uporabljaš tako:

```python
from parser import clean_html
from export import write_csv
```

Praktično pravilo:

```text
main.py     = zaženi program
parser.py   = pretvori HTML v podatke
export.py   = shrani podatke v CSV
utils.py    = majhne pomožne funkcije, če jih res potrebuješ
```

Za šolski projekt bi bil čisto lep minimum:

```text
projekt/
├── main.py
├── parser.py
└── tabela.html
```

`main.py` naj pove zgodbo programa:

```python
preberi datoteko
obdelaj podatke
shrani CSV
```

`parser.py` pa naj vsebuje podrobnosti, kako točno z regexom prideš od HTML-ja do podatkov.

> with
> vrstice = re.findall(r"<tr>(.?*)</tr>", table, flags=re.DOTALL)
> print(vrstice)
>
> i get the error File "C:\Users\Uporabnik\AppData\Local\Programs\Python\Python313\Lib\re\_parser.py", line 459, in _parse_sub
>     itemsappend(_parse(source, state, verbose, nested + 1,
>                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>                        not nested and not items))
>                        ^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "C:\Users\Uporabnik\AppData\Local\Programs\Python\Python313\Lib\re\_parser.py", line 689, in _parse
>     raise source.error("multiple repeat",
>                        source.tell() - here + len(this))
> re.PatternError: multiple repeat at position 7
>
> with the table being the whole text in the file attahced
>
> User context
>
> Attachments:
> - VE_1.html: `~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2000/VE_1.html`

<details><summary>2 previous messages</summary>

> I’ll check the actual file shape briefly so the regex advice matches what you’re parsing. The error itself is from a tiny typo in the pattern, but the surrounding HTML may also need a slightly more flexible pattern.
>
> The file is readable, and it starts with a full HTML page, not just the table fragment. I’m going to look for the first few `<tr>` tags now; that tells us whether your pattern needs to allow attributes or whitespace.
</details>

Napaka je v tem delu regexa:

```python
(.?*)
```

To Python razume kot “znak `.` je ponovljen z `?`, potem pa hočeš isti del še enkrat ponavljati z `*`”. Zato dobiš:

```text
multiple repeat
```

Pravilno je:

```python
(.*?)
```

Torej:

```python
vrstice = re.findall(r"<tr>(.*?)</tr>", table, flags=re.DOTALL)
print(vrstice)
```

Razlika:

```python
.?*   # narobe
.*?   # prav
```

Pomen pravilnega vzorca:

```python
<tr>    # začetek vrstice
(.*?)   # zajemi vsebino, ampak čim manj
</tr>   # konec vrstice
```

Ker ima tvoja datoteka včasih tudi presledke pred `<tr>`, je lahko še malo bolj robustno:

```python
vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)
```

Ta verzija bi delovala tudi, če bi bil kdaj začetni tag tak:

```html
<tr class="nekaj">
```

Za branje datoteke pa uporabi nekaj takega:

```python
import re

with open("VE_1.html", encoding="utf-8") as datoteka:
    table = datoteka.read()

vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)

print(len(vrstice))
print(vrstice[0])
```

Še opozorilo: v tvoji datoteki je celotna HTML stran, zato bo `vrstice` našel tudi nekaj vrstic iz drugih tabel pred glavno volilno tabelo. Glavna tabela s strankami se začne šele kasneje, zato boš moral potem izbrati pravi del, na primer z iskanjem vrstice, ki vsebuje `"Skupaj"` in `"JESENICE"`.

> s to kodo:
> podatki[stranka][okraj] = (
>             ocisti_html(okraj_rezultat)
>             .replace(".", "")
>             .replace("%", "")
>             .replace(",", ".")
>             .split("\n")
>         )
>
> ddobim nekaj takega kot je tole:
> 'RADOVLJICA I': ['28', '0.29']
>
> kako v tem sezamu string spremenim v int in v float

Najbolj direktno:

```python
vrednosti = (
    ocisti_html(okraj_rezultat)
    .replace(".", "")
    .replace("%", "")
    .replace(",", ".")
    .split("\n")
)

glasovi = int(vrednosti[0])
procent = float(vrednosti[1])

podatki[stranka][okraj] = [glasovi, procent]
```

Če imaš torej:

```python
vrednosti = ["28", "0.29"]
```

potem:

```python
int(vrednosti[0])      # 28
float(vrednosti[1])    # 0.29
```

Lahko pa napišeš malo krajše:

```python
vrednosti = (
    ocisti_html(okraj_rezultat)
    .replace(".", "")
    .replace("%", "")
    .replace(",", ".")
    .split("\n")
)

podatki[stranka][okraj] = [int(vrednosti[0]), float(vrednosti[1])]
```

Še bolj uporabno za kasneje je mogoče shraniti kot slovar:

```python
podatki[stranka][okraj] = {
    "glasovi": int(vrednosti[0]),
    "procent": float(vrednosti[1])
}
```

Potem dobiš:

```python
{
    "glasovi": 28,
    "procent": 0.29
}
```

in dostopaš tako:

```python
podatki["SDAS"]["RADOVLJICA I"]["glasovi"]
podatki["SDAS"]["RADOVLJICA I"]["procent"]
```

> ali misliš, da je taka oblika podatkov uporabna za nadaljnjo uporabo?:
>
> {'DeSUS': {'Skupaj': [4656, 3.38], 'JESENICE': [557, 3.41], 'RADOVLJICA I': [375, 3.87], 'RADOVLJICA II': [403, 3.85], 'KRANJ I': [564, 4.1], 'KRANJ II': [496, 3.7], 'KRANJ III': [418, 2.71], 'TRŽIČ': [342, 3.87], 'ŠKOFJA LOKA I': [394, 3.55], 'ŠKOFJA LOKA II': [436, 3.61], 'KAMNIK': [459, 2.69], 'IDRIJA': [212, 2.23]}, 'DS': {'Skupaj': [1009, 0.73], 'JESENICE': [123, 0.75], 'RADOVLJICA I': [131, 1.35], 'RADOVLJICA II': [101, 0.97], 'KRANJ I': [65, 0.47], 'KRANJ II': [90, 0.67], 'KRANJ III': [123, 0.8], 'TRŽIČ': [16, 0.18], 'ŠKOFJA LOKA I': [60, 0.54], 'ŠKOFJA LOKA II': [101, 0.84], 'KAMNIK': [148, 0.87], 'IDRIJA': [51, 0.54]}, 'GŽS': {'Skupaj': [1758, 1.28], 'JESENICE': [264, 1.62], 'RADOVLJICA I': [154, 1.59], 'RADOVLJICA II': [142, 1.36], 'KRANJ I': [184, 1.34], 'KRANJ II': [181, 1.35], 'KRANJ III': [165, 1.07], 'TRŽIČ': [91, 1.03], 'ŠKOFJA LOKA I': [150, 1.35], 'ŠKOFJA LOKA II': [114, 0.94], 'KAMNIK': [209, 1.22], 'IDRIJA': [104, 1.09]}, 'GČP': {'Skupaj': [572, 0.42], 'JESENICE': [91, 0.56], 'RADOVLJICA I': [35, 0.36], 'RADOVLJICA II': [57, 0.54], 'KRANJ I': [51, 0.37], 'KRANJ II': [53, 0.39], 'KRANJ III': [60, 0.39], 'TRŽIČ': [56, 0.63], 'ŠKOFJA LOKA I': [34, 0.31], 'ŠKOFJA LOKA II': [35, 0.29], 'KAMNIK': [63, 0.37], 'IDRIJA': [37, 0.39]}, 'LDS': {'Skupaj': [43892, 31.89], 'JESENICE': [5327, 32.64], 'RADOVLJICA I': [3493, 36.07], 'RADOVLJICA II': [3181, 30.41], 'KRANJ I': [5140, 37.4], 'KRANJ II': [5140, 38.3], 'KRANJ III': [4192, 27.23], 'TRŽIČ': [2719, 30.76], 'ŠKOFJA LOKA I': [3765, 33.95], 'ŠKOFJA LOKA II': [2771, 22.93], 'KAMNIK': [5918, 34.63], 'IDRIJA': [2246, 23.64]}, 'NPS': {'Skupaj': [370, 0.27], 'JESENICE': [54, 0.33], 'RADOVLJICA I': [12, 0.12], 'RADOVLJICA II': [37, 0.35], 'KRANJ I': [31, 0.23], 'KRANJ II': [40, 0.3], 'KRANJ III': [35, 0.23], 'TRŽIČ': [14, 0.16], 'ŠKOFJA LOKA I': [29, 0.26], 'ŠKOFJA LOKA II': [38, 0.31], 'KAMNIK': [57, 0.33], 'IDRIJA': [23, 0.24]}, 'NOVA': {'Skupaj': [536, 0.39], 'JESENICE': [66, 0.4], 'RADOVLJICA I': [24, 0.25], 'RADOVLJICA II': [26, 0.25], 'KRANJ I': [49, 0.36], 'KRANJ II': [55, 0.41], 'KRANJ III': [85, 0.55], 'TRŽIČ': [16, 0.18], 'ŠKOFJA LOKA I': [40, 0.36], 'ŠKOFJA LOKA II': [64, 0.53], 'KAMNIK': [70, 0.41], 'IDRIJA': [41, 0.43]}, 'NSi': {'Skupaj': [15805, 11.48], 'JESENICE': [1500, 9.19], 'RADOVLJICA I': [1132, 11.69], 'RADOVLJICA II': [1354, 12.94], 'KRANJ I': [1234, 8.98], 'KRANJ II': [1198, 8.93], 'KRANJ III': [1876, 12.18], 'TRŽIČ': [554, 6.27], 'ŠKOFJA LOKA I': [1470, 13.26], 'ŠKOFJA LOKA II': [2734, 22.62], 'KAMNIK': [2118, 12.39], 'IDRIJA': [635, 6.68]}, 'SNS': {'Skupaj': [4242, 3.08], 'JESENICE': [525, 3.22], 'RADOVLJICA I': [291, 3.0], 'RADOVLJICAII': [360, 3.44], 'KRANJ I': [569, 4.14], 'KRANJ II': [546, 4.07], 'KRANJ III': [416, 2.7], 'TRŽIČ': [266, 3.01], 'ŠKOFJA LOKA I': [328, 2.96], 'ŠKOFJA LOKA II': [217, 1.8], 'KAMNIK': [480, 2.81], 'IDRIJA': [244, 2.57]}, 'SLS+SKD': {'Skupaj': [12307, 8.94], 'JESENICE': [550, 3.37], 'RADOVLJICA I': [746, 7.7], 'RADOVLJICA II': [349, 3.34], 'KRANJ I': [673, 4.9], 'KRANJ II': [688, 5.13], 'KRANJ III': [1468, 9.53], 'TRŽIČ': [521, 5.89], 'ŠKOFJA LOKA I': [1315, 11.86], 'ŠKOFJA LOKA II': [1788, 14.8], 'KAMNIK': [2173, 12.72], 'IDRIJA': [2036, 21.43]}, 'SMS': {'Skupaj': [7204, 5.23], 'JESENICE': [949, 5.81], 'RADOVLJICA I': [567, 5.85], 'RADOVLJICA II': [623, 5.96], 'KRANJ I': [836, 6.08], 'KRANJ II': [754, 5.62], 'KRANJ III': [852, 5.53], 'TRŽIČ': [343, 3.88], 'ŠKOFJA LOKA I': [526, 4.74], 'ŠKOFJA LOKA II': [422, 3.49], 'KAMNIK': [903, 5.28], 'IDRIJA': [429, 4.52]}, 'SDS': {'Skupaj': [25503, 18.53], 'JESENICE': [2337, 14.32], 'RADOVLJICA I': [1359, 14.03], 'RADOVLJICA II': [1617, 15.46], 'KRANJ I': [2277, 16.57], 'KRANJ II': [2424, 18.06], 'KRANJ III':[4468, 29.02], 'TRŽIČ': [2714, 30.71], 'ŠKOFJA LOKA I': [1908, 17.21], 'ŠKOFJA LOKA II': [2297, 19.01], 'KAMNIK': [2852, 16.69], 'IDRIJA': [1250, 13.16]}, 'SDAS': {'Skupaj': [1003, 0.73], 'JESENICE': [454, 2.78], 'RADOVLJICA I': [28, 0.29], 'RADOVLJICA II': [71, 0.68], 'KRANJ I': [103, 0.75], 'KRANJ II': [112, 0.83], 'KRANJ III': [40, 0.26], 'TRŽIČ': [44, 0.5], 'ŠKOFJA LOKA I': [37, 0.33], 'ŠKOFJA LOKA II': [17, 0.14], 'KAMNIK': [78, 0.46], 'IDRIJA': [19, 0.2]}, 'ZDRUŽENI ZELENI': {'Skupaj': [1332, 0.97], 'JESENICE': [161, 0.99], 'RADOVLJICA I': [96, 0.99], 'RADOVLJICA II': [110, 1.05], 'KRANJ I': [173, 1.26], 'KRANJ II': [138, 1.03], 'KRANJ III': [93, 0.6], 'TRŽIČ': [116, 1.31], 'ŠKOFJA LOKA I': [87, 0.78], 'ŠKOFJA LOKA II': [48, 0.4], 'KAMNIK': [253, 1.48], 'IDRIJA': [57, 0.6]}, 'ZLSD': {'Skupaj': [17439, 12.67], 'JESENICE': [3364, 20.61], 'RADOVLJICA I': [1242, 12.82], 'RADOVLJICA II': [2030, 19.41], 'KRANJ I': [1794, 13.05], 'KRANJ II': [1506, 11.22], 'KRANJ III': [1105, 7.18], 'TRŽIČ': [1026, 11.61], 'ŠKOFJA LOKA I': [946, 8.53], 'ŠKOFJA LOKAII': [1002, 8.29], 'KAMNIK': [1308, 7.65], 'IDRIJA': [2116, 22.27]}, 'Dodatne informacije lahko dobite na volitve@gov.si': {}}

Ja, **je uporabna**, posebej za hitro iskanje v Pythonu:

```python
podatki["LDS"]["KRANJ II"]
```

ti vrne:

```python
[5140, 38.3]
```

Ampak ima tri manjše slabosti.

Prva: seznam `[4656, 3.38]` ni sam po sebi jasen. Ti veš, da je prvi element število glasov, drugi pa procent, ampak Python tega ne pove. Bolj berljivo bi bilo:

```python
podatki[stranka][okraj] = {
    "glasovi": 4656,
    "procent": 3.38
}
```

Potem dostopaš tako:

```python
podatki["DeSUS"]["Skupaj"]["glasovi"]
podatki["DeSUS"]["Skupaj"]["procent"]
```

Druga: imaš nekaj napak v imenih okrajev:

```python
"RADOVLJICAII"
"ŠKOFJA LOKAII"
```

namesto:

```python
"RADOVLJICA II"
"ŠKOFJA LOKA II"
```

To je nevarno, ker bo Python to razumel kot drug okraj. Verjetno se ti je to zgodilo zaradi `strip()` ali `split()`, ki ti je nekje pobral presledek med imenom in rimsko številko.

Tretja: v podatkih imaš še tole:

```python
'Dodatne informacije lahko dobite na volitve@gov.si': {}
```

To ni stranka, zato moraš takšne vrstice filtrirati ven.

Za nadaljnjo uporabo v CSV je najlepša oblika še vedno “ena vrstica = ena stranka v enem okraju”:

```python
vrstice = []

for stranka in podatki:
    for okraj in podatki[stranka]:
        glasovi = podatki[stranka][okraj][0]
        procent = podatki[stranka][okraj][1]

        vrstice.append({
            "stranka": stranka,
            "okraj": okraj,
            "glasovi": glasovi,
            "procent": procent
        })
```

Potem lahko to zelo enostavno zapišeš v CSV.

Če ostaneš pri trenutni obliki, je čisto v redu za šolski projekt. Jaz bi samo priporočal, da namesto seznama uporabiš slovar:

```python
podatki[stranka][okraj] = {
    "glasovi": int(vrednosti[0]),
    "procent": float(vrednosti[1])
}
```

Torej namesto:

```python
'RADOVLJICA I': [28, 0.29]
```

raje:

```python
'RADOVLJICA I': {
    'glasovi': 28,
    'procent': 0.29
}
```

Malo daljše, ampak precej bolj jasno in manj možnosti je, da kasneje zamenjaš `[0]` in `[1]`.

> kje tukaj misliš, da je problem, da so okraji preimenovani, kot si to izpostavil?:
>
> import re
> import csv
>
> with open("2000\\VE_1.html", encoding="utf-8") as dat:
>     table = dat.read()
>
> # splača se nam odstraniti vso odvečno solato, ki nam jo html pusti: značke, oznako &nbsp. To bom najlažje naredil z operatorjem replace
> def ocisti_html(niz):
>     niz = niz.replace("<br>", "\n")
>     niz = re.sub(r"<.*?>", "", niz)
>     niz = niz.replace("&nbsp;", "")
>     return niz.strip()
>
> # iz tabele izluščim vrstice, rad pa bi jih vse dal skupaj, ne pa obravnaval vsake posebej, zato bom uporabil re.findall, pri čemer obravnavam samo vsak teks znotraj značk <tr> in </tr>
>
> vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)
> print(len(vrstice))
>
> okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[4], flags=re.DOTALL)
> okraji = []
> for okraj in okraji_neocisceni[1:]:  # celica na položaju 0,0 v tabeli je prazna
>     okraji.append(ocisti_html(okraj))
> print(okraji)
>
> podatki = {}
> for vrstica in vrstice[7:]:
>     strankarski_rezultati = re.findall(r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL)
>     stranka = ocisti_html(strankarski_rezultati[0])
>     podatki[stranka] = {}
>
>     # rezultati po okrajih, kjer se sprehajamo skupaj po okraju in rezultatih v obliki <td>...</td>
>     for okraj, okraj_rezultat in zip(okraji, strankarski_rezultati[1:]):
>         vrednosti = (
>             ocisti_html(okraj_rezultat)
>             .replace(".", "")
>             .replace("%", "")
>             .replace(",", ".")
>             .split("\n")
>         )
>
>         glasovi = int(vrednosti[0])
>         procent = float(vrednosti[1])
>         podatki[stranka][okraj] = [glasovi, procent]
>
> print(podatki)

Problem je skoraj zagotovo tukaj:

```python
niz = niz.replace("&nbsp;", "")
```

S tem `&nbsp;` zamenjaš z **nič**, torej izbrišeš presledek.

Če ima HTML recimo:

```html
ŠKOFJA LOKA&nbsp;II
```

potem tvoja funkcija iz tega naredi:

```python
"ŠKOFJA LOKAII"
```

Namesto tega uporabi presledek:

```python
niz = niz.replace("&nbsp;", " ")
```

Torej:

```python
def ocisti_html(niz):
    niz = niz.replace("<br>", "\n")
    niz = re.sub(r"<.*?>", "", niz)
    niz = niz.replace("&nbsp;", " ")
    return niz.strip()
```

To je pomembno tudi pri procentih. Recimo:

```html
3,38&nbsp;%
```

bo postalo:

```python
"3,38 %"
```

kar je bolj pravilno kot:

```python
"3,38%"
```

Potem ti ta del še vedno deluje:

```python
.replace("%", "")
```

Druga stvar: če uporabljaš isti seznam `okraji` za vse stranke, potem bi morale imeti vse stranke enaka imena okrajev. Zato si takoj po tem delu dobro poglej:

```python
print(okraji)
```

Če tam vidiš:

```python
'ŠKOFJA LOKAII'
```

je napaka v čiščenju okrajev, torej v `ocisti_html`.

Še ena težava je tale rezultat:

```python
'Dodatne informacije lahko dobite na volitve@gov.si': {}
```

To se zgodi, ker greš z:

```python
for vrstica in vrstice[7:]:
```

čez vse vrstice do konca strani, tudi čez nogo strani. Dodaj preverjanje:

```python
for vrstica in vrstice[7:]:
    strankarski_rezultati = re.findall(r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL)

    if len(strankarski_rezultati) != len(okraji) + 1:
        continue
```

Tako obdelaš samo vrstice, ki imajo prvo celico za stranko in potem še po eno celico za vsak okraj.

> jaz imam 8 takih tabel za vseh 8 volilnih enot. žal se nekako podatki iz okrajev iz drugih tabel izbrišejo iz slovarja in ostane samo zadnja enota. tole je moja koda:
>
> import re
> import csv
>
> for enota in range(1, 9):
>     with open(f"2000\\VE_{enota}.html", encoding="utf-8") as dat:
>         table = dat.read()
>
>     # splača se nam odstraniti vso odvečno solato, ki nam jo html pusti: značke, oznako &nbsp. To bom najlažje naredil z operatorjem replace
>     def ocisti_html(niz):
>         niz = niz.replace("<br>", "\n")
>         niz = re.sub(r"<.*?>", "", niz)
>         niz = niz.replace("&nbsp;", " ")
>         return niz.strip()
>
>     # iz tabele izluščim vrstice, rad pa bi jih vse dal skupaj, ne pa obravnaval vsake posebej, zato bom uporabil re.findall, pri čemer obravnavam samo vsak teks znotraj značk <tr> in </tr>
>
>     vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)
>     print(len(vrstice))
>
>     okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[4], flags=re.DOTALL)
>     okraji = []
>     for okraj in okraji_neocisceni[
>         2:
>     ]:  # celica na položaju 0,0 v tabeli je prazna, stolpec 1 pa je označen kot glasovi skupaj po enoti, kar nas ne zanima
>         okraji.append(ocisti_html(okraj))
>     print(okraji)
>
>     podatki = {}
>     for vrstica in vrstice[7:]:
>         strankarski_rezultati = re.findall(
>             r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL
>         )
>         stranka = ocisti_html(strankarski_rezultati[0])
>         podatki[stranka] = {}
>
>         # rezultati po okrajih, kjer se sprehajamo skupaj po okraju in rezultatih v obliki <td>...</td>
>         for okraj, okraj_rezultat in zip(okraji, strankarski_rezultati[2:]):
>             vrednosti = (
>                 ocisti_html(okraj_rezultat)
>                 .replace(".", "")
>                 .replace(" %", "")
>                 .replace(",", ".")
>                 .replace("-", "0\n0")
>                 .split("\n")
>             )
>
>             glasovi = int(vrednosti[0])
>             procent = float(vrednosti[1])
>             podatki[stranka][okraj] = {"glasovi": glasovi, "procent": procent}

Problem je tukaj:

```python
podatki = {}
```

Ker je ta vrstica **znotraj** zanke:

```python
for enota in range(1, 9):
```

se slovar `podatki` pri vsaki novi volilni enoti ustvari na novo. Zato na koncu ostanejo samo podatki iz zadnje datoteke, torej iz `VE_8.html`.

Premakni ga **pred zanko**:

```python
podatki = {}

for enota in range(1, 9):
    with open(f"2000\\VE_{enota}.html", encoding="utf-8") as dat:
        table = dat.read()

    ...
```

Ampak imaš še drugi problem:

```python
podatki[stranka] = {}
```

Tudi to pri vsaki novi enoti povozi podatke iste stranke iz prejšnjih enot.

Namesto tega napiši:

```python
if stranka not in podatki:
    podatki[stranka] = {}
```

Celotna ideja:

```python
podatki = {}

for enota in range(1, 9):
    with open(f"2000\\VE_{enota}.html", encoding="utf-8") as dat:
        table = dat.read()

    vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)

    okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[4], flags=re.DOTALL)

    okraji = []
    for okraj in okraji_neocisceni[2:]:
        okraji.append(ocisti_html(okraj))

    for vrstica in vrstice[7:]:
        strankarski_rezultati = re.findall(
            r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL
        )

        if len(strankarski_rezultati) != len(okraji) + 2:
            continue

        stranka = ocisti_html(strankarski_rezultati[0])

        if stranka not in podatki:
            podatki[stranka] = {}

        for okraj, okraj_rezultat in zip(okraji, strankarski_rezultati[2:]):
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

            podatki[stranka][okraj] = {
                "glasovi": glasovi,
                "procent": procent
            }
```

Še bolj varno pa je, da vključiš tudi številko volilne enote, ker se lahko imena okrajev kdaj ponovijo ali pa bi rad kasneje vedel, od kod je podatek:

```python
podatki[stranka][f"VE {enota} - {okraj}"] = {
    "glasovi": glasovi,
    "procent": procent
}
```

Ali še lepše:

```python
podatki[stranka][okraj] = {
    "enota": enota,
    "glasovi": glasovi,
    "procent": procent
}
```

Ampak pri tej drugi možnosti bi se podatek povozil, če bi imela dva okraja enako ime. Zato je za tvojo trenutno strukturo bolj varno:

```python
podatki[stranka][f"VE {enota} - {okraj}"] = {
    "glasovi": glasovi,
    "procent": procent
}
```

Glavni popravek je torej:

```python
podatki = {}
```

mora biti **pred** `for enota in range(1, 9)`, in ne znotraj nje.

> preimenoval sem okraje v tipa 1001, 5007, 6010 etc in podatke spravil v podatki_koncni, kjer so samo stranke z glasovi v vseh 88 okrajih. pripravi mi nekje 10 ukazov tipa podatki_koncni['SDS']['2002'], da preverim, ali sem na koncu dobil prave podatke

Seveda. Daj si nekaj takih preverjanj, razpršenih čez različne stranke in različne volilne enote:

```python
print("SDS 2002:", podatki_koncni["SDS"]["2002"])
print("LDS 1005:", podatki_koncni["LDS"]["1005"])
print("NSi 3011:", podatki_koncni["NSi"]["3011"])
print("ZLSD 4010:", podatki_koncni["ZLSD"]["4010"])
print("SLS+SKD 5007:", podatki_koncni["SLS+SKD"]["5007"])
print("SNS 6010:", podatki_koncni["SNS"]["6010"])
print("DeSUS 7003:", podatki_koncni["DeSUS"]["7003"])
print("SMS 8011:", podatki_koncni["SMS"]["8011"])
print("NOVA 1001:", podatki_koncni["NOVA"]["1001"])
print("ZDRUŽENI ZELENI 8008:", podatki_koncni["ZDRUŽENI ZELENI"]["8008"])
```

Dodaj še ta dva za hitro strukturno preverjanje:

```python
print(len(podatki_koncni["SDS"]))        # pričakovano: 88
print(podatki_koncni.keys())             # preveri, katere stranke so ostale
```

Če želiš preveriti vse stranke naenkrat:

```python
for stranka in podatki_koncni:
    print(stranka, len(podatki_koncni[stranka]))
```

Pri vsaki stranki bi moral dobiti `88`.

> zdaj vse dela super. Hvala ti za vso pomoč. Rad bi to prevedel še na ostale volitve, a kar naenkrat dobim prazen slovar. Spodaj ti dajem svojo celotno kodo, pripel pa sem primer tabele iz leta 2004. Zakaj ne deluje?
>
> import re
> import csv
>
> podatki = {}
>
> # splača se nam odstraniti vso odvečno solato, ki nam jo html pusti: značke, oznako &nbsp. To bom najlažje naredil z operatorjem replace
> def ocisti_html(niz):
>     niz = niz.replace("<br>", "\n")
>     niz = re.sub(r"<.*?>", "", niz)
>     niz = niz.replace("&nbsp;", " ")
>     return niz.strip()
>
> for enota in range(1, 9):
>     with open(f"2004\\VE_{enota}.html", encoding="utf-8") as dat:
>         table = dat.read()
>
>     # iz tabele izluščim vrstice, rad pa bi jih vse dal skupaj, ne pa obravnaval vsake posebej, zato bom uporabil re.findall, pri čemer obravnavam samo vsak teks znotraj značk <tr> in </tr>
>
>     vrstice = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.DOTALL)
>
>     okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[4], flags=re.DOTALL)
>     okraji = []
>     for zap_st, okraj in enumerate(
>         okraji_neocisceni[2:], 1
>     ):  # celica na položaju 0,0 v tabeli je prazna, stolpec 1 pa je označen kot glasovi skupaj po enoti, kar nas ne zanima
>         st_okraja = f"{enota}00{zap_st}" if zap_st < 10 else f"{enota}0{zap_st}"
>         okraji.append(st_okraja)
>
>     for vrstica in vrstice[7:]:
>         strankarski_rezultati = re.findall(
>             r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL
>         )
>         stranka = ocisti_html(strankarski_rezultati[0])
>         if stranka not in podatki:
>             podatki[stranka] = {}
>
>         # rezultati po okrajih, kjer se sprehajamo skupaj po okraju in rezultatih v obliki <td>...</td>
>         for okraj, okraj_rezultat in zip(okraji, strankarski_rezultati[2:]):
>             vrednosti = (
>                 ocisti_html(okraj_rezultat)
>                 .replace(".", "")
>                 .replace(" %", "")
>                 .replace(",", ".")
>                 .replace("-", "0\n0")
>                 .split("\n")
>             )
>
>             glasovi = int(vrednosti[0])
>             procent = float(vrednosti[1])
>             podatki[stranka][okraj] = {"glasovi": glasovi, "procent": procent}
> podatki_koncni = {}
>
> for stranka in podatki.keys():
>     if len(podatki[stranka]) == 88:
>         podatki_koncni[stranka] = podatki[stranka]
> print(podatki_koncni)
>
> User context
>
> Attachments:
> - VE_4.html: `~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2004/VE_4.html`

<details><summary>5 previous messages</summary>

> Nice, glad the 2000 version is behaving. For 2004 I’ll look at the actual HTML structure first, because your code depends on fixed row positions like `vrstice[4]` and `vrstice[7:]`, and those are exactly the kind of thing that changes between years.
>
> I can already see a likely issue: 2004 has `<tr valign="top">`, so a plain `<tr>` pattern would fail, but your current pattern handles that. The next suspect is row numbering, so I’m checking which extracted rows actually contain the district header and party rows.
>
> Small tooling wrinkle: `python` is not on PATH in this shell. I’ll use the Windows Python launcher / installed path instead so we can still inspect without changing your files.
>
> The launcher is not available either, but PowerShell can do the same regex inspection. I’m using it just to print row indices, cell counts, and the first few cleaned cell texts.
>
> Found it. In this 2004 file the real header row is `vrstice[8]`, not `vrstice[4]`. Your `vrstice[4]` has only one cell, so `okraji_neocisceni[2:]` becomes empty, `okraji` becomes `[]`, and then every later `zip(okraji, ...)` does zero iterations.
</details>

Problem ni v regexu, ampak v indeksih vrstic.

V datoteki [VE_4.html](<~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2004/VE_4.html>) se prava tabela začne drugje kot leta 2000:

```python
vrstice[8]   # vrstica z okraji
vrstice[11]  # prva stranka
```

Ti pa uporabljaš:

```python
vrstice[4]
vrstice[7:]
```

Zato je tukaj:

```python
okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[4], flags=re.DOTALL)
```

`vrstice[4]` napačna vrstica. Ima samo eno celico, zato:

```python
okraji_neocisceni[2:]
```

postane prazen seznam. Posledično je tudi:

```python
okraji = []
```

In potem ta zanka ne naredi ničesar:

```python
for okraj, okraj_rezultat in zip(okraji, strankarski_rezultati[2:]):
```

ker je `okraji` prazen.

Za hiter popravek pri 2004 poskusi:

```python
okraji_neocisceni = re.findall(r"<td[^>]*>(.*?)</td>", vrstice[8], flags=re.DOTALL)
```

in:

```python
for vrstica in vrstice[11:]:
```

Še boljša rešitev pa je, da glave tabele ne iščeš po fiksni številki vrstice, ampak jo poiščeš:

```python
indeks_glave = None

for i, vrstica in enumerate(vrstice):
    celice = re.findall(r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL)
    besedila = [ocisti_html(celica) for celica in celice]

    if len(besedila) == 13 and besedila[1] == "Slovenija":
        indeks_glave = i
        break
```

Potem uporabiš:

```python
okraji_neocisceni = re.findall(
    r"<td[^>]*>(.*?)</td>",
    vrstice[indeks_glave],
    flags=re.DOTALL
)

okraji = []
for zap_st, okraj in enumerate(okraji_neocisceni[2:], 1):
    st_okraja = f"{enota}00{zap_st}" if zap_st < 10 else f"{enota}0{zap_st}"
    okraji.append(st_okraja)

for vrstica in vrstice[indeks_glave + 3:]:
    strankarski_rezultati = re.findall(
        r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL
    )

    if len(strankarski_rezultati) != len(okraji) + 2:
        continue

    stranka = ocisti_html(strankarski_rezultati[0])
```

Dodaj si še ta debug pred `podatki_koncni`, da vidiš, kaj se res dogaja:

```python
for stranka in podatki:
    print(stranka, len(podatki[stranka]))
```

Če vidiš same ničle, je problem pri `okraji`. Če vidiš številke manjše od `88`, potem ti zadnji filter vse odstrani:

```python
if len(podatki[stranka]) == 88:
```

> kaj bi bil problem za leto 2008 s to kodo?
>
> User context
>
> Attachments:
> - VE_4.html: `~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2008/VE_4.html`

<details><summary>2 previous messages</summary>

> Pogledal bom strukturo 2008 datoteke enako kot prej za 2004: koliko `<tr>` vrstic najde regex, katera vrstica je glava z okraji in kako izgledajo celice pri strankah. Pri teh starih HTML-jih je skoraj vedno krivec majhna sprememba v tabeli.
>
> Zanimivo: pri 2008 tvoja metoda z `<td>` vidi pri strankah samo 2 celici, ne 13. To pomeni, da ostali okrajni rezultati verjetno niso več v `<td>`, ampak v drugačnih oznakah ali celo v drugačni obliki tabele. Odpiram del HTML-ja okrog glavne tabele.
</details>

Za 2008 sta glavna problema v HTML strukturi:

1. Glava tabele uporablja `<th>`, ne `<td>`

Tvoja koda išče samo:

```python
re.findall(r"<td[^>]*>(.*?)</td>", vrstica, flags=re.DOTALL)
```

Ampak v 2008 je prva vrstica tabele približno:

```html
<tr>
  <th></th>
  <th>Slovenija</th>
  <th>VO 1<br />Kočevje</th>
  ...
</tr>
```

Zato z regexom za `<td>` ne dobiš imen okrajev.

2. HTML je malo pokvarjen: začne se s `<td>`, konča pa z `</th>`

Pri strankah je v 2008 nekaj takega:

```html
<td class="activpage"><div align="right">388<br />4,31&nbsp;%</div></th>
```

Začetna značka je `<td>`, zaključna pa napačno `</th>`. Zato tvoj regex:

```python
r"<td[^>]*>(.*?)</td>"
```

ujame samo prvi dve celici, ne pa vseh 13.

Zato dobiš pri stranki recimo samo:

```python
["DeSUS", "7.962 5,42 %"]
```

namesto vseh okrajev.

Popravek: uporabljaj regex, ki sprejme tako `<td>` kot `<th>` in tudi napačen zaključek:

```python
celice = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", vrstica, flags=re.DOTALL)
```

Ta del:

```python
t[dh]
```

pomeni: ujami `td` ali `th`.

Potem zamenjaj oba regexa za celice:

```python
okraji_neocisceni = re.findall(
    r"<t[dh][^>]*>(.*?)</t[dh]>",
    vrstice[indeks_glave],
    flags=re.DOTALL
)
```

in:

```python
strankarski_rezultati = re.findall(
    r"<t[dh][^>]*>(.*?)</t[dh]>",
    vrstica,
    flags=re.DOTALL
)
```

Še en popravek: leta 2008 je `<br />`, ne samo `<br>`, zato popravi čiščenje:

```python
def ocisti_html(niz):
    niz = re.sub(r"<br\s*/?>", "\n", niz)
    niz = re.sub(r"<.*?>", "", niz)
    niz = niz.replace("&nbsp;", " ")
    return niz.strip()
```

In verjetno odpri datoteko kot `windows-1250`, ker tako piše v HTML-ju:

```python
with open(f"2008\\VE_{enota}.html", encoding="windows-1250") as dat:
    table = dat.read()
```

Ključni problem pa je: **2008 nima več enakega HTML-ja kot 2000/2004**, zato tvoj regex za `<td>...</td>` izpusti večino celic.

> <br\s*/?> kaj to pomeni

To je regex za HTML prelom vrstice, ki ujame več oblik `<br>` značke.

```python
r"<br\s*/?>"
```

Pomen po delih:

```text
<      začetek značke
br     črki b in r
\s*    nič ali več presledkov
/?     nič ali en znak /
>      konec značke
```

Zato ujame vse te oblike:

```html
<br>
<br/>
<br />
<br   />
```

Uporabiš ga recimo tako:

```python
niz = re.sub(r"<br\s*/?>", "\n", niz)
```

To pomeni: vse HTML prelome vrstic zamenjaj s Python prelomom vrstice `\n`.

Zakaj ne samo:

```python
niz.replace("<br>", "\n")
```

Ker to ujame samo točno `<br>`, ne pa tudi `<br />`, ki se pogosto pojavlja v HTML-ju.

> Kako pa je s to datoteko?
>
> User context
>
> Attachments:
> - VE_5.html: `~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2011/VE_5.html`

<details><summary>2 previous messages</summary>

> Pogledal bom strukturo te 2011 datoteke tako kot pri 2008: ali uporablja `<td>` ali `<th>`, ali so zaključne značke pravilne, in kje se začne prava tabela. Pri teh datotekah se “ista” tabela očitno vsako leto malo preobleče.
>
> Tole za 2011 je zelo podobno kot 2008, samo z enim dodatnim opozorilom: datoteka v `<meta>` pravi `charset=windows-1250`, zato se slovenski znaki pokvarijo, če jo odpiraš z `utf-8`. Glavna tabela pa spet uporablja `<th>` v glavi in pokvarjene zaključne značke v podatkovnih celicah.
</details>

Pri 2011 je situacija skoraj ista kot pri 2008.

Glavni problemi:

```python
with open(..., encoding="utf-8")
```

Datoteka sama pravi:

```html
charset=windows-1250
```

Zato jo raje odpri tako:

```python
with open(f"2011\\VE_{enota}.html", encoding="windows-1250") as dat:
    table = dat.read()
```

Drugi problem: glava tabele uporablja `<th>`, ne `<td>`:

```html
<th>Slovenija</th>
<th>VO 1<br />Šentjur</th>
...
```

Tvoj regex išče samo `<td>...</td>`, zato glave ne najde pravilno.

Tretji problem: podatkovne celice so spet malo pokvarjene. Začnejo se s `<td>`, končajo pa z `</th>`:

```html
<td class="activpage"><div align="right">...</div></th>
```

Zato ta regex ni dovolj:

```python
r"<td[^>]*>(.*?)</td>"
```

Uporabi bolj splošnega:

```python
vzorec_celice = r"<t[dh][^>]*>(.*?)</t[dh]>"
```

To ujame tako `<td>` kot `<th>`, tudi če je zaključek čuden.

Popravi še `<br />`:

```python
def ocisti_html(niz):
    niz = re.sub(r"<br\s*/?>", "\n", niz)
    niz = re.sub(r"<.*?>", "", niz)
    niz = niz.replace("&nbsp;", " ")
    return niz.strip()
```

Za 2011 tudi ne uporabljaj več fiksno:

```python
vrstice[4]
```

Ker je pri tej datoteki glava tabele že bolj na začetku, približno `vrstice[0]`. Bolje jo poišči:

```python
vzorec_celice = r"<t[dh][^>]*>(.*?)</t[dh]>"

indeks_glave = None

for i, vrstica in enumerate(vrstice):
    celice = re.findall(vzorec_celice, vrstica, flags=re.DOTALL)
    besedila = [ocisti_html(celica) for celica in celice]

    if len(besedila) == 13 and besedila[1] == "Slovenija":
        indeks_glave = i
        break
```

Potem:

```python
okraji_neocisceni = re.findall(
    vzorec_celice,
    vrstice[indeks_glave],
    flags=re.DOTALL
)
```

In pri strankah:

```python
for vrstica in vrstice[indeks_glave + 3:]:
    strankarski_rezultati = re.findall(
        vzorec_celice,
        vrstica,
        flags=re.DOTALL
    )

    if len(strankarski_rezultati) != len(okraji) + 2:
        continue
```

Torej na kratko: za 2011 popravi `encoding`, uporabljaj `<t[dh]...>` namesto samo `<td...>`, popravi `<br />`, in glave tabele ne išči več z ročnim indeksom `4`.

> give me a quick check-list for 2008 to see whether the results came out ok

Here’s a quick 2008 sanity checklist you can run after building `podatki_koncni`.

```python
# 1. Which parties survived the "88 districts" filter?
print(podatki_koncni.keys())

# 2. Every included party should have 88 districts
for stranka in podatki_koncni:
    print(stranka, len(podatki_koncni[stranka]))

# 3. Check that all expected district codes exist
for stranka in podatki_koncni:
    for enota in range(1, 9):
        for okraj in range(1, 12):
            koda = f"{enota}00{okraj}" if okraj < 10 else f"{enota}0{okraj}"
            if koda not in podatki_koncni[stranka]:
                print("Missing:", stranka, koda)

# 4. Check types
print(type(podatki_koncni["SDS"]["4002"]["glasovi"]))
print(type(podatki_koncni["SDS"]["4002"]["procent"]))
```

Some spot checks from `2008/VE_4.html` should be:

```python
print(podatki_koncni["SDS"]["4002"])      # {'glasovi': 3579, 'procent': 48.29}
print(podatki_koncni["SDS"]["4003"])      # {'glasovi': 10139, 'procent': 51.08}
print(podatki_koncni["SD"]["4001"])       # {'glasovi': 4197, 'procent': 46.62}
print(podatki_koncni["DeSUS"]["4008"])    # {'glasovi': 1011, 'procent': 6.02}
print(podatki_koncni["ZARES"]["4009"])    # {'glasovi': 2608, 'procent': 17.42}
print(podatki_koncni["NSi"]["4010"])      # {'glasovi': 894, 'procent': 5.91}
print(podatki_koncni["LDS"]["4003"])      # {'glasovi': 991, 'procent': 4.99}
print(podatki_koncni["SLS+SMS"]["4004"])  # {'glasovi': 837, 'procent': 7.87}
print(podatki_koncni["SNS"]["4011"])      # {'glasovi': 701, 'procent': 4.87}
print(podatki_koncni["Zeleni"]["4010"])   # {'glasovi': 78, 'procent': 0.52}
```

Also check this:

```python
print(podatki_koncni.get(""))
```

It should print:

```python
None
```

If it prints data, you accidentally parsed an empty party name.

> Veš, kako pridejo ven podatki v obliki python slovarja. To bi rabil obrniti v uporabno datoteko CSV, oblike, kot je priložena. Kako to naredim, če rabim za začetek surfati samo po procentih (zaenkrat).
>
> User context
>
> Attachments:
> - rezultati2022.csv: `~/OneDrive/Dokumenti/FMF/racunalnistvo/UVP/PROJEKT - VOLITVE/2022/rezultati2022.csv`

<details><summary>2 previous messages</summary>

> Uporabil bom spreadsheet navodila, ker gre za pretvorbo v CSV in želim ujeti obliko priložene datoteke. Najprej pogledam pravila za delo s preglednicami, potem pa še glavo oziroma prvih nekaj vrstic tvojega CSV-ja.
>
> Zdaj bom pogledal še strukturo priloženega `rezultati2022.csv`: predvsem imena stolpcev in ali so okraji po stolpcih ali po vrsticah. To nam pove, ali moramo tvoj slovar “razširiti” po strankah ali po okrajih.
</details>

Priloženi CSV ima obliko:

```csv
OKRAJ,DeSUS,DOM,Resni.ca,...
1001,0.0077,0.0048,0.0571,...
1002,0.0045,0.0047,0.0287,...
```

Torej: **vrstice so okraji**, **stolpci so stranke**, v celicah pa so procenti zapisani kot deleži:

```python
34.89 % -> 0.3489
3.38 %  -> 0.0338
```

Če imaš podatke v obliki:

```python
podatki_koncni["SDS"]["4002"]["procent"]
```

potem lahko CSV narediš tako:

```python
import csv

stranke = list(podatki_koncni.keys())

okraji = []
for enota in range(1, 9):
    for zap_st in range(1, 12):
        if zap_st < 10:
            okraj = f"{enota}00{zap_st}"
        else:
            okraj = f"{enota}0{zap_st}"
        okraji.append(okraj)

with open("rezultati2008.csv", "w", encoding="utf-8", newline="") as dat:
    pisec = csv.writer(dat)

    pisec.writerow(["OKRAJ"] + stranke)

    for okraj in okraji:
        vrstica = [okraj]

        for stranka in stranke:
            procent = podatki_koncni[stranka][okraj]["procent"]
            delez = procent / 100
            vrstica.append(round(delez, 4))

        pisec.writerow(vrstica)
```

Ključna vrstica je ta:

```python
delez = procent / 100
```

Ker imaš v slovarju verjetno:

```python
29.53
```

v CSV-ju pa želiš:

```python
0.2953
```

Če bi raje imel v CSV-ju `29.53` namesto `0.2953`, potem samo odstraniš deljenje s 100:

```python
vrstica.append(procent)
```

Ampak glede na priloženi `rezultati2022.csv` je prava oblika `0.2953`.

> what does vrstica = [okraj] mean

This line:

```python
vrstica = [okraj]
```

creates a new list with one element inside it: the current district code.

For example, if:

```python
okraj = "4002"
```

then:

```python
vrstica = [okraj]
```

means:

```python
vrstica = ["4002"]
```

Why do this? Because you are building one CSV row. The first cell should be the district code, and then you append percentages for each party:

```python
vrstica = [okraj]

for stranka in stranke:
    procent = podatki_koncni[stranka][okraj]["procent"]
    delez = procent / 100
    vrstica.append(delez)
```

So after the loop, `vrstica` might look like:

```python
["4002", 0.4829, 0.1857, 0.0421]
```

Then you write that whole row into the CSV:

```python
pisec.writerow(vrstica)
```

So in plain words:

```python
vrstica = [okraj]
```

means: “Start this CSV row with the district code.”

> File "C:\Users\Uporabnik\OneDrive\Dokumenti\FMF\racunalnistvo\UVP\PROJEKT - VOLITVE\mogocezdaj.py", line 90, in <module>
>     procent = podatki_koncni[stranka][okraj]["procent"]
>               ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
> TypeError: 'int' object is not subscriptable

Ta napaka pomeni, da je tole:

```python
podatki_koncni[stranka][okraj]
```

nekje samo `int`, ne pa slovar.

Ti pričakuješ obliko:

```python
podatki_koncni["SDS"]["4002"] = {
    "glasovi": 3579,
    "procent": 48.29
}
```

ampak očitno imaš zdaj obliko približno:

```python
podatki_koncni["SDS"]["4002"] = 48.29
```

ali mogoče:

```python
podatki_koncni["SDS"]["4002"] = 3579
```

Zato ta del ne dela:

```python
["procent"]
```

ker pri številu ne moreš iskati ključa `"procent"`.

Najprej preveri obliko:

```python
print(podatki_koncni["SDS"]["4002"])
print(type(podatki_koncni["SDS"]["4002"]))
```

Če izpiše recimo:

```python
48.29
<class 'float'>
```

potem moraš uporabiti:

```python
procent = podatki_koncni[stranka][okraj]
```

Če izpiše recimo:

```python
3579
<class 'int'>
```

potem si v slovar shranil samo glasove, ne procentov.

Za CSV del imaš torej dve možnosti.

Če imaš podatke tako:

```python
podatki_koncni["SDS"]["4002"] = {
    "glasovi": 3579,
    "procent": 48.29
}
```

uporabiš:

```python
procent = podatki_koncni[stranka][okraj]["procent"]
```

Če imaš podatke tako:

```python
podatki_koncni["SDS"]["4002"] = 48.29
```

uporabiš:

```python
procent = podatki_koncni[stranka][okraj]
```

Za tvoj error je zelo verjetno pravilen popravek:

```python
procent = podatki_koncni[stranka][okraj]
delez = procent / 100
vrstica.append(round(delez, 4))
```

Dodaj si mini debug:

```python
for stranka in podatki_koncni:
    for okraj in podatki_koncni[stranka]:
        print(stranka, okraj, podatki_koncni[stranka][okraj], type(podatki_koncni[stranka][okraj]))
        break
    break
```

To ti pokaže točno, kakšna je notranja oblika slovarja.

> would you say this is a good solution:
>
> for stranka in stranke:
>     if type(podatki_koncni[stranka]) != "<class 'dict'>":
>           remove stranka from podatki_koncni

Not quite. Two issues:

First, `type(...)` returns a type object, not a string, so this is wrong:

```python
type(podatki_koncni[stranka]) != "<class 'dict'>"
```

It would need to be:

```python
type(podatki_koncni[stranka]) != dict
```

or better:

```python
not isinstance(podatki_koncni[stranka], dict)
```

Second, your error probably is **not** that:

```python
podatki_koncni[stranka]
```

is an `int`.

The error says this part is an `int`:

```python
podatki_koncni[stranka][okraj]
```

So the outer value may still be a dictionary, but the value for one district is just a number.

You should check the inner value:

```python
for stranka in stranke:
    for okraj in podatki_koncni[stranka]:
        if not isinstance(podatki_koncni[stranka][okraj], dict):
            print(stranka, okraj, podatki_koncni[stranka][okraj])
```

Also, don’t remove items from a dictionary while looping over it directly. Instead loop over a copy:

```python
for stranka in list(podatki_koncni.keys()):
    if not isinstance(podatki_koncni[stranka], dict):
        del podatki_koncni[stranka]
```

But for your case, I would not delete anything yet. First inspect:

```python
for stranka in podatki_koncni:
    for okraj in podatki_koncni[stranka]:
        vrednost = podatki_koncni[stranka][okraj]
        if not isinstance(vrednost, dict):
            print(stranka, okraj, vrednost, type(vrednost))
```

If it prints values like:

```python
SDS 4002 48.29 <class 'float'>
```

then your data is already just percentages, and your CSV line should be:

```python
procent = podatki_koncni[stranka][okraj]
```

not:

```python
procent = podatki_koncni[stranka][okraj]["procent"]
```

> ko tole poženem, vse deluje, ampak če večkrat zaporedoma poženem podatki\_v\_csv(leto) za leta 2000, 2004, 2008, 2011, 2014; se seznam strank v ustvarjeni csv datoteki samo podaljšuje in se samo dodajajo:
>
> import re
> import csv
> \
> podatki = {}
> \
> okraji\_index = {"2000": 4, "2004": 8, "2008": 0, "2011": 0, "2014": 0}
> vrstice\_index = {"2000": 7, "2004": 11, "2008": 3, "2011": 3, "2014": 3}
> \
> \
> *# splača se nam odstraniti vso odvečno solato, ki nam jo html pusti: značke, oznako &nbsp. To bom najlažje naredil z operatorjem replace*
> def ocisti\_html(niz):
>     niz = re.sub(r"\<br\s\*/?>", "\n", niz)
>     niz = re.sub(r"<.\*?>", "", niz)
>     niz = niz.replace("&nbsp;", " ")
>     return niz.strip()
> \
> \
> def pridobitev\_podatkov(leto):
>     if leto not in [2000, 2004, 2008, 2011, 2014]:
>         return "Neveljavno leto. Državnozborkse volitve so potekale leta 2000, 2004, 2008, 2011 in 2014."
>     for enota in range(1, 9):
>         with open(f"{leto}\\\VE\_{enota}.html", encoding="UTF-8") as dat:
>             table = dat.read()
> \
>         *# iz tabele izluščim vrstice, rad pa bi jih vse dal skupaj, ne pa obravnaval vsake posebej, zato bom uporabil re.findall, pri čemer obravnavam samo vsak teks znotraj značk \<tr> in \</tr>*
> \
>         vrstice = re.findall(r"\<tr[^>]\*>(.\*?)\</tr>", table, flags=re.DOTALL)
> \
>         okraji\_neocisceni = re.findall(
>             r"\<t[dh][^>]\*>(.\*?)\</t[dh]>",
>             vrstice[okraji\_index[f"{leto}"]],
>             flags=re.DOTALL,
>         )
> \
>         okraji = []
>         for zap\_st, okraj in enumerate(
>             okraji\_neocisceni[2:], 1
>         ):  *# celica na položaju 0,0 v tabeli je prazna, stolpec 1 pa je označen kot glasovi skupaj po enoti, kar nas ne zanima*
>             st\_okraja = f"{enota}00{zap\_st}" if zap\_st < 10 else f"{enota}0{zap\_st}"
>             okraji.append(st\_okraja)
> \
>         for vrstica in vrstice[vrstice\_index[f"{leto}"] :]:
>             strankarski\_rezultati = re.findall(
>                 r"\<t[dh][^>]\*>(.\*?)\</t[dh]>", vrstica, flags=re.DOTALL
>             )
>             stranka = ocisti\_html(strankarski\_rezultati[0])
>             if stranka not in podatki:
>                 podatki[stranka] = {}
> \
>             *# rezultati po okrajih, kjer se sprehajamo skupaj po okraju in rezultatih v obliki \<td>...\</td>, številka 2 je tam, ker se sprehajamo od tretjega stolpca naprej, saj sta prva ime stranka, drugi pa število vseh glasov*
>             for okraj, okraj\_rezultat in zip(okraji, strankarski\_rezultati[2:]):
>                 vrednosti = (
>                     ocisti\_html(okraj\_rezultat)
>                     .replace(".", "")
>                     .replace(" %", "")
>                     .replace(",", ".")
>                     .replace("-", "0\n0")
>                     .split("\n")
>                 )
> \
>                 glasovi = int(vrednosti[0])
>                 procent = float(vrednosti[1])
>                 podatki[stranka][okraj] = {"glasovi": glasovi, "procent": procent}
>     podatki\_koncni = {}
> \
>     for stranka in podatki.keys():
>         if len(podatki[stranka]) == 88:
>             podatki\_koncni[stranka] = podatki[stranka]
> \
>     *# pri letih 2004 in 2000 moj rezalnik ujame še nekaj ključev v slovar, ki niso stranke (npr.: 'Dodatne informacije na rvk\@gov.si': 0), zato se bom sprehodil po ključih slovarja in če njegova vrednost ni slovar, izbrisal vnos*
> \
>     for stranka in podatki\_koncni.keys():
>         if type(podatki\_koncni[stranka]) != dict:
>             podatki\_koncni.pop(stranka)
>     return podatki\_koncni
> \
>  *# sprememba v CSV*
> \
> def podatki\_v\_csv(leto):
>     okraji = []
>     for enota in range(1, 9):
>         for zap\_st in range(1, 12):
>             if zap\_st < 10:
>                 okraji.append(f"{enota}00{zap\_st}")
>             else:
>                 okraji.append(f"{enota}0{zap\_st}")
> \
>     stranke = list(pridobitev\_podatkov(leto).keys())
> \
>     with open(
>         f"rezultati{leto}\_procenti.csv", "w", encoding="utf-8", newline=""
>     ) as dat:
>         pisec = csv.writer(dat)
> \
>         pisec.writerow(["OKRAJ"] + stranke)
> \
>         for okraj in okraji:
>             vrstica = []
>             vrstica.append(okraj)
> \
>             for stranka in stranke:
>                 procent = pridobitev\_podatkov(leto)[stranka][okraj]["procent"]
>                 delez = procent / 100
>                 vrstica.append(round(delez, 4))
> \
>             pisec.writerow(vrstica)
>     return f"Preveri datoteko 'rezultati{leto}\_procenti.csv'"

Problem je globalni slovar:

```python
podatki = {}
```

Ker je zunaj funkcije, se **ne ustvari na novo** pri vsakem klicu. Če najprej poženeš:

```python
podatki_v_csv(2000)
```

se v `podatki` shranijo stranke iz 2000. Potem poženeš:

```python
podatki_v_csv(2004)
```

in se stranke iz 2004 samo dodajo v isti slovar. Zato se seznam strank v CSV podaljšuje.

Najboljši popravek: premakni `podatki = {}` v funkcijo `pridobitev_podatkov`.

```python
def pridobitev_podatkov(leto):
    podatki = {}

    if leto not in [2000, 2004, 2008, 2011, 2014]:
        return "Neveljavno leto."

    for enota in range(1, 9):
        ...
```

Drugi pomemben problem je tukaj:

```python
stranke = list(pridobitev_podatkov(leto).keys())
```

in potem kasneje:

```python
procent = pridobitev_podatkov(leto)[stranka][okraj]["procent"]
```

S tem funkcijo `pridobitev_podatkov(leto)` kličeš znova in znova. Raje jo pokliči samo enkrat:

```python
def podatki_v_csv(leto):
    okraji = []
    for enota in range(1, 9):
        for zap_st in range(1, 12):
            if zap_st < 10:
                okraji.append(f"{enota}00{zap_st}")
            else:
                okraji.append(f"{enota}0{zap_st}")

    podatki_koncni = pridobitev_podatkov(leto)
    stranke = list(podatki_koncni.keys())

    with open(f"rezultati{leto}_procenti.csv", "w", encoding="utf-8", newline="") as dat:
        pisec = csv.writer(dat)
        pisec.writerow(["OKRAJ"] + stranke)

        for okraj in okraji:
            vrstica = [okraj]

            for stranka in stranke:
                procent = podatki_koncni[stranka][okraj]["procent"]
                delez = procent / 100
                vrstica.append(round(delez, 4))

            pisec.writerow(vrstica)

    return f"Preveri datoteko 'rezultati{leto}_procenti.csv'"
```

Torej glavna dva popravka sta:

```python
podatki = {}
```

naj bo **znotraj** `pridobitev_podatkov`, in:

```python
podatki_koncni = pridobitev_podatkov(leto)
```

naj se v `podatki_v_csv` zgodi samo enkrat. Tako bo vsako leto obdelano posebej in se stranke ne bodo več kopičile iz prejšnjih klicev.
