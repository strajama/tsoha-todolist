# Asennusohje

## Lokaaliasennus

### Tarvittavat työvälineet

Koko lista ja tarkat [ohjeet](https://materiaalit.github.io/tsoha-18/tyovalineet/) tarvittaviin työvälineisiin löytyy 
Tietokantasovellus-kurssin sivulta. 

Näistä tarvitset lokaaliasennukseen:

* Tuen Python-kielisten ohjelmien suorittamiseen.
* Tuen Python-kirjastojen lataamiseen.
* Tuen Python-"virtuaaliympäristöjen" luomiseen.

## Asennus

* Lataa [projekti](https://github.com/strajama/tsoha-todolist) oikealla olevasta vihreästä Clone or download -napista 
painamalla zip-tiedostona.
* Pura zip-tiedosto haluamaasi paikkaan.
* Avaa komentorivi, mene ohjelman kansion juureen ja luo kansioon virtuaaliympäristö komennolla
> python3 -m venv venv
* Aktivoi virtuaaliympäristö komennolla
> source venv/bin/activate
* Lataa ohjelman tarvitsemat riippuvuudet komennolla
> pip install -r requirements.txt
* Käynnistä ohjelma komennolla
> python3 run.py
* Avaa sivu osoitteessa [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* Paikallisen sqlite-tietokannan voi avata seuraavilla komennoilla
> cd application/
> sqlite3 tasks.db

## Verkkoasennus Herokuun

### Tarvittavat työvälineet

Koko lista ja tarkat [ohjeet](https://materiaalit.github.io/tsoha-18/tyovalineet/) tarvittaviin työvälineisiin löytyy 
Tietokantasovellus-kurssin sivulta.

Näistä tarvitset verkkoasennukseen:

* PostgreSQL-tietokannanhallintajärjestelmän.
* Työvälineet Herokun käyttöön.
* Heroku-käyttäjätunnuksen.

### Asennus

* Lataa [projekti](https://github.com/strajama/tsoha-todolist) oikealla olevasta vihreästä Clone or download -napista 
painamalla zip-tiedostona.
* Pura zip-tiedosto haluamaasi paikkaan.
* Avaa komentorivi, mene ohjelman kansion juureen ja luo kansioon virtuaaliympäristö komennolla
> python3 -m venv venv
* Aktivoi virtuaaliympäristö komennolla
> source venv/bin/activate
* Lataa ohjelman tarvitsemat riippuvuudet komennolla
> pip install -r requirements.txt
* Luodaan projektille versionhallinta komennolla
> git init
* Luodaan projekti Herokuun seuraavilla komennoilla
> heroku create PROJEKTIN_NIMI
> git remote add heroku https://git.heroku.com/PROJEKTIN_NIMI.git
> git add .
> git commit -m "Initial commit"
> git push heroku master
* Luodaan Herokuun ympäristömuuttuja komennolla
> heroku config:set HEROKU=1
* Lisätään Herokuun tietokanta komennolla
> heroku addons:add heroku-postgresql:hobby-dev
* Avaa sivu osoitteessa [https://PROJEKTIN_NIMI.herokuapp.com/](https://PROJEKTIN_NIMI.herokuapp.com/)
* Herokun tietokannan voi avata komennolla
> heroku pg:psql
