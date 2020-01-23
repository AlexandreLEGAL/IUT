-- @ SCRIPTS/CreateDropConcoursAnimaux.sql;



drop table Classement;
drop table Concours;
drop table Animaux;
drop table Proprietaires;

create table Proprietaires
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table Animaux
( Prop Number(4),
NomAnimal VarChar2(20),  
Type VarChar2(10),  
Race VarChar2(10),  
Categorie VarChar2(10), 
DateNais date,
constraint keyAnimal primary key (Prop,NomAnimal),
constraint FKproprietaire foreign key (Prop) references Proprietaires (Id)); 

create table Concours
(Titre Varchar2(20),
Annee  date,
Categorie Varchar2(10),
Certificat Varchar2(20),
TypeConcours Varchar2(3),
Ville Varchar2(20),
check (TypeConcours = 'INT' or TypeConcours = 'NAT'),
constraint keyConcours primary key (Titre, Annee),
constraint uniqueConcours unique (Ville, Annee, Categorie));


create table Classement (
Prop Number(4) , 
Animal VarChar2(20), 
TitreC Varchar2(20),
AnneeC  date, 
PositionClassement number(3),
constraint KEYClassement primary key (Prop, Animal, TitreC, AnneeC),
constraint FKPropClassement foreign key (Prop) references Proprietaires(Id) on delete cascade,
constraint FKAnimalClassement foreign key (Prop, Animal) references Animaux(Prop,NomAnimal) on delete cascade,
constraint FKConcoursClassement foreign key (TitreC,AnneeC) references Concours(Titre, Annee) on delete cascade);

insert into proprietaires values(111, 'Niarchos', 'Carton', 'Lille');
insert into animaux values(111, 'Bargos', 'Course', 'Cheval', 'Poid lourd', to_date('2001','YYYY'));
insert into proprietaires values(222, 'George', 'Tintin', 'Congo');
insert into animaux values(222, 'Milou', 'Compagnie', 'Chien', 'Poid leger', to_date('1929','YYYY'));
insert into concours values ('Bellebete', to_date('2017','YYYY'), 'Poid leger', 'BoT', 'INT', 'Nice');
insert into classement values (222, 'Milou', 'Bellebete', to_date('2017','YYYY'), 3);
