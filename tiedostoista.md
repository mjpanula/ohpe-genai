Tässä on Python-skripti, joka demonstroi kansioiden ja tiedostojen luontia sekä poistoa.

```python
# Tuodaan tarvittavat moduulit:
# 'os' tarjoaa toimintoja käyttöjärjestelmän kanssa vuorovaikuttamiseen,
# kuten polkujen käsittelyyn ja kansioiden luontiin/poistoon.
# 'shutil' (shell utilities) tarjoaa korkeamman tason tiedosto-operaatioita,
# kuten kansioiden rekursiivisen poiston.
# 'pathlib' tarjoaa modernin, oliopohjaisen tavan käsitellä tiedostojärjestelmän polkuja.
# Se on usein suositeltavampi kuin vanhempi os.path.
import os
import shutil
from pathlib import Path

# Määritellään pääkansio, jonka sisällä kaikki operaatiot tehdään.
# Tämä helpottaa demon siivoamista ja estää vahingossa muiden tiedostojen muokkaamisen.
BASE_DIR_NAME = "demo_kansio_projekti"

# Luodaan Path-olio pääkansiolle. Path-oliot tekevät polkujen käsittelystä helpompaa.
# Esimerkiksi polkujen yhdistäminen onnistuu '/' operaattorilla: base_dir / "alikansio"
base_dir = Path(BASE_DIR_NAME)

def luo_ja_tayta_tiedosto(tiedoston_polku: Path, sisalto: str):
    """
    Luo tiedoston annettuun polkuun ja kirjoittaa siihen sisällön.
    Jos tiedosto on jo olemassa, se ylikirjoitetaan.

    Args:
        tiedoston_polku (Path): Polku tiedostoon, joka luodaan.
        sisalto (str): Tekstisisältö, joka kirjoitetaan tiedostoon.
    """
    try:
        # Avataan tiedosto kirjoitustilaan ('w').
        # 'encoding="utf-8"' on hyvä käytäntö merkkien oikeanlaisen tallennuksen varmistamiseksi.
        # 'with open(...)' varmistaa, että tiedosto suljetaan automaattisesti,
        # vaikka virheitä tapahtuisi.
        with tiedoston_polku.open(mode="w", encoding="utf-8") as tiedosto:
            tiedosto.write(sisalto)
        print(f"Tiedosto '{tiedoston_polku.name}' luotu ja täytetty onnistuneesti kansioon '{tiedoston_polku.parent}'.")
    except IOError as e:
        # IOError (tai sen aliluokat kuten FileNotFoundError, PermissionError)
        # voi tapahtua, jos tiedoston luonti/kirjoitus epäonnistuu.
        print(f"Virhe luotaessa/kirjoitettaessa tiedostoa '{tiedoston_polku}': {e}")

def main():
    """
    Pääfunktio, joka suorittaa kaikki demo-operaatiot.
    """
    print(f"--- Aloitetaan kansion '{BASE_DIR_NAME}' ja sen sisällön hallintademo ---")

    # 1. ALUSTUS: POISTETAAN MAHDOLLINEN AIEMPI DEMOKANSIO
    # Varmistetaan, että aloitamme puhtaalta pöydältä joka ajokerralla.
    if base_dir.exists():
        print(f"Kansio '{base_dir}' on jo olemassa. Poistetaan se ensin...")
        try:
            # shutil.rmtree() poistaa kansion ja kaiken sen sisällön rekursiivisesti.
            # Ole varovainen tämän komennon kanssa oikeissa projekteissa!
            shutil.rmtree(base_dir)
            print(f"Kansio '{base_dir}' ja sen sisältö poistettu.")
        except OSError as e:
            # OSError voi tapahtua, jos poistaminen epäonnistuu (esim. oikeusongelmat).
            print(f"Virhe poistettaessa olemassa olevaa kansiota '{base_dir}': {e}")
            print("Skriptin suoritus keskeytetään, koska alustavaa siivousta ei voitu tehdä.")
            return # Lopetetaan skripti, jos siivous epäonnistuu.

    # 2. KANSIOIDEN LUONTI
    print("\n--- Vaihe 1: Kansioiden luonti ---")
    try:
        # Path.mkdir() luo kansion.
        # parents=True: Luo tarvittavat yläkansiot, jos niitä ei ole olemassa.
        #               Tässä tapauksessa ei tarvita, koska luomme vain yhden tason kansion.
        # exist_ok=True: Ei aiheuta virhettä, jos kansio on jo olemassa.
        #                Tässä tapauksessa olemme juuri poistaneet sen, joten se ei ole olemassa.
        base_dir.mkdir(parents=True, exist_ok=True)
        print(f"Pääkansio '{base_dir.resolve()}' luotu.") # .resolve() antaa absoluuttisen polun.

        # Luodaan alikansioita pääkansioon
        alikansio1_polku = base_dir / "asiakirjat" # Käytetään '/' polkujen yhdistämiseen
        alikansio2_polku = base_dir / "kuvat"
        alikansio_tyhja_polku = base_dir / "temp_tyhja" # Tätä käytetään tyhjän kansion poistoon

        alikansio1_polku.mkdir(exist_ok=True) # Ei tarvitse parents=True, koska base_dir on jo olemassa
        print(f"Alikansio '{alikansio1_polku.name}' luotu kansioon '{base_dir}'.")

        alikansio2_polku.mkdir(exist_ok=True)
        print(f"Alikansio '{alikansio2_polku.name}' luotu kansioon '{base_dir}'.")

        alikansio_tyhja_polku.mkdir(exist_ok=True)
        print(f"Alikansio '{alikansio_tyhja_polku.name}' luotu kansioon '{base_dir}'.")

    except OSError as e:
        print(f"Virhe kansiota luotaessa: {e}")
        return # Jos peruskansioiden luonti epäonnistuu, ei kannata jatkaa.

    # 3. TIEDOSTOJEN LUONTI KANSIOIHIN
    print("\n--- Vaihe 2: Tiedostojen luonti kansioihin ---")
    tiedosto1_polku = alikansio1_polku / "raportti.txt"
    luo_ja_tayta_tiedosto(tiedosto1_polku, "Tämä on tärkeä raportti.\nSisältää paljon dataa.")

    tiedosto2_polku = alikansio1_polku / "muistio.md"
    luo_ja_tayta_tiedosto(tiedosto2_polku, "# Muistiinpanot\n\n- Tee tämä\n- Muista tuo")

    tiedosto3_polku = alikansio2_polku / "maisemakuva.jpg" # Vaikka .jpg, sisältö on tekstiä demossa
    luo_ja_tayta_tiedosto(tiedosto3_polku, "Tämä on kuvatiedoston placeholder-teksti.")

    tiedosto4_polku = alikansio2_polku / "logo.png"
    luo_ja_tayta_tiedosto(tiedosto4_polku, "Tämä on logo.png:n placeholder-teksti.")

    tiedosto_juuressa_polku = base_dir / "README.txt"
    luo_ja_tayta_tiedosto(tiedosto_juuressa_polku, f"Tämä on {BASE_DIR_NAME} projektin README.")

    # 4. KANSIOIDEN SISÄLLÖN LISTAUS (esimerkki)
    print("\n--- Vaihe 3: Kansioiden sisällön listaus ---")
    print(f"Sisältö kansiossa '{base_dir}':")
    # Path.iterdir() palauttaa iteraattorin kansion sisällöstä (tiedostot ja alikansiot)
    for kohde in base_dir.iterdir():
        tyyppi = "Kansio" if kohde.is_dir() else "Tiedosto"
        print(f"  - {kohde.name} ({tyyppi})")

    print(f"\nSisältö kansiossa '{alikansio1_polku}':")
    if alikansio1_polku.exists() and alikansio1_polku.is_dir():
        for kohde in alikansio1_polku.iterdir():
            print(f"  - {kohde.name}")


    # 5. YKSITTÄISEN TIEDOSTON POISTO
    print("\n--- Vaihe 4: Yksittäisen tiedoston poisto ---")
    if tiedosto2_polku.exists():
        try:
            # Path.unlink() poistaa tiedoston.
            # Jos polku osoittaa kansioon tai tiedostoa ei ole, se aiheuttaa virheen.
            tiedosto2_polku.unlink()
            print(f"Tiedosto '{tiedosto2_polku.name}' poistettu kansiosta '{tiedosto2_polku.parent}'.")
        except OSError as e:
            print(f"Virhe poistettaessa tiedostoa '{tiedosto2_polku}': {e}")
    else:
        print(f"Tiedostoa '{tiedosto2_polku.name}' ei löytynyt poistettavaksi.")

    # Tarkistetaan alikansio1:n sisältö poiston jälkeen
    print(f"\nSisältö kansiossa '{alikansio1_polku}' tiedoston poiston jälkeen:")
    if alikansio1_polku.exists() and alikansio1_polku.is_dir():
        for kohde in alikansio1_polku.iterdir():
            print(f"  - {kohde.name}")
    else:
        print(f"Kansiota '{alikansio1_polku}' ei enää löydy (tämä olisi yllättävää).")


    # 6. TYHJÄN KANSION POISTO
    print("\n--- Vaihe 5: Tyhjän kansion poisto ---")
    # alikansio_tyhja_polku luotiin tyhjänä.
    if alikansio_tyhja_polku.exists():
        try:
            # Path.rmdir() poistaa kansion. Se toimii VAIN, jos kansio on tyhjä.
            alikansio_tyhja_polku.rmdir()
            print(f"Tyhjä kansio '{alikansio_tyhja_polku.name}' poistettu.")
        except OSError as e:
            # OSError (esim. DirectoryNotEmptyError) jos kansio ei ole tyhjä tai muu virhe.
            print(f"Virhe poistettaessa tyhjää kansiota '{alikansio_tyhja_polku}': {e}")
    else:
        print(f"Kansiota '{alikansio_tyhja_polku.name}' ei löytynyt poistettavaksi (ehkä jo poistettu).")


    # 7. EI-TYHJÄN KANSION POISTOYRITYS (rmdir)
    print("\n--- Vaihe 6: Ei-tyhjän kansion poistoyritys (rmdir) ---")
    # alikansio2_polku sisältää vielä tiedostoja.
    if alikansio2_polku.exists():
        print(f"Yritetään poistaa kansio '{alikansio2_polku.name}', joka sisältää tiedostoja, käyttäen rmdir()...")
        try:
            alikansio2_polku.rmdir()
            # Tähän ei pitäisi päästä, koska kansio ei ole tyhjä.
            print(f"Kansio '{alikansio2_polku.name}' poistettu (yllättävää, sen ei pitänyt olla tyhjä).")
        except OSError as e:
            print(f"Odotettu virhe: Kansion '{alikansio2_polku.name}' poisto rmdir()-komennolla epäonnistui, koska se ei ole tyhjä: {e}")
    else:
        print(f"Kansiota '{alikansio2_polku.name}' ei löytynyt.")

    # 8. EI-TYHJÄN KANSION POISTO (shutil.rmtree)
    print("\n--- Vaihe 7: Ei-tyhjän kansion poisto (shutil.rmtree) ---")
    # Poistetaan alikansio1, joka sisältää vielä "raportti.txt".
    if alikansio1_polku.exists():
        print(f"Poistetaan kansio '{alikansio1_polku.name}' ja sen sisältö käyttäen shutil.rmtree()...")
        try:
            # shutil.rmtree() poistaa kansion ja KAIKEN sen sisällön rekursiivisesti.
            # Käytä tätä varoen!
            shutil.rmtree(alikansio1_polku)
            print(f"Kansio '{alikansio1_polku.name}' ja sen sisältö poistettu onnistuneesti.")
        except OSError as e:
            print(f"Virhe poistettaessa kansiota '{alikansio1_polku}' shutil.rmtree()-komennolla: {e}")
    else:
        print(f"Kansiota '{alikansio1_polku.name}' ei löytynyt poistettavaksi.")


    # 9. KOKO DEMOKANSION POISTAMINEN LOPUKSI (SIIVOUS)
    print("\n--- Vaihe 8: Koko demorakenteen siivous ---")
    if base_dir.exists():
        print(f"Poistetaan pääkansio '{base_dir.name}' ja kaikki sen jäljellä oleva sisältö...")
        try:
            shutil.rmtree(base_dir)
            print(f"Pääkansio '{base_dir.name}' ja sen kaikki sisältö poistettu.")
        except OSError as e:
            print(f"Virhe poistettaessa pääkansiota '{base_dir}': {e}")
            print("Saatat joutua poistamaan kansion manuaalisesti.")
    else:
        print(f"Pääkansiota '{base_dir.name}' ei löytynyt siivottavaksi (ehkä jo poistettu aiemmin).")

    print(f"\n--- Kansion '{BASE_DIR_NAME}' hallintademo päättyi ---")


# Tämä varmistaa, että main()-funktio ajetaan vain, kun skripti suoritetaan suoraan
# (eikä silloin, kun se tuodaan moduulina toiseen skriptiin).
if __name__ == "__main__":
    main()

```

