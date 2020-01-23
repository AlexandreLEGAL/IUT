#! /usr/bin/python3

def Personne(nom, age, moyen):
    """
    creer une personne qui doit être représentée par un dictionnaire
    paramètres: nom:
                age:
                moyen:
    resultat:
    """
    res = {'Nom': nom, 'Age': age, 'Moyen de transport': moyen}
    return res


def get_nom(pers):
    """
    retourne le nom de la personne
    """
    return pers['Nom']


def get_age(pers):
    """
    retourne l'age de la personne
    """
    return pers['Age']


def get_moyen_transport(pers):
    """
    retourne le moyen de transport utilisé par la personne
    """
    return pers['Moyen de transport']


def set_nom(pers, nom):
    """
    change le nom de la persone
    """
    pers['Nom'] = nom


def set_age(pers, age):
    """
    change l'age de la personne
    """
    pers['Age'] = age


def set_moyen_transport(pers, moyen):
    """ 
    change le moyen de transport de la personne
    """
    pers['Moyen de transport'] = moyen


def affiche_personne(pers):
    """
    affiche une personne
    """
    print('-' * 10)
    print('Nom:', get_nom(pers))
    print('Age:', get_age(pers))
    print('Moyen de transport:', get_moyen_transport(pers))
    print('-' * 10)


def lire_fichier_personnes(nom_fic):
    """
    lit une liste de personnes contenue dans un fichier
    """
    fic = open(nom_fic)
    liste_pers = []
    for ligne in fic:
        [nom, age, moyen_trans] = ligne[:len(ligne) - 1].split(',')
        liste_pers.append(Personne(nom, age, moyen_trans))
    fic.close()
    return liste_pers


def affiche_liste_personnes(liste_pers):
    """
    affiche une liste de personnes
    """
    for personne in liste_pers:
        affiche_personne(personne)


def age_moyen_utilisateur_transport(liste_pers, nom_moyen_transport):
    """
    retourne l'age moyen des personnes qui utilise comme moyen de transport
    celui passé en paramètres. Si aucune personne n'utilise ce moyen de transport
    la fonction doit retourner -1
    """
    res = 0
    cpt = 0
    for personne in liste_pers:
        if personne['Moyen de transport'] == nom_moyen_transport:
            res += personne['Age']
            cpt += 1
    if cpt == 0:
        res = -1
    else:
        res /= cpt
    return res

def liste_moyens_transport(listePers):
    """
    retourne sous la forme d'une liste de chaines de caractères la liste des 
    moyens de transport utilisés par les personne de listePers
    """
    res = []
    for personne in listePers:
        if personne['Moyen de transport'] not in res:
            res.append(personne['Moyen de transport'])
    return res


### programme principal
if __name__ == '__main__':
    lire_fichier_personnes('personnes.txt')
    # ajoutez vos appels aux fonctions sur les personnes
