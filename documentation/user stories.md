# User stories

## Ei-kirjautunut käyttäjä

* Käyttäjänä näen korkeintaan sata kirjautunutta käyttäjää, joilla on ei-aloitettuja tehtäviä.
  * SELECT Account.id, Account.name FROM Account LEFT JOIN Task ON Task.account_id = Account.id WHERE (Task.used_time = 0) GROUP BY Account.id LIMIT (100);

* Käyttäjänä näen aakkosissa 10 ensimmäistä tagia, minkä verran mitäkin tagia on käytetty tehtävissä ja paljon tagin tehtäville on tehty työtä.
  * SELECT Tag.name, COUNT(*), SUM (Task.used_time) FROM Tag INNER JOIN Tagtask ON Tagtask.tag_id = Tag.id INNER JOIN Task ON Task.id = Tagtask.task_id GROUP BY Tag.name LIMIT (10);

* Käyttäjänä näen minkä verran mikäkin käyttäjätyyppi on luonut tehtäviä.
  * SELECT Account.role, COUNT(*) FROM Account INNER JOIN Task ON Task.account_id = Account.id GROUP BY Account.role ORDER BY Account.role DESC;

* Käyttäjänä voin katsella tehtäviä listana, joista näytetään sata ensimmäistä listana. Listaa voi filtteröidä nimen perusteella.
  * SELECT task.id AS task_id, task.date_created AS task_date_created, task.date_modified AS task_date_modified, task.name AS task_name, task.description AS task_description, task.estimated_time AS task_estimated_time, task.used_time AS task_used_time, task.username AS task_username, task.account_id AS task_account_id 
FROM task ORDER BY task.name
 LIMIT 100 OFFSET 0
 
* Käyttäjänä näen tehtäviin kiinnitetyt tagit ja aakkosissa 100 ensimmäistä tagia, jotka tehtävään voi lisätä. Listaa voi filtteröidä nimen perusteella.
  * SELECT tag.id AS tag_id, tag.date_created AS tag_date_created, tag.date_modified AS tag_date_modified, tag.name AS tag_name 
FROM tag, tagtask 
WHERE ? = tagtask.task_id AND tag.id = tagtask.tag_id
  * SELECT tag.id AS tag_id, tag.date_created AS tag_date_created, tag.date_modified AS tag_date_modified, tag.name AS tag_name 
FROM tag ORDER BY tag.name
 LIMIT 100 OFFSET 0

* Käyttäjänä voin katsella tageja listana, joista näytetään sata ensimmäistä listana. Listaa voi filtteröidä nimen perusteella.
  * SELECT tag.id AS tag_id, tag.date_created AS tag_date_created, tag.date_modified AS tag_date_modified, tag.name AS tag_name 
FROM tag ORDER BY tag.name
 LIMIT ? OFFSET ?

* Käyttäjänä voin luoda käyttäjätunnuksena.
  * INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

* Käyttäjänä voin kirjautua sovellukseen.
  * SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.password = ? AND account.username = ?

## Kirjautunut käyttäjä

* Käyttäjänä voin kirjautuneena lisätä uuden tehtävän.
  * INSERT INTO task (date_created, date_modified, name, description, estimated_time, used_time, username, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, current_user.name, current_user.id)

* Käyttäjänä voin kirjautuneena muokata itse luomaani tehtävää.
  * UPDATE task SET date_modified=CURRENT_TIMESTAMP, name=?, description=?, estimated_time=?, used_time=? WHERE task.id = ?

* Käyttäjänä voin lisätä napista eri tehtäville tehtyjä tunteja
  * UPDATE task SET date_modified=CURRENT_TIMESTAMP, used_time=? WHERE task.id = ?

* Käyttäjänä voin kirjautuneena lisätä tehtävälle tageja.
  * INSERT INTO tagtask (tag_id, task_id) VALUES (?, ?)
 
* Käyttäjänä voin kirjautuneena poistaa tehtävältä tageja.
  * DELETE FROM tagtask WHERE tagtask.tag_id = ? AND tagtask.task_id = ?
  
* Käyttäjänä voin kirjautuneena katsoa oman käyttäjätilini tietoja ja nähdä sata kappaletta minkä nimisiä tehtäviä olen luonut
  * SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?
  * SELECT Task.name FROM Task WHERE (Task.Account_id = ?) LIMIT (100);

* Käyttäjänä voin kirjautuneena muokata oman käyttäjätilini tietoja roolia lukuunottamatta, mutta en sellaiseksi käyttäjänimeksi, joka toisella on jo käytössä.
  * UPDATE account SET date_modified=CURRENT_TIMESTAMP, name=?, username=?, password=? WHERE account.id = ?
  * SELECT COUNT(*) FROM Account WHERE (Account.username = ?) GROUP BY Account.username
  
# Admin-roolinen kirjautunut käyttäjä

* Admin-käyttäjänä voin kirjautuneena lisätä uuden tagin.
  * INSERT INTO tag (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)
  
* Admin-käyttäjänä voin kirjautuneena muokata tageja.
  * UPDATE tag SET date_modified=CURRENT_TIMESTAMP, name=? WHERE tag.id = ?

* Admin-käyttäjänä voin kirjautuneena poistaa tagin.
  * DELETE FROM tag WHERE tag.id = ?
  * DELETE FROM tagtask WHERE tagtask.tag_id = ? AND tagtask.task_id = ? (jos tagi on yhdistetty tehtävään)

* Käyttäjänä voin kirjautuneena poistaa tehtävän.
  * DELETE FROM task WHERE task.id = ?
  * DELETE FROM tagtask WHERE tagtask.tag_id = ? AND tagtask.task_id = ? (jos tehtävään on yhdistetty tagi)
