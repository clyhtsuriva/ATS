--Creation of the main table
drop table if exists paquet cascade;

create table paquet(
	id_paquet SERIAL PRIMARY KEY,
	heure TIME(0) NOT NULL,
	protocole VARCHAR(100) NOT NULL,
	source VARCHAR(100) NOT NULL,
	destination VARCHAR(100) NOT NULL
);


