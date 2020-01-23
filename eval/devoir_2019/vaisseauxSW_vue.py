#!/usr/bin/python3
# =====================
# NOM : 
# ====================

from jinja2 import Environment, FileSystemLoader  # ne pas modifier cette ligne
from vaisseauxSW_modele import *


# ne modifiez pas cette fonction
def creer_html(fichier_template, fichier_sortie, **infos):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template(fichier_template)
    html = template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()


creer_html("vaisseauxSW_template.html", "fichier_genere.html",
           liste_noms_vaisseaux=nomVaisseaux(vaisseaux_SW),
           liste_noms_vaisseaux_moins_de_5=nomVaisseaux_moins_de_5(vaisseaux_SW),
           info_vaisseaux=info_vaisseaux(vaisseaux_SW)
           )
