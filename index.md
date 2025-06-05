# Generatiivisen tekoälyn ja ohjelmistorobotiikan ohjelmointiteknologioiden perusteet

**!! Tämä osio tarjoaa avaimet kurssin harjoitustyön tekemiseen. Harjoitustyön ohjeen löytyvät [täältä](tehtava.md). Tehtävä palautetaan ohjeiden mukaisesti [Moodleen](https://moodle.seamk.fi/mod/assign/view.php?id=1400266).**

**Aikataulu**. Palautetut työt arvioidaan perjantaina 13. kesäkuuta. Mikäli palautettavien töiden (harjoitustyö ja itsearviointi) palautus viivästyy tästä, venyy arviointi Elokuulle.

## Sisällysluettelo

- [Generatiivisen tekoälyn ja ohjelmistorobotiikan ohjelmointiteknologioiden perusteet](#generatiivisen-tekoälyn-ja-ohjelmistorobotiikan-ohjelmointiteknologioiden-perusteet)
  - [Sisällysluettelo](#sisällysluettelo)
  - [Johdanto](#johdanto)
  - [Sanakirja](#sanakirja)
    - [Lyhyesti Pythonin muista kokoelmatyypeistä](#lyhyesti-pythonin-muista-kokoelmatyypeistä)
  - [JavaScript Object Notation (JSON)](#javascript-object-notation-json)
      - [Json-datan lukeminen Pythonissa](#json-datan-lukeminen-pythonissa)
      - [Json-datan kirjoittaminen Pythonissa](#json-datan-kirjoittaminen-pythonissa)
  - [Tiedostojen käsittely](#tiedostojen-käsittely)
    - [CSV-tiedoston lukeminen](#csv-tiedoston-lukeminen)
  - [HTML, CSS ja JavaScript](#html-css-ja-javascript)
  - [HTTP ja Rajapinnat (API)](#http-ja-rajapinnat-api)
    - [Flask - Pythonin WWW-palvelin](#flask---pythonin-www-palvelin)

## Johdanto

Tällä kurssin osalla emme käsittele monimutkaisia tekoälyalgoritmeja, vaan rakennamme ymmärrystä verkkoteknologioista, sekä syvennämme perustason ohjelmointitaitoa aiheilla, jotka on välttämättömiä ohjelmistorobotiikan ja tekoälynpalveluiden ohjelmallisessa hyödyntämisessä.

**Python-sanakirjat ja JSON (JavaScript Object Notation):**
Opitte, miten Python-sanakirjoja käytetään tehokkaasti datan strukturointiin ja miten JSON-muoto mahdollistaa datan vaihdon eri järjestelmien ja sovellusten välillä.

Python-sanakirjat ovat tietorakenteita, jotka tallentavat dataa avain-arvo -pareina, mahdollistaen jäsennellyn tiedon käsittelyn ohjelman sisällä. JSON (JavaScript Object Notation) on kevyt, tekstipohjainen tiedonvaihtomuoto, joka on hyvin samanlainen rakenteeltaan ja jota käytetään laajasti datan siirtoon eri järjestelmien välillä. Pythonissa on erittäin helppoa muuntaa Python-sanakirja JSON-merkkijonoksi ja päinvastoin käyttämällä sisäänrakennettua json-moduulia, mikä on keskeistä datan käsittelyssä tekoälyprojekteissa.

**Tiedostojen käsittely:**
Tiedostot ovat tietokoneelle tallennettuja nimettyjä tietokokonaisuuksia, jotka voivat sisältää esimerkiksi tekstiä, kuvia, ohjelmakoodia tai strukturoitua dataa. Ohjelmallinen tiedostojen käsittely tarkoittaa kykyä lukea tietoa tiedostoista ja kirjoittaa uutta tietoa niihin ohjelmakoodin avulla, ilman manuaalista avaamista ja muokkaamista. Esimerkiksi ohjelmistorobotiikassa (RPA) tämä on erittäin hyödyllistä: botti voi automaattisesti lukea käsiteltävät tiedot vaikkapa Excel-tiedostosta, CSV-tiedostosta tai lokitiedostosta, suorittaa niiden perusteella tehtäviä ja lopuksi kirjoittaa tulokset tai raportin uuteen tiedostoon, tehostaen ja automatisoiden rutiininomaisia prosesseja.

**Web-teknologiat (WWW):**
Monet tekoälysovellukset ovat web-pohjaisia tai hyödyntävät web-rajapintoja datan keräämiseen tai tulosten esittämiseen. Perehdymme:
*   **HTML, CSS ja JavaScript:** Näiden avulla ymmärrätte, miten web-sivut toimivat.
 *   **HTTP ja Rajapinnat (API):** Opitte, miten data liikkuu verkossa HTTP-protokollan avulla ja miten voitte hyödyntää ulkoisia rajapintoja (API) datan hakemiseen. Monet tekoälypalvelut (esim. kuvantunnistus, kielenkäsittely) ovat saatavilla API-rajapintojen kautta.

Tavoitteenamme on, että kurssin jälkeen ette ainoastaan ymmärrä näitä teknologioita teoreettisesti, vaan osaatte myös soveltaa niitä käytännössä.

## Sanakirja

Tarkempi kuvaus sanakirjasta löytyy jo tutuksi tulleesta **[mooc.fi materiaalista tämän linkin takaa](https://ohjelmointi-25.mooc.fi/osa-5/3-dictionary)**.

Me käytämme Pythonin **sanakirjoja (`dictionaries`)** **JSON-pohjaisten API-kutsujen (JSON-based API calls)** yhteydessä. JSON (JavaScript Object Notation) on yleinen tiedonvaihtomuoto web-sovellusten välillä, ja sen rakenne (avain-arvo -parit) vastaa lähes täydellisesti Pythonin sanakirjoja. Tämä tekee JSON-datan käsittelystä Pythonissa erittäin suoraviivaista: JSON-objekti voidaan helposti muuntaa Python-sanakirjaksi ja päinvastoin.

### Lyhyesti Pythonin muista kokoelmatyypeistä

Sanakirjat ovat Pythonissa äärimmäisen hyödyllisiä ja monikäyttöisiä myös monissa muissa tilanteissa. Pythonissa on myös muista sisäänrakennettuja kokoelmatietotyyppejä (collection data types), jotka auttavat organisoimaan ja käsittelemään dataa.

1.  **List (lista)** sisältää arvoja numerojärjestyksessä
    *   **Syntaksi:** Määritellään hakasulkeilla `[]`.
    *   **Esimerkki:** `nimet = ["Maija", "Pekka", "Liisa"]`, `numerot = [1, 5, 2, 5]`

2.  **Dictionary (sanakirja)** sisältää arvoja joihin viitataan avaimella
    *   **Syntaksi:** Määritellään aaltosulkeilla `{}` ja avain-arvo -parit erotellaan kaksoispisteellä `:`.
    *   **Esimerkki:** `henkilo = {"nimi": "Matti", "ikä": 30, "kaupunki": "Helsinki"}`

3.  **Set (joukko)** ei voi sisältää samaa arvoa kahta kertaa
    *   **Syntaksi:** Määritellään aaltosulkeilla `{}`. Huomaa, että tyhjä joukko luodaan `set()`-funktiolla, sillä `{}` luo tyhjän sanakirjan.
    *   **Esimerkki:** `hedelmat = {"omena", "banaani", "appelsiini"}`, `numerot_joukko = {1, 2, 3, 2}` (tulostuu `{1, 2, 3}`)

4.  **Tuple (monikko)** kuin lista, mutta tehokkaampi tietyissä tilanteissa
    *   **Syntaksi:** Määritellään sulkeilla `()` tai usein jopa ilman niitä, pelkillä pilkuilla erotelluilla arvoilla. Yhden alkion monikko vaatii pilkun peräänsä, esim. `(1,)` tai `1,`.
    *   **Esimerkki:** `koordinaatit = (10, 20)`, `vari_rgb = 255, 128, 0`, `yksi_alkio = ("a",)`

## JavaScript Object Notation (JSON)

[Wikipedia](https://fi.wikipedia.org/wiki/JSON) kertoo että JSON on avoin tiedostomuoto joka on osa JavaScript -standardia. [Englanninkielinen Wikipedia](https://en.wikipedia.org/wiki/JSON) taustoittaa asiaa vielä paremmin. Soveltavampaa tietoa löytyy mm. [RealPythonin](https://realpython.com/python-json/) ja [w3schools](https://www.w3schools.com/python/python_json.asp):in tutoriaaleista.

Meille riittää toistaiseksi tietää että JSON on internetin yleisin koneluettava tiedosiirtoformaatti, ja että sen hyödyntäminen Pythonissa on melko suoraviivaista.

#### Json-datan lukeminen Pythonissa

Alla oleva koodi konvertoi merkkijonona olevan JSON-datan pythonin sanakirjaksi, ja tulostaa datasta löytyvän nimen.

```python
import json
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
dictionary = json.loads(json_string)
print("Nimi:", dictionary["name"])
```

Tulostuu: `Nimi: Alice`

#### Json-datan kirjoittaminen Pythonissa

Alla luodaan Python-sanakirja, joka muunnetaan JSON-muotoon:

```python
import json
ransukoira = {} # luodaan tyhjä sanakirja
ransukoira["nimi"] = "Ransu"
ransukoira["ika"] = 5
ransukoira["rotu"] = "Karvakuono"
ransukoira["kaverit"] = ["Eno-Elmeri", "Riku"] # lista
json_result = json.dumps(ransukoira, indent=4)
print(json_result)
```

Tulostuu:
```json
{
    "nimi": "Ransu",
    "ika": 5,
    "rotu": "Karvakuono",
    "kaverit": [
        "Eno-Elmeri",
        "Riku"
    ]
}
```

**Huom!** Ylläolevassa koodissa `import json` tuo json-toiminnallisuuden (kirjaston) koodimme käyttöön. Ilman import-lausetta, koodi ei toimisi. Vaikka json-toiminnallisuus on virallinen osa Pythonia, sitä ei automaattisesti ladata käyttöön. Sama pätee moniin muihinkin kirjastoihin, kuten jatkossa käyttämiimme sys- ja flask-kirjastoihin.  


## Tiedostojen käsittely

Tiedostojen käsittelemisestä Pythonissa löytyy kosolti tietoa internetistä. Siitä kerrotaan mm. [Mooc-materiaalin osassa 6](https://ohjelmointi-25.mooc.fi/osa-6). [Mooc:in osio 7.4](https://ohjelmointi-25.mooc.fi/osa-7/4-datan-kasittely) kertoo lyhyesti sekä JSON- ja CSV-tiedostojen käsittelystä. Hyvää tietoa aiheesta tarjoilee [DigitalOcean](https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy), [GeeksForGeeks](https://www.geeksforgeeks.org/file-handling-python/), [W3Schools](https://www.w3schools.com/PYTHON/python_file_handling.asp) sekä Python-projektin oma [tutoriaali](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) ja [manuaali](https://docs.python.org/3/library/filesys.html).

Json-tiedostoja voi käsitellä esimerkiksi näin. Koodi generoi data.json nimisen tiedoston jonka sisältö on sama kuin koodiesimerkin alussa data-nimisen muuttujan sisältö:
```python
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Kirjoita JSON tiedosto
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Lue JSON tiedosto
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Tulosta JSON-data
print(loaded_data)
```

Tämä on esimerkki ison tiedoston lukemisesta rivi kerrallaan.
Tällä tavalla vältetään koko tiedoston lataaminen muistiin kerralla,
mikä on tärkeää, jos tiedosto on erittäin suuri.

```python
with open('large_example.txt', 'r') as file:  # Avataan tiedosto lukutilassa.
    for line in file:  # Käydään tiedoston rivit läpi yksi kerrallaan.
        print(line, end='')  # Tulostetaan rivi ilman ylimääräistä rivinvaihtoa.
```
Vaikka Pythonin syntaksi ylläolevassa esimerkissä `for line in file:` on hyvin ytimekäs ja saattaa antaa vaikutelman, että koko tiedosto olisi jotenkin jo valmiiksi käsittelyssä, se on itse asiassa erittäin optimoitu ja muistiystävällinen tapa käsitellä tiedostoja. Pythonin tiedosto-objekti toimii tässä yhteydessä **iteraattorina**, joka tuottaa yhden rivin kerrallaan pyydettäessä. 


### CSV-tiedoston lukeminen
CSV (Comma-Separated Values) on tiedostomuoto, jossa data tallennetaan tekstimuotoisena riveittäin, ja sarakkeiden arvot erotellaan toisistaan pilkuilla (tai muilla erotinmerkeillä, kuten puolipisteillä). Taulukkolaskentaohjelmat kuten Excel osaavat lukea ja tallentaa CSV-tiedostoja.

Alla olevassa koodiesimerkissä luetaan toiveet.csv-tiedostosta neljän sarakkeen (id,name,description,img-path) tiedot. Voit hyödyntää tätä esimerkkiä kurssin harjoitustyössä:

```python
import csv
with open('toiveet.csv', mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row['id'], row['name'], row['description'], row['img-path'])
```

## HTML, CSS ja JavaScript

Nämä kolme teknologiaa muodostavat modernien verkkosivujen ja -sovellusten perustan. Niiden ymmärtäminen on tärkeää, kun työskennellään web-pohjaisten tekoälypalveluiden kanssa tai kun ohjelmistorobotti automatisoi tehtäviä verkkoselaimessa.

**Web-sovelluksen toimintaperiatteista** löytyy hyvä selostus Helsingin yliopiston [Full Stack open -kurssin materiaaleista](https://fullstackopen.com/osa0/web_sovelluksen_toimintaperiaatteita).

*   **HTML (HyperText Markup Language):**
    HTML on merkkauskieli, jota käytetään verkkosivujen rakenteen ja sisällön määrittelemiseen. HTML-elementit, kuten otsikot (`<h1>`), kappaleet (`<p>`), linkit (`<a>`) ja kuvat (`<img>`), muodostavat sivun perusrakenteen. Ohjelmistorobotiikassa HTML-rakenteen ymmärtäminen on keskeistä, kun botti etsii ja käsittelee tietoa verkkosivuilta (esim. tunnistaa täytettävät kentät tai klikattavat painikkeet).
    *   Hyvä johdanto HTML:ään löytyy esimerkiksi [W3Schoolsista](https://www.w3schools.com/html/).

*   **CSS (Cascading Style Sheets):**
    CSS:n avulla määritellään HTML-dokumenttien ulkoasu ja esitystapa. CSS:llä hallitaan esimerkiksi värejä, fontteja, asettelua ja elementtien sijoittelua. Vaikka CSS ei ole suoraan vuorovaikutuksessa datan kanssa kuten HTML tai JavaScript, sen ymmärtäminen auttaa hahmottamaan, miksi verkkosivut näyttävät siltä kuin näyttävät ja miten visuaaliset elementit on järjestetty.
    *   CSS-perusteisiin voi tutustua [W3Schoolsissa](https://www.w3schools.com/css/).

*   **JavaScript:**
    JavaScript on ohjelmointikieli, joka tuo verkkosivuille interaktiivisuutta ja dynaamisuutta. Se on kuin talon sähköjärjestelmä ja liikkuvat osat, jotka mahdollistavat toiminnallisuuden. JavaScriptillä voidaan esimerkiksi validoida lomakkeiden syötteitä, luoda animaatioita, muokata sivun sisältöä lennosta ilman sivun uudelleenlatausta (AJAX) ja kommunikoida palvelimien kanssa (esim. API-kutsut). Monet nykyaikaiset verkkosivut ja -sovellukset, mukaan lukien tekoälypalveluiden käyttöliittymät, hyödyntävät JavaScriptiä laajasti. RPA-bottien tulee joskus osata odottaa JavaScriptillä ladattavaa sisältöä tai jopa suorittaa JavaScript-komentoja selaimessa.
    *   JavaScriptin perusteet löytyvät hyvin selitettynä [W3Schoolsista](https://www.w3schools.com/js/).


## HTTP ja Rajapinnat (API)

Hyvä suomenkielinen kuvaus HTTP-protokollasta löytyy [Mooc Web-Palvelinohjelmointi -kurssin materiaalin osasta 1.1](https://web-palvelinohjelmointi-21.mooc.fi/osa-1/1-internetin-perusosat) jolla käytetään Java-ohjelmointieltä ja Spring-sovelluskehystä. Se ei sovellu muilta osin kovin hyvin tämän kurssin itseopiskelumateriaaliksi.

HTTP eli Hyper Text Transfer Protocol on yksinkertainen tekstipohjainen protokolla.

Kysely:
```
GET /index.html HTTP/1.1
Host: www.munpalvelin.net
```
Vastaus:
```
HTTP/1.1 200 OK
Date: Mon, 01 Sep 2014 03:12:45 GMT
Server: Apache/2.2.14 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 973
Connection: close
Content-Type: text/html;charset=UTF-8

.. runko joka sisältää HTML-koodin, yms...
```

### Flask - Pythonin WWW-palvelin

**Web-serveri, webbiservu, HTTP-palvelin**, rakkaalla lapsella on monta nimeä. Web-palvelin on Internetin kulmakivi. **Webbiservu** on ohjelmisto, joka vastaa verkkosivujen ja web-sovellusten pyynnöistä ja lähettää niihin vastauksia. Se toimii internetin perusrakenteena ja käyttää **HTTP-protokollaa (HyperText Transfer Protocol)** viestintään. Koko **WWW (World Wide Web)** perustuu tähän yksinkertaiseen mutta tehokkaaseen viestintämekanismiin.

Eri teknologioilla ja ohjelmointikielillä toteutettuja web-palvelimia on todella paljon. **Pythonin Flask-webbipalvelin ei ole yleisimpiä web-palvelimia, mutta se mahdollistaa helpon tavan tutustua Web-ohjelmointiin.**

**!! Huom! Flask ei asennu Pythonin mukana, se pitää asentaa erikseen.** Asennusohjeen löydät [täältä](install-flask.md).

Alla olevassa esimerkissä on Python-Flask-esimerkki, jossa vastaanotetaan HTTP POST -viestillä kuva, nimi ja kuvaus.
```python
@app.route('/wishes', methods=['POST'])
def add_wish():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    image = request.files['image']
    name = request.form.get('name')
    description = request.form.get('description')

    if not name or not description or image.filename == '':
        return jsonify({'error': 'Missing data'}), 400

    # Tallenna kuva
    img_filename = image.filename
    img_path = os.path.join('static/kuvat', img_filename)
    image.save(img_path)
```
