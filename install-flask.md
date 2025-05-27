# Flask - asennus

[YouTube: How to Install Flask in Python (2023 Easy Guide) - The Code City](https://www.youtube.com/watch?v=6EJklo3Kpr4)

Yllä oleva video näyttää, kuinka Flask asennetaan pipin avulla. Videoon on mahdollista laittaa päälle automaattisesti generoidut suomenkieliset tekstitykset.

## Mikä on Flask?

**Flask on kevyt ja joustava web-sovelluskehys, joka on kirjoitettu Pythonilla**. Se mahdollistaa web-sovellusten ja API-rajapintojen nopean kehittämisen. Flask on suunniteltu minimalistiseksi, mutta sitä voidaan laajentaa lisäosilla ja kirjastoilla tarpeen mukaan.

On tärkeää huomata, että Flask ei kuulu Pythonin standardikirjastoon, joten se täytyy asentaa erikseen esimerkiksi `pip`-työkalun avulla.

## Mikä on pip ja miten sitä käytetään?

`pip` on Pythonin paketinhallintatyökalu, jonka avulla voit asentaa, päivittää ja hallita Python-paketteja. Se on erityisen hyödyllinen, kun haluat lisätä uusia kirjastoja tai työkaluja Python-projektiisi.

### Miksi käyttää pipiä?

- Helppo tapa asentaa ja hallita Python-paketteja.
- Auttaa pitämään projektisi riippuvuudet ajan tasalla.
- Tukee laajaa valikoimaa kirjastoja ja työkaluja.

### Flaskin asentaminen pipillä Windows-ympäristössä

1. Avaa komentokehote (Command Prompt) tai PowerShell.
2. Varmista, että Python ja pip on asennettu. Voit tarkistaa tämän komennolla:
    ```bash
    python --version
    pip --version
    ```
3. Asenna Flask komennolla:
    ```bash
    pip install flask
    ```
4. Varmista, että Flask on asennettu oikein:
    ```bash
    python -m flask --version
    ```