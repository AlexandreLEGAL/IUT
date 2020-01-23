exemple1 = {
    'Pokemon the Movie': (1000, 3000),
    'Avengers vs predator': (4000, 20),
    'Poil de carotte': (2000, 2000),
    "L'alphabet en 634 rot": (3, 5),
}


# Exercice 1
def moins_succes(box_office):
    n = float('inf')
    for a in box_office.values():
        if a[1] > n:
            n = a[1]
    return n


# Exercice 4
trois_amis = {'Camille': {'Velo', 'Kayak', 'Boxe'}, 'Dominique': {'Velo'},
              'Claude': {'Lecture', 'Tricot', 'Boxe', 'Velo'}}


# 4.1 - Non on ne pas peut utiliser un enssemble comme clé, car les enssembles sont mutables. En revanche
# on peut les utiliser comme valeurs

# 4.2

def activite_populaire(dic):
    popularite_activite = {}  # Dictionnaire avec comme cle les activite et en valeur le nombre de fois il y a l'activit
    for enssemble_activite in dic.values():
        for activite in enssemble_activite:
            if activite in popularite_activite:
                popularite_activite[activite] += 1
            else:
                popularite_activite[activite] = 1

    def popularite(activite):
        return popularite_activite[activite]

    # popularite_max = 0
    activite_plus_populaire = max(popularite_activite, key=popularite)
    # for (activite, popularite) in popularite_activite.items():
    #     if popularite > popularite_max:
    #         popularite_max = popularite
    #         activite_plus_populaire = activite
    return activite_plus_populaire


assert activite_populaire(trois_amis) == 'Velo'


# 4.3

def activite_deux_personnes(dic, nom1, nom2):
    activite_commmune = set()
    for activite in dic[nom1]:
        if activite in dic[nom2]:
            activite_commmune.add(activite)
    return activite_commmune


def activite_deux_personnes2(dic, nom1, nom2):
    return dic[nom1] & dic[nom2]


assert activite_deux_personnes(trois_amis, 'Camille', 'Claude') == {'Boxe', 'Velo'}
assert activite_deux_personnes(trois_amis, 'Camille', 'Claude') == activite_deux_personnes2(trois_amis, 'Camille',
                                                                                            'Claude')


# 4.4

def partage_activite(dic, nom1):
    res = {}
    for autre_personne in dic.keys():
        if nom1 != autre_personne:
            en_commun = activite_deux_personnes2(dic, nom1, autre_personne)
            if len(en_commun) != 0:
                res[autre_personne] = en_commun
    return res


assert partage_activite(trois_amis, 'Dominique') == {'Camille': {'Velo'}, 'Claude': {'Velo'}}

# Exercice 5
liste_pokemon = [('Bulbizarre', {'Plante', 'Poison'}, '001.png'), ('Herbizarre', {'Plante', 'Poison'}, '002.png'),
                 ('Abo', {'Poison'}, '023.png'),
                 ('Jungko', {'Plante'}, '254.png'), ('Mimiqui', {'Fee', 'Spectre'}, '423.png')]


def dictionnaire_type(liste_de_pokemon):
    res = {}
    for (nom, enssemble_de_types, _) in liste_de_pokemon:
        for typee in enssemble_de_types:
            if typee in res:
                res[typee].add(nom)
            else:
                res[typee] = {nom}
    return res


assert dictionnaire_type(liste_pokemon) == {'Plante': {'Bulbizarre', 'Jungko', 'Herbizarre'}, 'Poison': {'Bulbizarre', 'Abo', 'Herbizarre'}, 'Fee': {'Mimiqui'}, 'Spectre': {'Mimiqui'}}
# Exercice 6

exemple_version1={
    ('Beatles','Batterie'):'Ringo Starr',
    ('Beatles','Chant'):'John Lennon',
    ('Beatles','Clavier'):'John Lennon',
    ('Pink Floyd', 'Chant'):'Syd Barett',
    ('Pink Floyd'):'s'
}