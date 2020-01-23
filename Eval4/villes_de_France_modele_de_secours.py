from villes_de_France_données import regions_et_logos, toutes_les_villes

########################################################################
# MODELE DE SECOURS
########################################################################

liste_des_villes_par_regions = {
    'Île-de-France': [('Paris', 2220445), ('Saint-Denis', 110733), ('Boulogne-Billancourt', 116927),
                      ('Argenteuil', 108865), ('Montreuil', 104748), ('Nanterre', 93509), ('Vitry-sur-Seine', 91188),
                      ('Créteil', 91042), ('Asnières-sur-Seine', 86799), ('Versailles', 85461), ('Courbevoie', 84658),
                      ('Colombes', 84392), ('Aulnay-sous-Bois', 82314), ('Aubervilliers', 80273),
                      ('Rueil-Malmaison', 79204), ('Champigny-sur-Marne', 76450), ('Saint-Maur-des-Fossés', 75285),
                      ('Drancy', 68955), ('Issy-les-Moulineaux', 67360), ('Levallois-Perret', 65374),
                      ('Noisy-le-Grand', 64619), ('Cergy', 62979), ('Neuilly-sur-Seine', 62075), ('Antony', 61603),
                      ('Ivry-sur-Seine', 59793), ('Clichy', 59783), ('Villejuif', 57781), ('Sarcelles', 56828),
                      ('Épinay-sur-Seine', 55157), ('Pantin', 54852), ('Maisons-Alfort', 54841),
                      ('Le Blanc-Mesnil', 54227), ('Chelles', 53708), ('Évry', 53699), ('Meaux', 53526),
                      ('Fontenay-sous-Bois', 53272), ('Bondy', 53074), ('Clamart', 52457), ('Sartrouville', 51747),
                      ('Bobigny', 50479), ('Sevran', 50077), ('Corbeil-Essonnes', 49373), ('Vincennes', 49136),
                      ('Montrouge', 48954), ('Suresnes', 48526), ('Massy', 48372), ('Saint-Ouen', 47432),
                      ('Meudon', 45507), ('Alfortville', 45043), ('Mantes-la-Jolie', 44985), ('Puteaux', 44506),
                      ('Rosny-sous-Bois', 44448), ('Livry-Gargan', 43798), ('Choisy-le-Roi', 43405),
                      ('Gennevilliers', 43376), ('Noisy-le-Sec', 42607), ('Garges-lès-Gonesse', 41962),
                      ('La Courneuve', 40874), ('Melun', 40011), ('Saint-Germain-en-Laye', 39540), ('Gagny', 39195),
                      ('Bagneux', 38817), ('Pontault-Combault', 38135), ('Stains', 38022), ('Châtillon', 37089),
                      ('Savigny-sur-Orge', 37045), ('Poissy', 36994), ('Bagnolet', 36010),
                      ('Sainte-Geneviève-des-Bois', 35877), ('Villepinte', 35864), ('Neuilly-sur-Marne', 34955),
                      ('Conflans-Sainte-Honorine', 34876), ('Tremblay-en-France', 34704), ('Franconville', 34014),
                      ('Le Perreux-sur-Marne', 33720), ('Montigny-le-Bretonneux', 33252), ('Châtenay-Malabry', 33067),
                      ('Villeneuve-Saint-Georges', 32976), ('Houilles', 32481), ('Palaiseau', 32461),
                      ('Trappes', 31854), ('Plaisir', 31753), ('Les Mureaux', 31647), ('Goussainville', 31442),
                      ('Athis-Mons', 31434), ('Viry-Châtillon', 31350), ('Nogent-sur-Marne', 31292),
                      ('Vigneux-sur-Seine', 31074), ('Chatou', 30876), ('Charenton-le-Pont', 30774),
                      ("L'Haÿ-les-Roses", 30772), ('Malakoff', 30428), ('Savigny-le-Temple', 30172)],
    "Provence-Alpes-Côte d'Azur": [('Marseille', 858120), ('Nice', 343895), ('Toulon', 165584),
                                   ('Aix-en-Provence', 142149), ('Avignon', 92209), ('Antibes', 75731),
                                   ('Cannes', 73744), ('La Seyne-sur-Mer', 64675), ('Hyères', 56502), ('Fréjus', 53511),
                                   ('Arles', 52697), ('Grasse', 50409), ('Martigues', 48870), ('Cagnes-sur-Mer', 47811),
                                   ('Aubagne', 45128), ('Salon-de-Provence', 44187), ('Istres', 43463),
                                   ('Le Cannet', 42454), ('Gap', 40225), ('Draguignan', 40054), ('La Ciotat', 35631),
                                   ('Saint-Raphaël', 34567), ('Vitrolles', 34236), ('Marignane', 34154),
                                   ('Six-Fours-les-Plages', 33652)],
    'Auvergne-Rhône-Alpes': [('Lyon', 506615), ('Saint-Étienne', 170761), ('Grenoble', 160779),
                             ('Villeurbanne', 148543), ('Clermont-Ferrand', 141365), ('Annecy', 124401),
                             ('Vénissieux', 62575), ('Valence', 62150), ('Chambéry', 59490), ('Vaulx-en-Velin', 45294),
                             ('Saint-Priest', 44446), ('Caluire-et-Cuire', 42494), ('Bourg-en-Bresse', 40967),
                             ('Bron', 39283), ("Saint-Martin-d'Hères", 38100), ('Montluçon', 37289),
                             ('Montélimar', 37193), ('Villefranche-sur-Saône', 36559), ('Échirolles', 35875),
                             ('Roanne', 35200), ('Saint-Chamond', 35097), ('Thonon-les-Bains', 34973),
                             ('Annemasse', 34953), ('Romans-sur-Isère', 33366), ('Meyzieu', 32225),
                             ('Rillieux-la-Pape', 30529), ('Aix-les-Bains', 30291)],
    'Occitanie': [('Toulouse', 466297), ('Montpellier', 275318), ('Nîmes', 151075), ('Perpignan', 120605),
                  ('Béziers', 75701), ('Montauban', 58826), ('Narbonne', 52855), ('Albi', 49531),
                  ('Carcassonne', 45941), ('Sète', 44136), ('Castres', 41382), ('Tarbes', 40900), ('Alès', 39993),
                  ('Colomiers', 38541)],
    'Pays de la Loire': [('Nantes', 298029), ('Angers', 151056), ('Le Mans', 143813), ('Saint-Nazaire', 69350),
                         ('Cholet', 53853), ('La Roche-sur-Yon', 53162), ('Laval', 50073), ('Saint-Herblain', 44337),
                         ('Rezé', 39505)],
    'Grand Est': [('Strasbourg', 276170), ('Reims', 183042), ('Metz', 117619), ('Mulhouse', 111167), ('Nancy', 104321),
                  ('Colmar', 68784), ('Troyes', 60750), ('Charleville-Mézières', 48615),
                  ('Châlons-en-Champagne', 45002), ('Thionville', 41083), ('Haguenau', 34761), ('Épinal', 32006),
                  ('Schiltigheim', 31610)],
    'Nouvelle-Aquitaine': [('Bordeaux', 246586), ('Limoges', 134577), ('Poitiers', 87435), ('Pau', 77489),
                           ('La Rochelle', 74998), ('Mérignac', 69301), ('Pessac', 61514), ('Niort', 58311),
                           ('Bayonne', 48178), ('Brive-la-Gaillarde', 46961), ('Angoulême', 41955), ('Talence', 41182),
                           ('Anglet', 38633), ('Agen', 34126), ('Châtellerault', 31722), ("Villenave-d'Ornon", 31027),
                           ('Mont-de-Marsan', 31009), ('Périgueux', 30069)],
    'Hauts-de-France': [('Lille15', 233897), ('Amiens', 132479), ('Roubaix', 95600), ('Tourcoing', 95329),
                        ('Dunkerque17', 89160), ('Calais', 76402), ("Villeneuve-d'Ascq", 62869),
                        ('Saint-Quentin', 55878), ('Beauvais', 54738), ('Valenciennes', 43787),
                        ('Boulogne-sur-Mer', 42476), ('Wattrelos', 41337), ('Arras', 40970), ('Douai', 40736),
                        ('Compiègne', 40732), ('Marcq-en-Barœul', 39291), ('Creil', 34922), ('Cambrai', 32897),
                        ('Liévin', 31590), ('Lens', 31398), ('Maubeuge', 30347)],
    'Bretagne': [('Rennes', 213454), ('Brest', 139384), ('Quimper', 63513), ('Lorient', 57662), ('Vannes', 53036),
                 ('Saint-Malo', 45980), ('Saint-Brieuc', 45207)],
    'Normandie': [('Le Havre', 172807), ('Rouen', 110618), ('Caen', 106538), ('Cherbourg-en-Cotentin18', 80959),
                  ('Évreux', 49461), ('Dieppe', 30086)],
    'Bourgogne-Franche-Comté': [('Dijon', 153668), ('Besançon', 116690), ('Belfort', 49764),
                                ('Chalon-sur-Saône', 44985), ('Auxerre', 34843), ('Nevers', 34485), ('Mâcon', 34014)],
    'Centre-Val de Loire': [('Tours', 136125), ('Orléans', 114977), ('Bourges', 66528), ('Blois', 46351),
                            ('Châteauroux', 44479), ('Chartres', 38728), ('Joué-lès-Tours', 37748), ('Dreux', 31191)],
    'La Réunion': [('Saint-Paul', 104634), ('Saint-Pierre', 81583), ('Le Tampon', 76796), ('Saint-André', 55900),
                   ('Saint-Louis', 52803), ('Saint-Benoît', 37738), ('Saint-Joseph', 37362), ('Le Port', 35653),
                   ('Saint-Leu', 33575), ('Sainte-Marie', 33042), ('La Possession', 32261)],
    'Martinique': [('Fort-de-France', 83651), ('Le Lamentin', 39926)],
    'Corse': [('Ajaccio', 68587), ('Bastia', 43331)],
    'Guadeloupe': [('Les Abymes', 56001), ('Baie-Mahault', 30547)],
    'Guyane': [('Cayenne', 55817), ('Saint-Laurent-du-Maroni', 44169), ('Matoury', 31934)]
}