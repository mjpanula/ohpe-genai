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