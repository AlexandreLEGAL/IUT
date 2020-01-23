-- @ SCRIPTS/CreateDrop-ToursFR;
-- @ SCRIPTS/instanceToursFR;




drop table TEMPS;
drop table ETAPES;
drop table COUREURS;
drop table EQUIPES;
drop table PAYS;

create table PAYS (
CodePays Varchar2(3) primary key,
NPays Varchar2(20));

create table EQUIPES
(NomEquipe VarChar2(30)  primary key, 
DirecteurSportif  VarChar2(20));

create table COUREURS
(NumCoureur Number (4) primary key,
NomCoureur VarChar2(30),
PrenomCoureur VarChar2(30),
NomEquipe VarChar2(20),
CodePays VarChar(3),
foreign key (CodePays) references PAYS(CodePays) on delete cascade,
foreign key (NomEquipe) references EQUIPES(NomEquipe) on delete cascade);

create table ETAPES(
NumEtape Number (3) primary key,
DateEtape DATE DEFAULT sysdate,
VilleDepart Varchar2(20),
VilleArrivee Varchar2(20),
NbKm Number (3));

create table TEMPS(
NumCoureur Number (3),
NumEtape Number (3),
TempsRealise Date,
constraint Temps_ok primary key (NumCoureur, NumEtape),
constraint CoureurExiste foreign key (NumCoureur) references COUREURS(NumCoureur),
constraint CoureurExisteEtape foreign key (NumCoureur) references ETAPES(NumCoureur));


