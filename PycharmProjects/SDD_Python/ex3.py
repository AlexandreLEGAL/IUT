def huitcarac(pw):
    """
    Vérifie si le password contient au moins 8 caractères
    :param pw:
    :return un boolean:
    """
     i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res
    pass


def contient_chiffre(pw):
    """
    On vérifie si le password contient au moins 1 chiffre
    :param pw:
    :return un boolean:
    """
     i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res
    pass


def contient_espace(pw):
    """
    On vérifie si le password ne contient pas d'espace
    :param pw:
    :return un boolean:
    """
     i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res
    pass


def contient_maj(pw):
    """
    On vérifie si le password contient au moins une majuscule
    :param pw:
    :return un boolean:
    """
     i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res
    pass


def maj_consec(pw):
    """
    On vérifie si le password ne contient pas de majuscule consecutive
    :param pw:
    :return un boolean:
    """
    i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res


def contient_ponc(pw):
    """
    On vérifie si le password ne contient pas de ponctuation
    :param pw:
    :return un boolean:
    """
     i = 1
    res = False
    while i < len(pw)-1 and res == False:
        if pw[i].isupper() and pw[i + 1].isupper():
            res = True
        i += 1
    if pw[-1].isupper() and pw[-2].isupper():
        res = True
    return res
    pass
