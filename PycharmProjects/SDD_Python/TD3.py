def frequences(liste):
    res = {}
    for elem in liste:
        if elem not in res.keys():
            res[elem] = 1
        else:
            res[elem] += 1
    return res


liste_activite = [('Sommeil', 7.5), ('Repas', 0.25), ('Douche', 0.1), ('Transport', 0.75), ('Travail', 4), ('Repas', 1),
                  ('Sommeil', 0.5), ('Travail', 4.5)]


# assert occupation(liste_activite) == "Travail"

def occupation1(liste, truc):
    """
    renvoie l'occupation d'une personne
    :param liste:
    :return:
    """
    res = 0
    for (activite, temps) in liste:
        if activite == truc:
            res += temps
    return res


def occupation2(liste):
    """
    renvoie le dictionnaire du temps pris par chaque activité
    :param liste: tuple de 2 éléments
    :return:
    """
    res = {}
    for (activite, _) in liste:
        if activite not in res.keys():
            res[activite] = occupation1(liste, activite)
    return res


def occupation3(liste):
    """
    renvoie l'activité sur laquel on a passer le plus de temps
    :param liste:
    :return:
    """
    res = ""
    maxi = 0
    for (activite, temps) in occupation2(liste).items():
        if temps > maxi:
            res = activite
            maxi = temps
    return res


recettes = {'Kouglof': (20, 20, 'difficile'), 'Salade de fruits': (30, 0, 'facile'),
            'Mousse au chocolat': (25, 0, 'facile'), 'Gateau au yaourt': (10, 20, 'facile')}
magasin = {'Au panier Bio': (False, False), 'Au supermarché': (False, True), 'Au commerce du jour': (True, True)}
contient = {('Kouglof', 'Farine'), ('Kouglof', 'Raisins secs'), ('Kouglof', 'Oeufs'), ('Kouglof', 'Lait'),
            ('Salade de fruits', 'Fraises'), ('Salade de fruits', 'Pommes'), ('Salade de fruits', 'Bananes'),
            ('Salade de fruits', 'Oranges'), ('Salade de fruits', 'Raisins secs'), ('Salade de fruits', 'Noix'),
            ('Mousse au chocolat', 'Chocolat'), ('Mousse au chocolat', 'Oeufs'), ('Mousse au chocolat', 'Beurre'),
            ('Gateau au yaourt', 'Farine'), ('Gateau au yaourt', 'Yaourt'), ('Gateau au yaourt', 'Oeufs'),
            ('Gateau au yaourt', 'Lait')}
vend = {('Fraises', 'Au panier Bio'), ('Farine', 'Au panier Bio'), ('Raisins secs', 'Au panier Bio'),
        ('Oeufs', 'Au panier Bio'), ('Lait', 'Au panier Bio'), ('Pommes', 'Au panier Bio'),
        ('Fraises', 'Au supermarché'), ('Lait', 'Au supermarché'), ('Bananes', 'Au supermarché'),
        ('Oranges', 'Au supermarché'), ('Noix', 'Au supermarché'), ('Chocolat', 'Au supermarché'),
        ('Beurre', 'Au commerce du jour'), ('Yaourt', 'Au commerce du jour'), ('Chocolat', 'Au commerce du jour'),
        ('Oeufs', 'Au commerce du jour')}


def recettes_avec(ingredient, ingredients_recettes):
    """
    Renvoie la liste des recettes contenant 'ingredient'
    :param ingredient:
    :param ingredients_recettes:
    :return:
    """
    recettes_trouvees = set()
    for (ingr, recette) in ingredients_recettes.items():
        if ingr == ingredient:
            recettes_trouvees.add(recette)
    return recettes_trouvees


def ouvert_lundi(dico):
    ensemble = set()
    for (nom, jour) in dico.items():
        if jour[1]:
            ensemble.add(nom)
    return ensemble


print(ouvert_lundi(magasin))


def ingr_vendus(vend, magasin):
    res = set()
    for (ingr, mag) in vend:
        if mag == magasin:
            res.add(ingr)
    return res


print(ingr_vendus(vend, 'Au panier Bio'))
assert ingr_vendus(vend, 'Au panier Bio') == {'Fraises', 'Oeufs', 'Pommes', 'Farine', 'Lait', 'Raisins secs'}


def acheter_lundi(vend, magasin):
    res = set()
    mag_ouvert = str(ouvert_lundi(magasin))
    for mag in mag_ouvert:
        res.add(str(ingr_vendus(vend, mag)))
    return res


def recettes_lundi(vend, magasin, c):
    imp = set()
    toutes = set(recettes.keys())
    for (nom, ingr) in c:
        if not ingr in ingr_vendus(vend, magasin):
            imp.add(nom)
    return toutes - imp


print(recettes_lundi(vend, magasin, contient))
