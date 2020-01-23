from villes_de_France_données import regions_et_logos, toutes_les_villes


########################################################################
# FICHIER MODELE
########################################################################

def getAllRegion(dic):
    """
    Renvoie la liste des Regions
    :param dic:
    :return:
    """
    res = []
    for (region, img) in dic.items():
        res.append(region)
    return res


assert getAllRegion({"moi": "pasmoi", "toi": "pastoi"}) == ["moi", "toi"]


def getcommune_region_habitant(dic):
    """
    Renvoie une liste de tuple composer de la comune, region, habitant
    :param dic:
    :return:
    """
    res = []
    for commune, (region, annee) in dic.items():
        res.append((commune, dic[commune][region], dic[commune][annee]))
    return res
