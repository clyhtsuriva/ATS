--Creation of the main table
drop table if exists trame cascade;

create table trame(
	id_trame serial primary key,
	heure varchar(100),
	protocole varchar(100),
	source varchar(100),
	destination varchar(100)
);


