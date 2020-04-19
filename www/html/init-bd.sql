--Creation of the main table
drop table if exists paquet cascade;

create table paquet(
	id_paquet SERIAL PRIMARY KEY,
	heure TIME(0) NOT NULL,
	protocole VARCHAR NOT NULL,
	ip_source VARCHAR NOT NULL,
	ip_destination VARCHAR NOT NULL,
	port_source INT NOT NULL,
	port_destination INT NOT NULL
);


