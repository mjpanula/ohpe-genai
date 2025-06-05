## Lyhyt Johdatus CSS:ään (Cascading Style Sheets)

**Mitä CSS on?**

CSS on lyhenne sanoista **Cascading Style Sheets** (kaskadoidut tyylisivut). Se on kieli, jota käytetään kuvaamaan HTML-dokumentin (tai XML-dokumentin) ulkoasua ja muotoilua. Toisin sanoen:

*   **HTML** määrittelee verkkosivun rakenteen ja sisällön (otsikot, kappaleet, kuvat, linkit).
*   **CSS** määrittelee, miltä tuo rakenne ja sisältö näyttävät (värit, fontit, asettelut, välit, animaatiot).

CSS:n avulla voit erottaa sisällön esitystavasta, mikä tekee sivuston ylläpidosta helpompaa ja joustavampaa.

**Miten CSS toimii?**

CSS toimii **sääntöjen** perusteella. Jokainen sääntö koostuu:

1.  **Valitsimesta (Selector):** Määrittää, mihin HTML-elementtiin (tai elementteihin) tyyli kohdistuu.
2.  **Ominaisuudesta (Property):** Määrittää, mitä ulkoasun piirrettä halutaan muuttaa (esim. väri, fonttikoko).
3.  **Arvosta (Value):** Määrittää ominaisuuden uuden arvon (esim. `red`, `16px`).

**Syntaksi:**

```css
valitsin {
  ominaisuus: arvo;
  toinen-ominaisuus: toinen-arvo;
}
```

**Esimerkki:**

```css
/* Tämä sääntö kohdistuu kaikkiin <p>-elementteihin (kappaleisiin) */
p {
  color: blue; /* Tekstin väriksi sininen */
  font-size: 16px; /* Fonttikooksi 16 pikseliä */
}

/* Tämä sääntö kohdistuu elementtiin, jolla on luokka "korostus" */
.korostus {
  font-weight: bold;
  background-color: yellow;
}

/* Tämä sääntö kohdistuu elementtiin, jolla on ID "pääotsikko" */
#pääotsikko {
  font-size: 32px;
  text-align: center;
}
```

**CSS:n liittäminen HTML:ään**

On kolme päätapaa liittää CSS HTML-dokumenttiin:

1.  **Ulkoinen tyylitiedosto (Suositeltavin):**
    CSS-säännöt kirjoitetaan erilliseen `.css`-päätteiseen tiedostoon (esim. `tyylit.css`). Tämä tiedosto linkitetään HTML-dokumentin `<head>`-osioon:
    ```html
    <head>
      <link rel="stylesheet" href="tyylit.css">
    </head>
    ```
    Tämä on paras tapa, koska se mahdollistaa samojen tyylien käytön useilla sivuilla ja pitää HTML-koodin siistinä.

2.  **Sisäinen tyylitagi:**
    CSS-säännöt voidaan kirjoittaa suoraan HTML-dokumentin `<head>`-osion sisälle `<style>`-tagien väliin:
    ```html
    <head>
      <style>
        p {
          color: green;
        }
      </style>
    </head>
    ```
    Hyödyllinen yksittäisille sivuille tai pieniin testauksiin.

3.  **Inline-tyylit (Vältä, jos mahdollista):**
    CSS-sääntöjä voidaan lisätä suoraan yksittäisiin HTML-elementteihin `style`-attribuutilla:
    ```html
    <p style="color: red; font-size: 12px;">Tämä kappale on punainen ja pienellä fontilla.</p>
    ```
    Tämä tekee tyylien hallinnasta vaikeaa ja sitä tulisi käyttää vain poikkeustapauksissa.

**Peruskäsitteitä**

*   **Kaskadi (Cascade):** CSS-säännöt "kaskadoituvat". Tämä tarkoittaa, että useampi sääntö voi kohdistua samaan elementtiin. Selain ratkaisee ristiriidat sääntöjen **spesifisyyden** (kuinka tarkasti sääntö kohdistuu) ja **järjestyksen** perusteella. Myöhemmin määritellyt tai spesifisemmät säännöt yleensä ylikirjoittavat aiemmat.
*   **Laatikkomalli (Box Model):** Jokainen HTML-elementti nähdään CSS:ssä laatikkomaisena. Laatikko koostuu:
    *   **Sisältö (Content):** Teksti, kuva tms.
    *   **Täyte (Padding):** Tyhjä tila sisällön ja reunuksen välissä.
    *   **Reunus (Border):** Viiva täytteen ympärillä.
    *   **Marginaali (Margin):** Tyhjä tila reunuksen ulkopuolella, erottaa elementin muista elementeistä.