**Skriptin toiminta lyhyesti:**

1.  **Alustus:** Jos `demo_kansio_projekti` on olemassa edelliseltä ajokerralta, se poistetaan sisältöineen (`shutil.rmtree`).
2.  **Kansioiden luonti:**
    *   Luo pääkansion `demo_kansio_projekti` (`base_dir.mkdir`).
    *   Luo alikansiot `asiakirjat`, `kuvat` ja `temp_tyhja` pääkansion sisälle.
3.  **Tiedostojen luonti:**
    *   Luo useita tekstitiedostoja (`.txt`, `.md`, `.jpg`, `.png` -nimillä, mutta kaikki sisältävät tekstiä demotarkoituksessa) eri kansioihin käyttäen apufunktiota `luo_ja_tayta_tiedosto`.
4.  **Sisällön listaus:**
    *   Tulostaa pääkansion ja yhden alikansion sisällön (`Path.iterdir()`).
5.  **Yksittäisen tiedoston poisto:**
    *   Poistaa `muistio.md` -tiedoston `asiakirjat`-kansiosta (`tiedosto_polku.unlink()`).
6.  **Tyhjän kansion poisto:**
    *   Poistaa `temp_tyhja`-kansion (`kansio_polku.rmdir()`). Tämä onnistuu, koska kansio on tyhjä.
