# Exercice 1
groupePrefere = {'Florent': 'Chantal Goya', 'Celine': 'SuperBus',
                 'Julien': 'ACDC', 'Denys': 'ACDC', 'Caroline': 'Chantal Goya'}


def fansDe(dictionnaire, groupe):
    res = set()
    for (pers, gr) in dictionnaire.items():
        if gr == groupe:
            res.add(gr)
    return res


# Exercice 2.1
regimeAlimentaire = {
    'Requin': {'Nageur', 'Sac Plastique', 'Poisson'},
    'Nageur': {'Poisson', 'Noisette'},
    'Lion': {'Gazelle'},
    'Ecureuil': {'Noisette'}}
nourritureDisponible = {
    'Ocean': {'Poisson', 'Sac Plastique', 'Nageur'},
    'Savane': {'Gazelle'},
    'Jardin avec piscine': {'Nageur', 'Noisette'}
}


def inverse(dic):
    res = {}
    for (animal, liste_nourriture) in dic.items():
        for nourriture in liste_nourriture:
            if nourriture not in res:
                res[nourriture] = {animal}
            else:
                res[nourriture].add(animal)
    return res


# Exercice 2.2

def peutSurvivre(regimeAlimentaire, nourritureDisponible):
    res = {}
    for (lieu, liste_al) in nourritureDisponible.items():
        if lieu not in res.keys():
            res[lieu] = set()
        for (animal, enssemble_nourriture) in regimeAlimentaire.items():
            for nourriture in enssemble_nourriture:
                if nourriture in liste_al:
                    if animal not in res[lieu]:
                        res[lieu].add(animal)
    return res


# {Ocean : Requin}
print("==========================================")
print("Exercice 3 - Rapide et furieux, une série qui se répète un peu")


# Version 1
def nombre_apparition(chaine, caractere):
    cpt = 0
    for char in chaine:
        # ICI
        if caractere == char:
            cpt = cpt + 1
    return cpt


def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    caracteresRepetees = set()
    for caractere in chaine:
        if nombre_apparition(chaine, caractere) > 1:
            caracteresRepetees.add(caractere)
    return caracteresRepetees


print(caracteres_en_double("Yolo"))

print(caracteres_en_double("Tu lui brises le coeur, je te brise la tête !"))  # 45 caractères


# Version 2
def caracteres_en_double(chaine):
    """
    resultat : la liste des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu = []
    caracteres_repetes = []
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.append(caractere)
        else:
            caracteres_repetes.append(caractere)
    return caracteres_repetes


# Version 3
def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu = set()
    caracteres_repetes = set()
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.add(caractere)
        else:
            caracteres_repetes.add(caractere)
    return caracteres_repetes


print("==========================================")
print("Exercice 4 - Oh les amoureux !")

ATM = {'Armand': 'Beatrice', 'Beatrice': 'Cesar', 'Cesar': 'Dalida',
       'Dalida': 'Cesar', 'Etienne': 'Beatrice', 'Firmin': 'Henri',
       'Gaston': 'Beatrice', 'Henri': 'Firmin'}


def reciproque(dicoAmoureux):
    """
    revoie la liste des couples de personne qui sont amoureux l'un de l'autre
    """
    res = []
    for (personne, amant) in dicoAmoureux.items():
        if amant in dicoAmoureux.keys():
            if dicoAmoureux[amant] == personne:
                if (personne, amant) not in res and (amant, personne) not in res:
                    res.append((personne, amant))
    return res


assert len(reciproque(ATM)) == 2, "Il y a très certainement des couples en double"
assert ('Henri', 'Firmin') in reciproque(ATM) or ('Firmin', 'Henri') in reciproque(ATM)


# assert ('Dalida', 'Cesar') in reciproque(ATM) or ('Cesar', 'Dalida') in les_couples(ATM)

def soupirants(dic, pers):
    res = []
    for (personne, amant) in dic.items():
        if amant is pers:
            res.append(personne)
    return res

print("==========================================")
print("Exercice 6 - Le retour des timides maladifs")

amoursATM = {
    'Armand': {'Beatrice', 'Dalida'},
    'Beatrice': {'Cesar', 'Armand'},
    'Cesar': {'Dalida', 'Gaston'},
    'Dalida': {'Cesar', 'Armand'},
    'Etienne': {'Beatrice', 'Firmin'},
    'Firmin': {'Henri', 'Beatrice', 'Armand', 'Dalida'},
    'Gaston': {'Beatrice', 'Dalida', 'Cesar'},
    'Henri': {'Firmin', 'Armand', 'Cesar', 'Henri'}}
