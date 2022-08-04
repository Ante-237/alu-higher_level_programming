-- cities table 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY NOT NULL AUTO_GENERATED,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states (state_id)
	);
