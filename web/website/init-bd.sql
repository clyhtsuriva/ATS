--Example used in a previous project

/*
drop table if exists util cascade;
drop table if exists contact cascade;

create table util(
	id_util serial primary key,
	login varchar(20) not null,
	mdp varchar(20)
);

create table contact(
	id_contact serial primary key,
	nom varchar(100),
	email varchar(100),
	tel varchar(10),
	adresse varchar(100),
	latitude real,
	longitude real,
	id_util smallint not null references util
);

insert into util(login,mdp) values ('root','root');
insert into util(login,mdp) values ('pico','pico');
*/

--drop table if exists aaa cascade;

--create table aaa(
--	bbb ccc ddd
--);
