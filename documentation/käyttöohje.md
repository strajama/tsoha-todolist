# Käyttöohje

Sovellus on muistilista, joka on tarkoitettu yhden tai useamman henkilön käyttöön. 

Etusivun tulosteessa ensimmäisenä näkee keillä käyttäjistä on tehtäviä (tasks), joihin ei ole käytetty aikaa, jos sellaisia käyttäjiä on.
Toiseksi näkee, että mitä tageja on liitetty tehtäviin, kuinka moneen tehtävään mikäkin tagi on liitetty ja kuinka paljon kyseisiin tehtäviin on käytetty aikaa.
Kolmannessa tulosteessa näkee, että kuinka paljon tehtäviä eri käyttäjäroolin omaavat käyttäjät ovat luoneet.

Sovelluksessa liikutaan ylärivin linkkien kautta.

## List tasks

Linkistä avautuu lista kaikista sovelluksissa olevista tehtävistä ja ne näkyvät kaikille käyttäjille.

Tehtävät näkyvät taulukossa, jossa on tehtävän nimi (Task), kuvailu (Description), arvioitu aika (Estimated time), käytetty aika (Used time) ja omistaja (Owner).

Kirjautuneet käyttäjät voivat katsoa ja editoida tehtävän tageja Tags-linkistä, editoida tehtävää Edit task -linkistä ja poistaa tehtävän Delete-napista.

### Tags-linkki

Linkistä avautuu näkymä, jossa ensimmäisenä näkyy tehtävään yhdistetyt tagit.

Alaosassa on listattuna kaikki mahdolliset tagit ja näiden vieressä valintaruudut. Valintaruudun valitseminen ja Add or remove tags to the task -napin painaminen joko lisää tai poistaa tagin. Jos tagia ei ole vielä yhdistetty kyseiseen tehtävään, niin tagi lisätään sille ja jos tagi on yhdistetty tehtävään, niin se poistuu tehtävän yhteydestä.

### Edit task -linkki

Linkistä avautuu taulukko, jossa näkyy tehtävän nykyiset tiedot (Current data) ja kentät, joihin kirjoittamalla voi muokata niitä.

Task name -rivillä on tehtävän nykyinen nimi ja kenttä, johon kirjoittamalla sitä voi muuttaa.

Description-rivillä on tehtävän nykyinen kuvailu ja kenttä, johon kirjoittamalla sitä voi muuttaa.

Estimated time -rivillä on tehtävän nykyinen arvioitu aikavaatimus ja kenttä, johon kirjoittamalla sitä voi muuttaa.

Time used -rivillä on tehtävään käytetty aika ja kenttä, johon kirjoittamalla sitä voi muuttaa.

Save changes -nappia painamalla uudet tiedot korvaavat nykyiset tiedot.

## Add a task

Linkin kautta pääsee lisäämään uuden tehtävän. Toiminto on vain kirjautuneiden käyttäjien käytettävissä.

Task name -kenttään kirjoitetaan tehtävän nimi, jonka tulee olla 2-144 merkkiä pitkä.

Description-kenttään kirjoitetaan tehtävän kuvailu. Tämän kentän voi jättää tyhjäksi.

Estimated time -kenttään kirjoitetaan arvio siitä paljonko tehtävään käytetään aikaa lukuna 1-999 välillä.

Add a new task -nappi luo uuden tehtävän. 

Tehtävän luonnin jälkeen aukeaa lista kaikista tehtävistä.

## List tags

Linkistä avautuu lista kaikista sovelluksissa olevista tageista ja ne näkyvät kaikille käyttäjille.

Listalla näkyy kaikki tagit, Edit tag -linkki ja Delete-nappi. Vain admin-roolin omaavat käyttäjät voivat poistaa tagin tai muokata sitä.

### Edit tag -linkki

Vain admin-roolin omaavat käyttäjät voivat käyttää tätä linkkiä.

Edit tag -linkistä pääsee muokkaamaan tagin nimen toiseksi ja Save changes -nappia painamalla muutos tallentuu.

## Add a tag

Linkin kautta pääsee lisäämään uuden tehtävän. Toiminto on vain kirjautuneiden, admin-roolin omaavien käyttäjien käytettävissä.

Uuden tagin luomiseksi sille pitää kirjoittaa nimi, joka on 2-144 merkkiä pitkä sekä painaa Add a new tag -nappia.

## User information

Linkin kautta näkee kirjautuneen käyttäjän käyttäjätilin tiedot (nimi, käyttäjätunnus ja salasana, rooli) ja tehtävät sekä pääsee muokkaamaan käyttäjätilin tiedoista nimeä, käyttäjätunnusta ja salasanaa.

## Login

Linkin kautta voi kirjautua sovellukseen.

Username-kenttään kirjoitetaan käyttäjätunnus ja password-kenttään salasana.

Login-napilla kirjaudutaan sovellukseen.

## Sign up

Linkin kautta voi luoda uudet käyttäjätunnukset.

### Uusien käyttäjätunnusten luominen

Name-kenttään kirjoitetaan nimi, jota sovelluksessa haluaa käyttää.

Username-kenttään kirjoitetaan käyttäjätunnus, jota käytetään kirjautuessa. Se on pakollinen ja pituudeltaan oltava vähintään kaksi merkkiä.

Password-kenttään kirjoitetaan salasana.

Role-valikosta valitaan käyttäjärooli.

Sign in new user -nappi luo uudet käyttäjätunnukset.


