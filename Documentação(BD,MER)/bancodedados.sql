create database bancodedados;

use bancodedados;


create table cliente(
codigoCliente int primary key auto_increment not null,
nomeCliente varchar(100) not null,
cpfCliente varchar(100) not null ,
celularCliente varchar(100) not null,
senhaCliente varchar(100) not null
)Engine = InnoDB;
insert into cliente values ('', 'Miguel', '220.251.670-08', '988930277', '1234');

select*from cliente;



drop table cliente;
delete from cliente where codigoCliente = '';
alter table cliente auto_increment = 1;



create table funcionario(
codigoFunc int primary key auto_increment not null,
nomeFunc varchar(100) not null,
cpfFunc varchar(100) not null,
celularFunc varchar(100) not null,
salarioFunc varchar(100) not null,
senhaFunc varchar(100) not null,
cargo varchar(100) not null
)Engine = InnoDB;

insert into funcionario values ('', 'Manuel', '06525115116', '988930277', '1000', '1234','Administrador');

select*from funcionario;



drop table funcionario;
delete from funcionario where codigoFunc = '';
alter table funcionario auto_increment = 1;



create table lanche(
codigoLanche int primary key auto_increment not null,
nomeLanche varchar(100) not null,
descricaoLanche varchar(100) not null,
quantidadeLanche int(5) not null,
valorLanche decimal(5,2) not null
)Engine = InnoDB;
insert into lanche values ('', 'Hamburgão', 'Lanche com Queijo', '10', '5,00');
insert into lanche values ('', 'Pizza', 'Lanche com Queijo', '10', '5,00');
insert into lanche values ('', 'Bauru', 'Lanche com Queijo', '10', '5,00');
select*from lanche;



drop table lanche;
delete from lanche where codigoLanche = '';
alter table lanche auto_increment = 1;



drop database bancodedados;



set sql_safe_updates = 1;