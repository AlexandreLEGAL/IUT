# Ex1
def croissant(liste):
    i = 1
    ok = True
    while i < len(liste) and ok:
        if liste[i - 1] > liste[i]:
            ok = False
        i += 1
    return ok


# Ex2
def soldes(objets_prix, rabais):
    nouveau_dico = {}
    for (objet, prix) in objets_prix.items():
        nouveau_dico[objet] = prix - (prix * rabais) / 100
    return nouveau_dico


objets_prix = {"Sable": 10, "Chocolat": 0.5, "Baguette": 1.5}
rabais = 20


def indiceMinimum(liste):
    """paramètre : liste est une liste d'éléments comparables
    """
    minimum = None
    indiceMin = None
    for i in range(len(liste)):
        l_i = liste[i]
        if minimum is None or l_i < minimum:
            minimum = l_i
            indiceMin = i
            # deuxième passage  ici
    return indiceMin


# assert indiceMinimum([4, 4, 4, 4]) == 5
def plusCourteChaine(liste):
    """paramètre  :  liste est une liste de chaines de caractères
    """
    longueursChaines = []
    for chaine in liste:
        longueursChaines.append(len(chaine))
    indicePlusCourteChaine = indiceMinimum(longueursChaines)
    if indicePlusCourteChaine == None:
        return None
    else:
        return liste[indicePlusCourteChaine]


animaux = ["veau", "vache", "cochon", "couvée"]
animalCourt = plusCourteChaine(animaux)


# print(animalCourt)


def frequences_initiales(liste):
    dico = {}
    for i in range(len(liste)):
        initiale = liste[i][0]
        if initiale in dico.keys():
            dico[initiale] = dico[initiale] + 1
        else:
            dico[initiale] = 1
    return dico


def acquiertAnimaux(troupeau, animal, nombre):
    """
    Cette fonction ajoute un certain nombre d'animaux dans le troupeau
    :param troupeau:
    :param animal:
    :param nombre:
    :return:
    """
    if animal in troupeau.keys():
        troupeau[animal] = troupeau[animal] + nombre
    else:
        troupeau[animal] = nombre
    return troupeau


tdp = {"veau": 14, "vache": 7, "poule": 42}
acquiertAnimaux(tdp, "vache", 23)
assert tdp == {'veau': 14, 'vache': 30, 'poule': 42}
acquiertAnimaux(tdp, 'girafe', 2)
assert tdp == {'veau': 14, 'vache': 30, 'poule': 42, 'girafe': 2}


def reunitTroupeaux(troupeau1, troupeau2):
    """Cette fonction réunit deux troupeaux d'animaux
    Paramètres :−deux dictionnaires dont les clés sont le nom des animaux et les clefs le nombre de ce type d'animal dans le troupeau
    Résultat : un nouveau dictionnaire qui est la réunion des deux troupeaux
    """
    res = {}
    for (animal, nombre) in troupeau1.items():
        acquiertAnimaux(res, animal, nombre)
    for (animal, nombre) in troupeau2.items():
        acquiertAnimaux(res, animal, nombre)
    return res


perrette = {'veau': 14, 'vache': 7, 'poule': 42}
jean = {'vache': 12, 'cochon': 17, 'veau': 3}
assert reunitTroupeaux(perrette, jean) == {'veau': 17, 'vache': 19, 'poule': 42, 'cochon': 17}

