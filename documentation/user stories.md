# User stories

## Ei-kirjautunut käyttäjä

* Käyttäjänä näen keillä kirjautuneilla käyttäjillä on ei-aloitettuja tehtäviä.
  * SELECT Account.id, Account.name FROM Account LEFT JOIN Task ON Task.account_id = Account.id WHERE (Task.used_time = 0) GROUP BY Account.id

* Käyttäjänä näen minkä verran mitäkin tagia on käytetty tehtävissä ja paljon tagin tehtäville on tehty työtä.
  * SELECT Tag.name, COUNT(*), SUM (Task.used_time) FROM Tag INNER JOIN Tagtask ON Tagtask.tag_id = Tag.id INNER JOIN Task ON Task.id = Tagtask.task_id GROUP BY Tag.name;

* Käyttäjänä näen minkä verran mikäkin käyttäjätyyppi on luonut tehtäviä.
  * SELECT Account.role, COUNT(*) FROM Account INNER JOIN Task ON Task.account_id = Account.id GROUP BY Account.role ORDER BY Account.role DESC;

* Käyttäjänä voin katsella tehtäviä listana.
  * SELECT task.id AS task_id, task.date_created AS task_date_created, task.date_modified AS task_date_modified, task.name AS task_name, task.description AS task_description, task.estimated_time AS task_estimated_time, task.used_time AS task_used_time, task.username AS task_username, task.account_id AS task_account_id 

* Käyttäjänä voin katsella tageja listana.
  * SELECT tag.id AS tag_id, tag.date_created AS tag_date_created, tag.date_modified AS tag_date_modified, tag.name AS tag_name 

* Käyttäjänä voin luoda käyttäjätunnuksena.
  * INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

* Käyttäjänä voin kirjautua sovellukseen.
  * SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role
  
## Kirjautunut käyttäjä

* Käyttäjänä voin kirjautuneena lisätä uuden tehtävän.
 * INSERT INTO task (date_created, date_modified, name, description, estimated_time, used_time, username, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, 0, current_user.id, current_user.name)

* Käyttäjänä voin kirjautuneena muokata itse luomaani tehtävää.
 * UPDATE task SET date_modified=CURRENT_TIMESTAMP, name=?, description=?, estimated_time=?, used_time=? WHERE task.id = ?

* Käyttäjänä voin lisätä napista eri tehtäville tehtyjä tunteja
 * UPDATE task SET date_modified=CURRENT_TIMESTAMP, used_time=? WHERE task.id = ?


* Käyttäjänä voin kirjautuneena lisätä tehtävälle tageja.
* Käyttäjänä näen tehtäviin kiinnitetyt tagit.
* Admin-käyttäjänä voin kirjautuneena lisätä uuden tagin.
* Admin-käyttäjänä voin kirjautuneena muokata tagia.
* Admin-käyttäjänä voin kirjautuneena poistaa tagin.

* Käyttäjänä voin kirjautuneena poistaa tehtävän.
