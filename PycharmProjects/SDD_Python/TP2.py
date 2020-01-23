#######################################################################
# Feuille de TP 2
# NOM : Legal
#######################################################################


#######################################################################
print("==========================================")
print("Exercice : Dictionnaires")


def premieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    'liste' et les valeurs l'indice de la première occurence de chaque élément
    """
    res = {}
    for i in range(len(liste)):
        res[liste[i]] = res.get(liste[i], i)
    return res


# TESTS
liste = ['a', 'b', 'b', 'a', '!']
assert premieres_occurences(liste) == {'a': 0, 'b': 1, '!': 4}
assert premieres_occurences([]) == {}
print("Bravo ! Vous avez terminé la première question de cet exercice")


def dernieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    de 'liste' et les valeurs l'indice de la dernière occurence de chaque élément
    """
    res = {}
    for i in range(len(liste)):
        if liste[i] in res:
            del res[liste[i]]
        res[liste[i]] = res.get(liste[i], i)
    return res


# TESTS
liste = ['a', 'b', 'b', 'a', '!']
assert dernieres_occurences(liste) == {'a': 3, 'b': 2, '!': 4}
assert dernieres_occurences([]) == {}
print("Félicitation ! Vous avez brillamment terminé cet exercice")

#######################################################################
print("==========================================")
print("Exercice : les Avengers")


def intelligenceMoyenne(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : l'intelligence moyenne des personnages (float)
    """
    moy = 0
    for key in dico.keys():
        moy += int(dico.get(key)[1])
    moy = moy / len(dico)
    return moy


# exemple de dictionnaire bidon pour faire des tests :
superHero = {
    'Spiderman': (5, 5, 'araignée à quatre pattes'),
    'Hulk': (4, 7, "Grand homme vert"),
    'Agent 13': (2, 3, 'agent 13'),
    'M Becker': (2, 9, 'Expert en graphes'),
}
assert intelligenceMoyenne(superHero) == 6.0


# N OUBLIEZ PAS D ECRIRE AU MOINS UN TEST PAR FONCTION


def kikelplusfort(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : le nom du personnage le plus fort (str)
    """
    res = ""
    maxi = 0
    for key in dico.keys():
        if int(dico.get(key)[0]) > maxi:
            maxi = int(dico.get(key)[0])
            res = key
    return res


assert kikelplusfort(superHero) == 'Spiderman'


def combienDeCretins(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : le nombre de personnages dont l'intelligence est inférieure à la moyenne.
    """
    res = 0
    moy = intelligenceMoyenne(dico)
    for key in dico.keys():
        if int(dico.get(key)[1]) > moy:
            res += 1
    return res


assert combienDeCretins(superHero) == 2
print("Avez-vous pensé à écrire au moins un test par fonction ?")

#######################################################################
print("==========================================")
print("Exercice : la maison qui rend fou")

mqrf1 = {
    "Abribus": "Astus",
    "Jeancloddus": "Abribus",
    "Plexus": "Gugus",
    "Astus": None,
    "Gugus": "Plexus",
    "Saudepus": None
}

mqrf2 = {
    "Abribus": "Astus",
    "Jeancloddus": None,
    "Plexus": "Jeancloddus",
    "Astus": "Gugus",
    "Gugus": "Plexus",
    "Saudepus": "Bielorus",
}

mqrf3 = {
    "Abribus": "Astus",
    "Jeancloddus": None,
    "Plexus": "Saudepus",
    "Astus": "Gugus",
    "Gugus": "Plexus",
    "Saudepus": None,
}


def verifieCoherence(mqrf):
    """
    cette fonction vérifie que chaque guichet donne le formulaire ou renvoie vers un guichet qui existe.
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    ok = True
    i = 0
    while i < len(mqrf) and ok:
        for key in mqrf.keys():
            if mqrf.get(key) != key:
                res = False
    return ok


assert not verifieCoherence(mqrf1)
assert not verifieCoherence(mqrf2)
assert verifieCoherence(mqrf3)


def conditionDeCesar(mqrf):
    """
    cette fonction vérifie que la mqrf vérifie la condition de César : un guichet qui ne donne pas le formulaire doit renvoyer vers un guichet dont le nom est plus loin dans l'ordre alphabétique
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    pass


def quelGuichet(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou qui vérifie la condition de César
      - guichet est le nom d'un guichet de la mqrf
    résultat : le nom du guichet qui finit par donner le formulaire
    """
    pass


def possible(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou
      - guichet est le nom d'un guichet de la mqrf
    résultat : un booléen indiquant s'il est possible d'obtenir le formulaire A-38 dans la mqrf en commençant par s'adresser au guichet
    """
    pass


print("Avez-vous pensé à écrire au moins un test par fonction ?")
