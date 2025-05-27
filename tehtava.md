# Kurssin harjoitustyö

**Harjoitustyö** on nelivaiheinen. Täydet pisteet saa toteuttamalla kaikki 4 osioita.


1. Tee Flask-sovellus joka lukee tiedostosta lahjatoiveiden nimet, ja tulostaa ne HTML-taulukossa
2. Flask sovellus lukee CSV-tiedostosta lahjatoiveiden nimen, kuvauksen sekä kuvapolun ja tulostaa ne HTML-taulukossa
3. Flask sovellus lukee CSV-tiedostosta edelliset, muuntaa lahjatoivetiedot JSON-muotoon ja tarjoilee niitä niitä JSON-formaatissa HTTP-rajapinnan yli
4. Edellisen lisäksi, uusia lahjatoiveita pystyy tallentamaan tiedostoon. Myös kuvan lataaminen pitää olla mahdollista.

Tehtävä palautetaan ZIP-pakattuna moodleen. Jokainen vaihe tulee löytyä omana hakemistonaan.

```
harjoitustyö.zip

harjoitustyö/
├── vaihe1/
│   ├── toiveet.txt
│   ├── index.html
│   └── app.py
├── vaihe2/
│   ├── toiveet.csv
│   ├── index.html
│   └── app.py
├── vaihe3/
│   ├── toiveet.csv
│   ├── index.html
│   └── app.py
└── vaihe4/
    ├── toiveet.csv
    ├── app.py
    ├── add_wish.html
    └── index.html
```