*   **Yksiköt:** CSS:ssä käytetään monia eri yksiköitä arvoille, kuten `px` (pikselit), `%` (prosentit), `em` (suhteessa fonttikokoon), `rem` (suhteessa juurielementin fonttikokoon), `vw`/`vh` (suhteessa näkymän leveyteen/korkeuteen).

**Yleisimpiä Ominaisuuksia (esimerkkejä):**

*   **Tekstin muotoilu:** `color`, `font-family`, `font-size`, `font-weight`, `text-align`, `line-height`
*   **Taustat:** `background-color`, `background-image`, `background-position`
*   **Laatikkomalli:** `width`, `height`, `padding`, `margin`, `border`
*   **Asettelu:** `display` (esim. `block`, `inline`, `flex`, `grid`), `position`, `float` (vanhempi), `z-index`

**Responsiivinen Suunnittelu**

CSS on avainasemassa responsiivisten verkkosivujen luomisessa, eli sivujen, jotka mukautuvat eri näyttökokoihin (tietokoneet, tabletit, puhelimet). Tämä saavutetaan usein **mediakyselyillä (`@media queries`)**:

```css
/* Perustyylit */
body {
  font-size: 16px;
}

/* Tyylit, jotka aktivoituvat, kun näytön leveys on enintään 600px */
@media (max-width: 600px) {
  body {
    font-size: 14px;
  }
  .sivupalkki {
    display: none; /* Piilota sivupalkki pienillä näytöillä */
  }
}
```

**Mistä jatkaa?**

Paras tapa oppia CSS:ää on kokeilemalla itse. Aloita yksinkertaisista HTML-sivuista ja kokeile muuttaa niiden ulkoasua CSS:llä.

---

### Hyödyllisiä Linkkejä CSS:n Opiskeluun ja Referensseihin:

1.  **MDN Web Docs (Mozilla Developer Network) - CSS:**
    *   **Opas ja tutoriaalit:** [https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) (Englanniksi, mutta erittäin kattava ja luotettava. Selaimen kääntäjällä voi auttaa.)
    *   **CSS Referenssi:** [https://developer.mozilla.org/en-US/docs/Web/CSS/Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) (Täydellinen lista kaikista CSS-ominaisuuksista ja valitsimista.)

2.  **W3Schools - CSS Tutorial:**
    *   [https://www.w3schools.com/css/default.asp](https://www.w3schools.com/css/default.asp) (Helppokäyttöinen, paljon interaktiivisia esimerkkejä, hyvä aloittelijoille.)

3.  **CSS-Tricks:**
    *   **Almanac (Ominaisuus- ja valitsinopas):** [https://css-tricks.com/almanac/](https://css-tricks.com/almanac/) (Erinomainen paikka tarkistaa tietyn ominaisuuden tai valitsimen toiminta selkeiden esimerkkien kera.)
    *   **Guides ja Artikkelit:** Sivustolla on paljon syventäviä artikkeleita ja oppaita monimutkaisempiin CSS-tekniikoihin, kuten Flexboxiin ja Gridiin.
        *   Flexbox: [https://css-tricks.com/snippets/css/a-guide-to-flexbox/](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
        *   Grid: [https://css-tricks.com/snippets/css/complete-guide-grid/](https://css-tricks.com/snippets/css/complete-guide-grid/)

4.  **freeCodeCamp - Responsive Web Design Certification:**
    *   [https://www.freecodecamp.org/learn/responsive-web-design/](https://www.freecodecamp.org/learn/responsive-web-design/) (Laaja, ilmainen kurssikokonaisuus, joka opettaa HTML:n ja CSS:n perusteet ja etenee responsiiviseen suunnitteluun ja käytännön projekteihin.)

5.  **Smashing Magazine:**
    *   [https://www.smashingmagazine.com/category/css](https://www.smashingmagazine.com/category/css) (Artikkeleita ja tutoriaaleja uusimmista CSS-tekniikoista ja parhaista käytännöistä.)

Toivottavasti tästä on apua CSS-matkallasi! Muista, että kärsivällisyys ja harjoittelu ovat avainasemassa.