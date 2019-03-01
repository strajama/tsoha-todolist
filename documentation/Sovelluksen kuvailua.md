# Yleistä

Sovellus on tarkoitettu useammalle käyttäjälle yhteiseksi muistilistaksi, 
johon lisätyt tehtävät ja tagit ovat julkisia kaikille. 
Kuka tahansa kirjautunut käyttäjä voi lisätä tehtävään käytettyä aikaa ja yhdistää tehtävään tageja tai poistaa niitä.
Kirjautuessa sovellukseen voi valita, että haluaako worker- vai admin-roolin itselleen. 
Admin-roolin omaavat voivat poistaa tehtäviä sekä lisätä ja poistaa tageja.
Ainoastaan omia tehtäviä pääsee muokkaamaan.

## Tietokantaratkaisut

Tietokantana on lokaalisti SQlite ja verkosssa PostgreSQL, mikä on toimiva, mutta ei täysin ihanteellinen ratkaisu, 
koska ne eivät toimi täysin yksi yhteen.

Tietokantataulujen nimissä on käytetty "account" -sanaa, joka muuten koodissa on korvattu sanalla "user".

Tietokannan rakenne on muuten normalisoitu paitsi että Task-taulussa on ylimääräisenä rivinä account_id:n lisäksi username, 
joka on Taskin luoneen Userin/Accountin name-sarakkeessa oleva tieto. 
Tämä sen takia, jotta sovelluksen tehtävälistausta tehdessä ei tarvitsisi tehdä ylimääräistä hakua tehtävän omistajan nimen 
selville saamiseksi.

Tietokannassa on indeksöity erikseen 

* Account-taulun username-kenttä, jotta olisi nopea varmistaa ettei samannimistä käyttäjää ole.
* Tag-taulun name-kenttä, jotta olisi nopea varmistaa ettei samannimistä tagia ole.
