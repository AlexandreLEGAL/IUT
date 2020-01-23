# 1.1
liste = [1, 5, 7, 6, 4]


def score(n):
    return n % 5


m = min(liste, key=score)
# 1.2
liste1 = [(2, 6), (7, 6), (4, -1), (1, 5)]


def score1(c):
    return c[1] - c[0]


liste2 = sorted(liste1, key=score1)
# 1.3
liste3 = ['abeille', 'renard', 'canard', 'koala']


def f(L, k):
    def score2(s):
        return s[k]

    return sorted(L, key=score2)


liste4 = f(liste3, 2)
# 2.1
enssemble1 = {13, 5, 7, 6, 15, 14, 12}
enssemble2 = {7, 5, 9}


# def entier_consec(ensemble):
#     liste_trie = sorted(ensemble)
#     liste_de_liste_de_consec = []
#     m = 0
#     for i in range(len(liste_trie)):
#         if liste_trie[i] is liste_trie[0] or liste_trie[i - 1] != liste_trie[i] - 1:
#             liste_de_liste_de_consec.append([liste_trie[i]])
#             m += 1
#         else:
#             liste_de_liste_de_consec[m].append(liste_trie[i])
#     print(liste_de_liste_de_consec)
#     return max(liste_de_liste_de_consec, key=len)


def separe_consecutives(l):
    res = []
    plage_courante = []
    for elem in l:
        if plage_courante == [] or elem == plage_courante[-1] + 1:
            plage_courante.append(elem)
        else:
            res.append(plage_courante)
            plage_courante = [elem]
    res.append(plage_courante)
    return res


assert separe_consecutives([0, 1, 4, 5, 6, 9]) == [[0, 1], [4, 5, 6], [9]]


def plus_longue_sequence_consec(e):
    # tier e:
    l = sorted(e)
    sous_liste_consecutives = separe_consecutives(l)
    print(sous_liste_consecutives)
    return max(sous_liste_consecutives, key=len)


# 2.2
def elements_frequents(liste, k):
    dico_freq = {}
    for elem in liste:
        if elem in dico_freq:
            dico_freq[elem] += 1
        else:
            dico_freq[elem] = 1
    res = set()
    for (element, frequence) in dico_freq.items():
        if frequence >= k:
            res.add(element)
    return res


# 3.1
club_sportif = {'Aurelien': {'Saut a la perche', 'Lancer du marteau'},
                'Elsa': {'Lancer du marteau', 'Lancer de Javelot', 'Sport de chambre'},
                'Usain': {'110 metres haies', '100 metres'}}


def pratiquants(club, discipline):
    sportifs = []
    for (nom, sports) in club.items():
        if discipline in sports:
            sportifs.append(nom)
    return sportifs


# 3.2
def discipline_populaire(club):
    freq = {}
    for (personne, sport) in club.items():
        for d in sport:
            if d in freq:
                freq[d] += 1
            else:
                freq[d] = 1

    def frequence(d):
        return freq[d]

    return max(freq, key=frequence)


# 3.4
# def constituer_equipe(club, epreuves):
#
# 4.1
planches_exemple = [152, 161, 161, 170, 175, 185, 190, 200]
dic_presonnnes = {('Alexandra_Ledermann', 182), ('Bachir', 172),
                  ('Prof.Chen', 171), ('Dadada', 172), ('Esteban', 179), ('FantaXYou', 165)}


# 4.2
def triTaille(personnes):
    def Taille(T):
        return T[1]

    return sorted(personnes, key=Taille)


# 4.3
def attribution1(planches, personnes):
    """
    Renvoie un dictionnaire sous la forme:
    {'nom':tailleplanche}
    :param planches:
    :param personnes:
    :return:
    """
    res = {}
    for (pres, taill) in personnes:
        for planc in planches:
            if pres not in res.keys() and planc not in res.items():
                res[pres] = planc
            elif pres in res.keys() and abs(taill - res[pres]) > abs(taill - planc):
                res[pres] = planc
    return res
