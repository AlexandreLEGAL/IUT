#!/usr/bin/python3
from jinja2 import Environment, FileSystemLoader

from villes_de_France_modele import *

from villes_de_France_modele_de_secours import *

repertoire = "/pub/1A/DocNum/Eval4/images/"


def creer_html(fichier_template, fichier_sortie, **infos):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template(fichier_template)
    html = template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()


##### EXERCICE 1 ########

creer_html("villes_de_France_template.html", "PagesGenerees/toutes_les_villes.html",
           villes=toutes_les_villes,
           allregion=getAllRegion(regions_et_logos),
           info=getcommune_region_habitant(toutes_les_villes),
           )

##### EXERCICE 2 ########

# TODO
