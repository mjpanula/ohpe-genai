# Generatiivisen tekoälyn ja ohjelmistorobotiikan ohjelmointiteknologioiden perusteet

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

[Wikipedia](https://fi.wikipedia.org/wiki/JSON) kertoo että JSON on avoin tiedostomuoto joka on osa JavaScript -standardia. [Englanninkielinen Wikipedia](https://en.wikipedia.org/wiki/JSON) taustoittaa asiaa vielä paremmin.

Meille riittää toistaisekssi tietää että JSON on yleisin internetin tiedosiirtoformaatti, ja että sen hyödyntäminen Pythonissa on melko suoraviivaista.

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

Alla luodaan Python-anakirja, joka muunnetaan JSON-muotoon.

```python
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

**Muista puhua json-importista**
