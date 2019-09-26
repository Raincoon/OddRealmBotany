CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE plant (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	mature_time INTEGER NOT NULL, 
	is_tree BOOLEAN NOT NULL, 
	owner_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (is_tree IN (0, 1)), 
	FOREIGN KEY(owner_id) REFERENCES account (id)
)

CREATE TABLE tag (
	id INTEGER NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	owner_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES account (id)
)

CREATE TABLE plant_tag_helper (
	plant_id INTEGER NOT NULL, 
	tag_id INTEGER NOT NULL, 
	PRIMARY KEY (plant_id, tag_id), 
	FOREIGN KEY(plant_id) REFERENCES plant (id), 
	FOREIGN KEY(tag_id) REFERENCES tag (id)
)