CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(20) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(20) NOT NULL, 
	role VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
)

CREATE UNIQUE INDEX indexusername ON account (username);

CREATE TABLE tag (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

CREATE UNIQUE INDEX indexname ON account (name);

CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(30) NOT NULL, 
	description VARCHAR(60), 
	estimated_time INTEGER, 
	used_time INTEGER, 
	username VARCHAR(20), 
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