7.  **Ei-tyhjän kansion poistoyritys (`rmdir`):**
    *   Yrittää poistaa `kuvat`-kansion `rmdir()`-komennolla. Tämä epäonnistuu ja tulostaa virheilmoituksen, koska kansio sisältää vielä tiedostoja.
8.  **Ei-tyhjän kansion poisto (`shutil.rmtree`):**
    *   Poistaa `asiakirjat`-kansion ja sen jäljellä olevan sisällön (`raportti.txt`) käyttäen `shutil.rmtree()`. Tämä onnistuu, koska `shutil.rmtree` poistaa kansion sisällöstä riippumatta.
9.  **Loppusiivous:**
    *   Poistaa koko `demo_kansio_projekti`-kansion ja kaiken sen mahdollisen jäljellä olevan sisällön (`shutil.rmtree`) varmistaakseen, ettei levylle jää turhia tiedostoja demon jälkeen.

**Miten ajat skriptin:**

1.  Tallenna koodi tiedostoon, esimerkiksi `kansio_demo.py`.
2.  Avaa komentokehote tai terminaali.
3.  Siirry hakemistoon, johon tallensit tiedoston.
4.  Suorita skripti komennolla: `python kansio_demo.py`

Näet tulosteet komentokehotteessa, ja voit myös tarkistaa tiedostojärjestelmästä, että kansio `demo_kansio_projekti` luodaan ja poistetaan skriptin ajon aikana.