drop table Client;
drop table Produit;
drop table Commande;
drop table DetailCommande;


create table Client(
IdCli Number(4), 
NomCli Varchar2(20), 
PrenomCli  VarChar2(20), 
Adresse Varchar2(20));
 
create table Produit(
Ref Number(4), 
NomProd Varchar2(20), 
Prix   Number(10,2));

create table  Commande(
NumCom Number(4), 
DateCom Date, 
IdCli   Number(4));

create table DetailCommande(
NumCom Number(4), 
Ref Number(4),   
Quantite Number(4));

