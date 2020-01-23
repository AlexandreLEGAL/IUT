#!/usr/bin/python3
# ===========
# Les données
# ===========
# source : https://swapi.co/

"""
vaisseaux_SW est un dictionnaire :
 - les clés sont le nom des vaisseau (str)
 - les valeurs sont des tuples (equipage, vitesse, image)
    * equipage : est le nombre total des membres d'équipage (int)
    * vitesse : est un nombre qui modélise la vitesse du vaisseau (float)
    * image est le nom de l'image qui illustre le vaisseau (str)
"""

vaisseaux_SW = {'CR90 corvette': (165, 2.0, 'cr90_vignette.jpg'),
                'Star Destroyer': (47060, 2.0, 'Star_Destroyer_Pellaeon_vi.jpg'), 'Slave 1': (1, 3.0, 'slaveI.jpg'),
                'Imperial shuttle': (6, 1.0, 'NuClasse_Attack_Shuttle_vi2.jpg'),
                'EF76 Nebulon-B escort frigate': (854, 2.0, 'Fregate_Nebulon_vi.jpg'),
                'Calamari Cruiser': (5400, 1.0, 'ConsularCruiser.jpg'), 'B-wing': (1, 2.0, 'bwing_v.jpeg'),
                'Republic Cruiser': (9, 2.0, 'pantorancruiser_vignette.jpg'),
                'Droid control ship': (175, 2.0, 'cannonieredroide.jpg'),
                'Naboo fighter': (1, 1.0, 'bombardiernaboo.jpg'), 'Naboo Royal Starship': (8, 1.8, 'nefroyale.jpg'),
                'Scimitar': (1, 1.5, 'ch_TIEscimitarvignette.jpg'), 'H-type Nubian yacht': (4, 0.9, 'nubian_yacht.jpg'),
                'Solar Sailer': (3, 1.5, 'Voilier1.jpg'), 'Death Star': (342953, 4.0, 'etoile_mort.jpg'),
                'X-wing': (1, 1.0, 'X-Wing-Fighter_47c7c342.jpeg'), 'Executor': (279144, 2.0, 'Executor_vi.jpg'),
                'Rebel transport': (6, 4.0, 'transport_resistance_vignette.jpg')}


# ================================
# Outils de traitement des données
# ================================

def nomVaisseaux(dic):
    """
    Renvoie la liste des noms de tous les vaisseaux
    dic : un dictionnaire
    """
    res = []
    for nom in dic.keys():
        res.append(nom)
    return res


assert nomVaisseaux({'Jean': (9, 5, 'image'), 'David': (5, 4, 'image')}) == ['Jean', 'David']


def nomVaisseaux_moins_de_5(dic):
    """
    Renvoie la liste des noms de tous les vaisseaux dont l'équipage est strictement inféreur à 5
    dic : un dictionnaire
    """
    res = []
    for (nom, (equipage, _, _)) in dic.items():
        if equipage < 5:
            res.append(nom)
    return res


assert nomVaisseaux_moins_de_5({'Jean': (9, 5, 'image'), 'David': (4, 4, 'image')}) == ['David']


# def tuple_vaisseaux_moins_de_5(dic):
#     """
#     Renvoie la tuple composer du nom de l'equipage et de la vitesse des vaisseaux dont l'équipage est strictement inféreur à 5
#     dic : un dictionnaire
#     """
#     res = []
#     for vaisseaux in dic.keys():
#         for (equipage, vitesse, _) in dic.values():
#             if [vaisseaux] in nomVaisseaux_moins_de_5(dic):
#                 res.append((vaisseaux, equipage, vitesse))
#     return res
#
#
# assert tuple_vaisseaux_moins_de_5({'Jean': (9, 5, 'image'), 'David': (4, 4, 'image')}) == [('David', 4, 4)]


def info_vaisseaux(dic):
    """
    Renvoie la tuple composer du nom de l'equipage et de la vitesse des vaisseaux
    dic : un dictionnaire
    """
    res = []
    for info in dic.values():
        res.append(info)
    return res


assert info_vaisseaux({'Jean': (9, 5, 'image'), 'David': (4, 4, 'image')}) == [(9, 5, 'image'), (4, 4, 'image')]
