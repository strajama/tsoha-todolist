CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE tag (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(1000), 
	estimated_time INTEGER, 
	used_time INTEGER, 
	username VARCHAR(144), 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE tagtask (
	tag_id INTEGER NOT NULL, 
	task_id INTEGER NOT NULL, 
	PRIMARY KEY (tag_id, task_id), 
	FOREIGN KEY(tag_id) REFERENCES tag (id), 
	FOREIGN KEY(task_id) REFERENCES task (id)
)
