-- liste les noms des equipes
select NomEquipe
from EQUIPES;
-- 7 lignes selectionnees

-- lister les noms des directeurs sportifs

select DirecteurSportif
from EQUIPES;
-- 7 lignes selectionnees

-- lister les noms et prenoms des coureurs
select NomCoureur,PrenomCoureur
from COUREURS;
-- 7 lignes selectionnees

--trouver l'equipe du coureur ULLRICH
select NomEquipe
from COUREURS
where NomCoureur = 'ULLRICH';
-- TELEKOM

-- trouver les noms des coureurs de l'equipe COFIDIS
select NomCoureur
from COUREURS
where NomEquipe = 'COFIDIS';

-- ROMINGER COPPEL MATE

-- Lister tous les coureurs francais
select NomCoureur, PrenomCoureur
from COUREURS
where CodePays = 'FRA';
--NOMCOUREUR		       PRENOMCOUREUR
------------------------------ ------------------------------
--JALABERT		       Laurent
--COPPEL			       Jerome

--temps que le coureur 'JALABERT' a fait à l'etape 3
select to_char(temprealiser, "hs24")
from TEMPS natural join COUREURS
where TEMPS.NumCoureur = COUREURS.NomCoureur and;

--le nom et le prenom des coureur dont le prenom commence par un j
select NomCoureur, PrenomCoureur
from COUREURS
where prenomCoureur like 'J%'
order by NomCoureur desc, PrenomCoureur;

--










